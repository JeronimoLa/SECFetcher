import json
import os
import sys


def get_configuration():    
    with open("config.json", "r") as file:
        data = json.loads(file.read())
    return data

if __name__ == "__main__":
    data = get_configuration()
    print(data)