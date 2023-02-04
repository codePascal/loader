import json


def load_json(path):
    with open(path, 'r') as out:
        data = json.load(out)
    return data
