
import requests
import json
import time
from config import get_configuration


config = get_configuration()

def accounts_payable():
    """ The company-concept API returns all the XBRL disclosures from a single company (CIK) and concept (a taxonomy and tag) into a single JSON file,
    with a separate array of facts for each units on measure that the company has chosen to disclose (e.g. net profits reported in U.S. dollars and in 
    Canadian dollars)."""

    url = "https://data.sec.gov/api/xbrl/companyconcept/CIK0000320193/us-gaap/AccountsPayableCurrent.json"
    headers =  config["user_agent"]

    response = requests.get(url=url, headers=headers)
    data = response.json()
    keys = data.keys()
    print(keys)


if __name__ == "__main__":
    accounts_payable()

