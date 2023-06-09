import os
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

connect_args = {}
if environ.get('IS_TESTING') is None:
    connect_args = {
        'sslmode': 'require', 'sslrootcert': 'BaltimoreCyberTrustRoot.crt.pem'
    }

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_test_db(schema="test"):
    Base.metadata.schema = schema
    Base.metadata.create_all(bind=engine)


def drop_test_db(schema="test"):
    Base.metadata.schema = schema
    Base.metadata.drop_all(bind=engine)


def recreate_test_db():
    drop_test_db()
    init_test_db()


def get_test_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
