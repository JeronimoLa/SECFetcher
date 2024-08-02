import json

def get_configuration():
    with open("config.json", "r") as file:
        data = json.loads(file.read())
    return data