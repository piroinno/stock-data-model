from stock.data.model import crud, models
import os
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from stock.data.model.database import SessionLocal, Base, engine

def init_test_db():
    Base.metadata.create_all(bind=engine)

def drop_test_db():
    Base.metadata.drop_all(bind=engine)

def recreate_test_db():
    drop_test_db()
    init_test_db()

@pytest.fixture(scope="session")
def db():
    recreate_test_db()
    db = SessionLocal()
    add_timezone(db)
    add_country(db)
    add_city(db)
    add_exchanges(db)
    add_ticker(db)
    try:
        yield db
    finally:
        db.close()

def add_timezone(db: SessionLocal):
    # Add test data
    crud.set_timezone(db, timezone=models.TimezoneModel(
        name="Eastern Standard Time", abbr="EST", dst="EDT"
    ))

    crud.set_timezone(db, timezone=models.TimezoneModel(
        name="Greenwich Mean Time", abbr="GMT", dst="BST"
    ))

def add_city(db: SessionLocal):
    # Add test data
    crud.set_city(db, city=models.CityModel(
        name="New York", country_id=1
    ))

    crud.set_city(db, city=models.CityModel(
        name="London", country_id=2
    ))

def add_country(db: SessionLocal):
    # Add test data
    crud.set_country(db, country=models.CountryModel(
        name="United States", code="US"
    ))

    crud.set_country(db, country=models.CountryModel(
        name="United Kingdom", code="UK"
    ))

def add_ticker(db: SessionLocal):
    # Add test data
    crud.set_ticker(db, ticker=models.TickerModel(
        ticker="AAPL", name="Apple Inc.", exchange_id=1
    ))

def add_exchanges(db: SessionLocal):
    # Add test data
    crud.set_exchange(db, exchange=[
        models.ExchangeModel(
            name="National Association of Securities Dealers Automated Quotations", country_id=1, city_id=1, timezone_id=1,
            acronym="NASDAQ", mic="XNAS"
        )
    ])

    crud.set_exchange_list(db, exchange=[
        models.ExchangeModel(
            name="New York Stock Exchange", country_id=1, city_id=1, timezone_id=1,
            acronym="NYSE", mic="XNYS"
        )
    ])

    crud.set_exchange_list(db, exchange=[
        models.ExchangeModel(
            name="London Stock Exchange", country_id=2, city_id=2, timezone_id=2,
            acronym="LSE", mic="XLON"
        )
    ])


def test_get_ticker(db: SessionLocal):
    ticker = crud.get_ticker(db, ticker_id=1)
    assert ticker.id == 1
    assert ticker.ticker == "AAPL"

def test_get_tickers(db: SessionLocal):
    tickers = crud.get_tickers(db)
    assert len(tickers) == 1

def test_get_ticker_by_name(db: SessionLocal):
    ticker = crud.get_ticker_by_name(db, ticker="AAPL")
    assert ticker.id == 1
    assert ticker.ticker == "AAPL"

def test_get_exchange(db: SessionLocal):
    exchange = crud.get_exchange(db, exchange_id=1)
    assert exchange.id == 1
    assert exchange.exchange == "NASDAQ"

def test_get_exchanges(db: SessionLocal):
    exchanges = crud.get_exchanges(db)
    assert len(exchanges) == 3
