import json


def test_api():
    fields_fertilized = {}
    for line in open('sample_events.txt').readlines():
        event = json.loads(line)
        if event['event'] == 'fertilizing:create':
            if event['entity']['field_id'] in fields_fertilized:
                print('duplicate fertilization: ', event)
            else:
                print('unique')
                fields_fertilized[event['entity']['field_id']] = True
    print(fields_fertilized)


if __name__ == '__main__':
    test_api()
