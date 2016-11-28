import json
import requests


SERVER_URL = 'http://192.168.83.20:8000/apis/'
EVENT_URL = SERVER_URL + 'events/'
FIELD_URL = SERVER_URL + 'fields/'
USER_URL = SERVER_URL + 'users/'


def ingest_events():
    print('Requirement #1 Ingest events')
    error_count = 0
    for x, line in enumerate(open('sample_events.txt').readlines()):
        event = json.loads(line)
        r = requests.post(EVENT_URL, json=event,)
        if r.status_code > 299:
            error_count += 1
            print('line: {} code: {} error: {}'.format(x + 1, r.status_code, r.text))
    print('{} errors found'.format(error_count))


def get_user(user_id):
    return requests.get(USER_URL + '{}/'.format(user_id)).json()


def test_api():
    ingest_events()

    print('\nRequirement #2')
    print('All events created by user 162\n')
    for event in requests.get(EVENT_URL + '?user_id=162').json():
        print(event)

    print('\nRequirement #3')
    print('All users who affected field 176\n')
    field = requests.get(FIELD_URL + '176/').json()
    print(field)
    print('Created by: {}'.format(get_user(field['created_by'])))
    print('Planted by: {}'.format(get_user(field['planted_by'])))
    print('Fertilized by: {}'.format(get_user(field['fertilized_by'])))

    print('\nRequirement #4')
    print('All events after 2016-11-01T16:56:55.436642 and before 2016-11-01T16:56:56.437836.\n')
    args = '?timestamp_gt=2016-11-01T16:56:55.436642&timestamp_lt=2016-11-01T16:56:56.437836'
    for event in requests.get(EVENT_URL + args).json():
        print(event)

    print("\nState of all fields that weren't deleted")
    for field in requests.get(FIELD_URL).json():
        print(field)


if __name__ == '__main__':
    test_api()
