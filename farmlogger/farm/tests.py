import json
import pytz

from django.test import TestCase
from django.utils.dateparse import parse_datetime
from farmlogger.farm.models import (
    Event, User, Field
)


class EventTestCase(TestCase):
    def _parse_date_string(self, date_string):
        return pytz.timezone('UTC').localize(parse_datetime(date_string))

    def _create_user(self):
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:10.162098",
                "event": "user:create",
                "entity": {
                    "email": "derrick_clark@example.com",
                    "id": 2,
                    "name": "Derrick Clark"
                },
            }),
            content_type='application/json',
        )
        return User.objects.get(pk=2)

    def _create_field(self, id_=3):
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:10.162371",
                "event": "field:create",
                "entity": {
                    "acres": 95,
                    "user_id": 2,
                    "id": id_,
                    "name": "Game Land"
                }
            }),
            content_type='application/json',
        )
        return Field.objects.get(pk=id_)

    def setUp(self):
        self.user = self._create_user()

    def test_event_created(self):
        event = Event.objects.all().first()
        self.assertEqual(event.event, 'user:create')
        self.assertEqual(event.timestamp,
                         self._parse_date_string("2016-11-01T16:56:10.162098"))

    def test_user_created(self):
        self.assertEqual(self.user.email, "derrick_clark@example.com")
        self.assertEqual(self.user.name, "Derrick Clark")

    def test_field_created(self):
        field = self._create_field()
        self.assertEqual(field.acres, 95)
        self.assertEqual(field.name, "Game Land")
        self.assertEqual(field.created_by, self.user)

    def test_field_deleted(self):
        self._create_field()
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:11.164781",
                "event": "field:delete",
                "entity": {
                    "acres": 95,
                    "user_id": 2,
                    "id": 3,
                    "name": "Game Land"
                }
            }),
            content_type='application/json',
        )
        with self.assertRaises(Field.DoesNotExist):
            Field.objects.get(pk=3)

    def test_field_fertilized(self):
        self._create_field()
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:11.164861",
                "event": "fertilizing:create",
                "entity": {
                    "user_id": 2,
                    "field_id": 3,
                    "id": 5,
                    "type": "Anhydrous Amonia"
                }
            }),
            content_type='application/json',
        )
        field = Field.objects.get(pk=3)
        self.assertEqual(field.fertilizer_type, 'Anhydrous Amonia')
        self.assertEqual(field.fertilization_time,
                         self._parse_date_string("2016-11-01T16:56:11.164861"))
        self.assertEqual(field.fertilized_by, self.user)

    def test_user_deleted(self):
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:12.167463",
                "event": "user:delete",
                "entity": {
                    "email": "derrick_clark@example.com",
                    "id": 2,
                    "name": "Derrick Clark"
                }
            }),
            content_type='application/json',
        )
        self.assertTrue(User.objects.get(pk=2).deleted)

    def test_field_updated(self):
        self._create_field()
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:14.171529",
                "event": "field:update",
                "entity": {
                    "acres": 150,
                    "user_id": 2,
                    "id": 3,
                    "name": "Game Land2"
                }
            }),
            content_type='application/json',
        )
        field = Field.objects.get(pk=3)
        self.assertEqual(field.acres, 150)
        self.assertEqual(field.name, "Game Land2")

    def test_planting_created(self):
        self._create_field()
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:18.191173",
                "event": "planting:create",
                "entity": {
                    "user_id": 2,
                    "field_id": 3,
                    "id": 10,
                    "crop": "Clover"
                }
            }),
            content_type='application/json',
        )
        field = Field.objects.get(pk=3)
        self.assertEqual(field.crop, "Clover")
        self.assertEqual(field.planted_by, self.user)
        self.assertEqual(field.planting_time,
                         self._parse_date_string("2016-11-01T16:56:18.191173"))

    def test_rainfall_recorded(self):
        self._create_field()
        field = self._create_field(id_=4)
        field.total_rainfall = 2
        field.save()
        self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:21.206149",
                "event": "rainfall",
                "entity": {
                    "start": "2016-11-01T15:12:21.206135",
                    "amount": 6.792917597561106,
                    "end": "2016-11-01T16:56:21.206147",
                    "fields": [3, 4]
                }
            }),
            content_type='application/json',
        )
        field3 = Field.objects.get(pk=3)
        field4 = Field.objects.get(pk=4)
        self.assertAlmostEqual(field3.total_rainfall, 6.792917597561106, places=10)
        self.assertEqual(field3.last_rainfall,
                         self._parse_date_string("2016-11-01T16:56:21.206147"))
        self.assertAlmostEqual(field4.total_rainfall, 8.792917597561106, places=10)
        self.assertEqual(field4.last_rainfall,
                         self._parse_date_string("2016-11-01T16:56:21.206147"))

    def test_400_if_field_does_not_exist(self):
        r = self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:14.171529",
                "event": "field:update",
                "entity": {
                    "acres": 150,
                    "user_id": 2,
                    "id": 3,
                    "name": "Game Land2"
                }
            }),
            content_type='application/json',
        )
        self.assertEqual(r.status_code, 400)

    def test_400_if_user_deleted(self):
        user = User.objects.get(pk=2)
        user.deleted = True
        user.save()
        r = self.client.post(
            '/apis/events/',
            json.dumps({
                "timestamp": "2016-11-01T16:56:12.167463",
                "event": "user:delete",
                "entity": {
                    "email": "derrick_clark@example.com",
                    "id": 2,
                    "name": "Derrick Clark"
                }
            }),
            content_type='application/json',
        )
        self.assertEqual(r.status_code, 400)
