import json

def json_write_file(data, filename="", mode='w'):
    with open(filename, mode, encoding='utf-8') as json_file:
        json.dump(data, json_file)

def json_read_file(filename="", mode='r'):
    with open(filename, mode) as json_file:
        load_dict = json.load(json_file)
    return load_dict