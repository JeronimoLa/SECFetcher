import requests
import json
import time
from config import get_configuration


config = get_configuration()

def filings():
    url = "https://data.sec.gov/submissions/CIK0000320193.json"
    headers =  config["user_agent"]

    response = requests.get(url=url, headers=headers)
    data = response.json()

    keys_under_filings = data["filings"].keys()
    print()
    print(keys_under_filings)

    recent_file_keys = data["filings"]["recent"].keys()
    print(f'\n\nDictionary keys inside ["filings"]["recent"] -> {recent_file_keys}\n\n')

    for key in recent_file_keys:
        # print(f"Key name: {key} -- length of the value {len(data['filings']['recent'].get(key))} - data type {type(data['filings']['recent'].get(key))}")
        value = data['filings']['recent'].get(key)[0]
        if isinstance(value, str):
            length = len(value) * 5 + 5
            print(f"{key} = Column(String({(length)}))")
        else:
            print(f"{key} = Column(Integer)")


if __name__ == "__main__":
    filings()
