from django.db import models
from django.contrib.postgres.fields import JSONField

EVENT_CHOICES = (
    ('user:create', 'user:create'),
    ('user:delete', 'user:delete'),
    ('field:create', 'field:create'),
    ('field:update', 'field:update'),
    ('field:delete', 'field:delete'),
    ('planting:create', 'planting:create'),
    ('fertilizing:create', 'fertilizing:create'),
    ('rainfall', 'rainfall'),
)


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)


class Field(models.Model):
    created_by = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    acres = models.IntegerField()

    planted_by = models.ForeignKey(User, null=True, related_name="plantings")
    planting_time = models.DateTimeField(null=True)
    crop = models.CharField(max_length=255)

    total_rainfall = models.FloatField(default=0)
    last_rainfall = models.DateTimeField(null=True)

    fertilized_by = models.ForeignKey(User, null=True, related_name="fertilizations")
    fertilizer_type = models.CharField(max_length=50)
    fertilization_time = models.DateTimeField(null=True)


class Event(models.Model):
    user = models.ForeignKey(User, null=True)
    fields = models.ManyToManyField(Field)
    timestamp = models.DateTimeField()
    event = models.CharField(max_length=100, choices=EVENT_CHOICES)
    entity = JSONField()
