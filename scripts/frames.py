


# https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json



import requests
import json
import time
from config import get_configuration


config = get_configuration()

def frames():
    """ The xbrl/frames API aggregates one fact for each reporting entity that is last filed that most closely 
    fits the calendrical period requested. This API supports for annual, quarterly and instantaneous data: """

    url = "https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json"

    headers =  config["user_agent"]

    response = requests.get(url=url, headers=headers)
    data = response.json()
    keys = data.keys()

    print(data)
    print(keys)

    
if __name__ == "__main__":
    frames()

