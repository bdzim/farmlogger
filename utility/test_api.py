import json
import requests


SERVER_URL = 'http://192.168.83.20:8000/apis/'
EVENT_URL = SERVER_URL + 'events/'


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


def test_api():
    ingest_events()

    print('\nRequirement #2')
    print('All events created by user 162\n')
    for event in requests.get(EVENT_URL + '?user_id=162').json():
        print(event)

    print('\nRequirement #4')
    print('All events after 2016-11-01T16:56:55.436642 and before 2016-11-01T16:56:56.437836.\n')
# after 346 and before 357
    args = '?timestamp_gt=2016-11-01T16:56:55.436642&timestamp_lt=2016-11-01T16:56:56.437836'
    for event in requests.get(EVENT_URL + args).json():
        print(event)


if __name__ == '__main__':
    test_api()
