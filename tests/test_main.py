from stock.data.model import crud
from sqlalchemy.orm import Session
import pytest

@pytest.fixture
def db():
    from stock.data.model import models
    from stock.data.model import schemas
    from stock.data.model.database import SessionLocal, engine

    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_get_ticker(db: Session):
    ticker = crud.get_ticker(db, ticker_id=1)
    assert ticker.id == 1
    assert ticker.ticker == "AAPL"

def test_get_tickers(db: Session):
    tickers = crud.get_tickers(db)
    assert len(tickers) == 3

def test_get_ticker_by_name(db: Session):
    ticker = crud.get_ticker_by_name(db, ticker="AAPL")
    assert ticker.id == 1
    assert ticker.ticker == "AAPL"

def test_get_exchange(db: Session):
    exchange = crud.get_exchange(db, exchange_id=1)
    assert exchange.id == 1
    assert exchange.exchange == "NASDAQ"

def test_get_exchanges(db: Session):
    exchanges = crud.get_exchanges(db)
    assert len(exchanges) == 3
