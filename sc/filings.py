import requests
import json
import time
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import get_configuration

config = get_configuration()


def filings():
    url = "https://data.sec.gov/submissions/CIK0000320193.json"
    headers =  config["user_agent"]

    response = requests.get(url=url, headers=headers)
    data = response.json()


    keys_under_filings = data["filings"].keys()
    print(keys_under_filings)
    print()

    recent_file_keys = data["filings"]["recent"].keys()
    print(f'Dictionary keys under ["filings"] -> ["recent"] -> {recent_file_keys}\n')

    print(f'Dictionary keys under filings -> files ->  {type(data["filings"]["files"])}')


    for key in recent_file_keys:
        # time.sleep(2)
        # print(f"Key name: {key} -- length of the value {len(data['filings']['recent'].get(key))} - data type {type(data['filings']['recent'].get(key))}")
        value = data['filings']['recent'].get(key)[0]
        if isinstance(value, str):
            length = len(value) * 5
            if length % 1 == 0:
                print(f"{key} = Column(String({(length)}))")
            else:
                print(f"{key} = Column(String({(length-1)}))")
        else:
            print(f"{key} = Column(Integer)")

if __name__ == "__main__":
    filings()





    # print(f"key" )
    # try:
    #     print(f"data type -- {type(data['filings']['recent'].get(key)[0])} length of string {len(data['filings']['recent'].get(key)[0])}")
    # except Exception:
    #     print(f"data type -- {type(data['filings']['recent'].get(key)[0])} length of string {data['filings']['recent'].get(key)}")

# my_list = []
# for key in recent_file_keys:
#     my_lists = data['filings']['recent'].get(key)
#     my_list.append(my_lists)


# print(tuple(recent_file_keys))
# for element in zip(*my_list):
#     print(element)
# for 
    # for i in range(len( data['filings']['recent'].get(key))):
    #     print(data['filings']['recent'].get(key))

    # print(data['filings']['recent'].get(key))
