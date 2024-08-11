
import requests
import json
import time
from config import get_configuration


config = get_configuration()

def company_facts():
    """ This API returns all the company concepts data for a company into a single API call: """

    url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json"

    headers =  config["user_agent"]

    response = requests.get(url=url, headers=headers)
    data = response.json()
    keys = data.keys()

    print(keys)

    # print(data["entityName"])
    print(data["facts"].keys())

    for item in data["facts"]["dei"]["EntityCommonStockSharesOutstanding"]["units"]["shares"]:
        print(item)

    for k in (data["facts"]["us-gaap"].keys()):
        value = data["facts"]["us-gaap"].get(k)
        for j in value["units"]:
            for l in value["units"][j]:
                print(l)
        # print(value["units"].keys())

    
if __name__ == "__main__":
    company_facts()

