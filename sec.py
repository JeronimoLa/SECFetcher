import requests
import json
import time
import logging

from config import get_configuration
from database.models import CompanyData, ProdCompanyData
from database.db_engine import session
from sqlalchemy import text

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

    def __init__(self, cik, ticker):
        self.base_url = "https://data.sec.gov/"
        self.headers = config["user_agent"]
        self.cik = self.validate_length(str(cik))
        self.ticker = ticker


    def validate_length(self, cik, required_length=10):
        """ Ensures all CIK's are a length of 10"""
        return "0"*(required_length - len(cik)) + cik


    def push_to_db(self, submission_data, value):
        import hashlib
        primary_key = hashlib.sha256(value.encode('utf-8')).hexdigest()

        key = { "id": primary_key }
        # print(submission_data.keys())
        #call the database and check the primiary key created just not against the existing one inside of the database

        my_query = f""" 
                SELECT id FROM prod_company_data
                WHERE tickers = '{{{self.ticker}}}'"""
        try:
            results = session.execute(text(my_query)).fetchall()
            # print(type(results))
            # print(results)
        except Exception:
            print(e)
        self.validate_existing_entry(results, primary_key)
        # time.sleep(5)
        res = {**key, **submission_data}
        return res


    def validate_existing_entry(self, new_key, existing_key):
        time.sleep(3)
        new = new_key[0]
        print(new[0])
        print(existing_key)

        if new[0] == existing_key:
            print("match found")




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
    headers = config["user_agent"]
    res = requests.get(url, headers=headers)
    data = res.json()

    cik_strm = [[index['cik_str'],index['ticker'],index['title']] for index in data.values() ]

    database_data = []

    n = 10
    for x in chunks(cik_strm, n):
        time.sleep(10)
        try:
            for stock in x:
                try:         
                    fetcher = FinanceData(cik=stock[0], ticker=stock[1])
                    data = fetcher.get_stock_submissions()
                    # time.sleep(100)
                    database_data.append(data)
                except Exception as e:
                    logging.info(f"An error occurred at getting stock data: {e}")
            # validate_existing_entry(database_data) # I can check against them once the i have iterateed for the chunk size or do it individually
            # time.sleep(1000)
            session.bulk_insert_mappings(ProdCompanyData, database_data)
            session.commit()
        except Exception as i:
            logging.info(f"An error occurred commit to database: {i}")
            session.rollback()
        database_data = []
    session.commit()


if __name__ == "__main__":
    main()



