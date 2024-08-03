import requests
import json
import time
import logging

from config import get_configuration
from database.models import CompanyData, ProdCompanyData
from database.db_engine import session

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

config = get_configuration()


class FinanceData:
    def __init__(self, cik):
        self.cik = self.validate_length(str(cik))
        self.base_url = "https://data.sec.gov/"
        self.headers = config["User-Agent"]
        self.aggregator = False


    def validate_length(self, cik, required_length=10):
        """ Ensures all CIK's are a length of 10"""
        return "0"*(required_length - len(cik)) + cik


    def push_to_db(self, submission_data, value):
        import hashlib
        hash_string = hashlib.sha256(value.encode('utf-8')).hexdigest()

        primary_key = { "id": hash_string }
        res = {**primary_key, **submission_data}
        return res


    def vaidate_existing_entry():pass


    def get_stock_submissions(self):

        db_submission = []

        ticker_submissions_url = f"{self.base_url}submissions/CIK{self.cik}.json"
        print(ticker_submissions_url) # convert to log file
        res = requests.get(url=ticker_submissions_url, headers=self.headers)
        try:
            data = res.json()  # serializes the response object and turns it into a dict
        except JSONDecodeError:
            print('Response could not be serialized') 
        
        id_value = self.cik + str(data['filings'])   

        # if id_value == query_entry:

        full_data = self.push_to_db(data, id_value)
        return full_data


def chunks(my_list, n):
    results = []
    for i in range(0, len(my_list), n):        
        results = my_list[i:i+n]
        yield results
        # for item in my_list:
        #     print(item)


def main():

    url =  "https://www.sec.gov/files/company_tickers.json"
    headers =  {
        "User-Agent": "AdminContact@jeronimo.landafloresx19@gmail.com",
        "Host": "www.sec.gov" 
    }

    res = requests.get(url, headers=headers)
    data = res.json()

    cik_strm = [[index['cik_str'],index['ticker'],index['title']] for index in data.values() ]

    database_data = []

    n = 10
    for x in chunks(cik_strm, n):
        time.sleep(1)
        try:
            for stock in x:
                try:             
                    fetcher = FinanceData(cik=stock[0])
                    data = fetcher.get_stock_submissions()
                    database_data.append(data)
                except Exception as e:
                    logging.info(f"An error occurred at getting stock data: {e}")
            session.bulk_insert_mappings(ProdCompanyData, database_data)
            session.commit()
        except Exception as i:
            logging.info(f"An error occurred commit to database: {i}")
            session.rollback()
        database_data = []
    session.commit()


if __name__ == "__main__":
    main()



