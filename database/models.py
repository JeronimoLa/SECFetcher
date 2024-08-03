from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import declarative_base

try: 
    from database.db_engine import engine
except:
    from db_engine import engine


Base = declarative_base()

################################################
#        SCHEMA'S FOR POSTGRES DATABASE        #
################################################

class CompanyData(Base):
    __tablename__ = 'dev_company_data'

    id = Column(String(64), primary_key=True)

    cik = Column(String(100))
    entityType = Column(String(100))
    sic = Column(String(100))
    sicDescription = Column(String(100))
    insiderTransactionForOwnerExists = Column(Integer)
    insiderTransactionForIssuerExists = Column(Integer)
    name = Column(String(100))
    tickers = Column(ARRAY(String(50)))
    exchanges = Column(ARRAY(String(50)))
    ein = Column(String(100))
    description = Column(String(100))
    website = Column(String(100))
    investorWebsite = Column(String(100))
    category = Column(String(100))
    fiscalYearEnd = Column(String(100))
    stateOfIncorporation = Column(String(100))
    stateOfIncorporationDescription = Column(String(100))
    addresses = Column(JSON)
    phone = Column(String(100))
    flags = Column(String(100))
    formerNames = Column(JSON)
    filings = Column(JSON)


class ProdCompanyData(Base):
    __tablename__ = 'prod_company_data'

    id = Column(String(64), primary_key=True)

    cik = Column(String(100))
    entityType = Column(String(100))
    sic = Column(String(100))
    sicDescription = Column(String(100))
    insiderTransactionForOwnerExists = Column(Integer)
    insiderTransactionForIssuerExists = Column(Integer)
    name = Column(String(100))
    tickers = Column(ARRAY(String(50)))
    exchanges = Column(ARRAY(String(50)))
    ein = Column(String(100))
    description = Column(String(100))
    website = Column(String(100))
    investorWebsite = Column(String(100))
    category = Column(String(100))
    fiscalYearEnd = Column(String(100))
    stateOfIncorporation = Column(String(100))
    stateOfIncorporationDescription = Column(String(100))
    addresses = Column(JSON)
    phone = Column(String(100))
    flags = Column(String(100))
    formerNames = Column(JSON)
    filings = Column(JSON)


class ProdCompanyFilingsData(Base):
    __tablename__ = 'prod_company_filings_data'

    id = Column(String(64), primary_key=True)

    accessionNumber = Column(String(100))
    filingDate = Column(String(50))
    reportDate = Column(String(50))
    acceptanceDateTime = Column(String(120))
    act = Column(String(10))
    form = Column(String(15))
    fileNumber = Column(String(45))
    filmNumber = Column(String(45))
    items = Column(String(45))
    size = Column(Integer)
    isXBRL = Column(Integer)
    isInlineXBRL = Column(Integer)
    primaryDocument = Column(String(85))
    primaryDocDescription = Column(String(15))


class DevCompanyData(Base):
    __tablename__ = 'dev_company_filings_data'

    id = Column(String(64), primary_key=True)

    accessionNumber = Column(String(100))
    filingDate = Column(String(50))
    reportDate = Column(String(50))
    acceptanceDateTime = Column(String(120))
    act = Column(String(10))
    form = Column(String(15))
    fileNumber = Column(String(45))
    filmNumber = Column(String(45))
    items = Column(String(45))
    size = Column(Integer)
    isXBRL = Column(Integer)
    isInlineXBRL = Column(Integer)
    primaryDocument = Column(String(85))
    primaryDocDescription = Column(String(15))


if __name__ == "__main__":
    Base.metadata.create_all(engine)
