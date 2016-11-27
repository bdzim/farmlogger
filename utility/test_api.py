import json
import requests


SERVER_URL = 'http://192.168.83.20:8000/apis/'
EVENT_URL = SERVER_URL + 'events/'


def test_api():
    error_count = 0
    for x, line in enumerate(open('sample_events.txt').readlines()):
        event = json.loads(line)
        r = requests.post(EVENT_URL, json=event,)
        if r.status_code > 299:
            error_count += 1
            print('line: {} code: {} error: {}'.format(x, r.status_code, r.text))
    print('{} errors found'.format(error_count))

    print('\nRequirement #1')
    for event in requests.get(EVENT_URL, json=event,)


if __name__ == '__main__':
    test_api()
