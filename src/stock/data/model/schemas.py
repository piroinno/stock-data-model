from typing import Optional
from pydantic import BaseModel
import datetime

class ExchangeSchema(BaseModel):
    name: str
    acronym: str
    country: str
    mic: str

class ExchangeCreate(ExchangeSchema):
    country_id: int
    city_id: int
    timezone_id: int

class Exchange(BaseModel):
    id: int
    name: str
    time_generated: datetime.datetime
    acronym: str
    country: str
    mic: str
    country_id: int
    city_id: int
    timezone_id: int
    
    class Config:
        orm_mode = True

class TimezoneSchema(BaseModel):
    name: str
    abbr: str
    dst: str

class TimezoneCreate(TimezoneSchema):
    pass

class Timezone(TimezoneSchema):
    id: int
    name: str
    time_generated: datetime.datetime
    abbr: str
    dst: str
    
    class Config:
        orm_mode = True

class Country(BaseModel):
    id: int
    name: str
    time_generated: datetime.datetime
    code: str
    
    class Config:
        orm_mode = True

class City(BaseModel):
    id: int
    name: str
    time_generated: datetime.datetime
    country_id: int
    
    class Config:
        orm_mode = True

class Currency(BaseModel):
    id: int
    name: str
    time_generated: datetime.datetime
    code: str
    
    class Config:
        orm_mode = True
        
class Ticker(BaseModel):
    id: int
    name: str
    time_generated: datetime.datetime
    exchange_id: int
    ticker: str
    currency_id: int
    
    class Config:
        orm_mode = True

class CurrencySchema(BaseModel):
    name: str
    code: str

class CurrencyCreate(CurrencySchema):
    pass

class Currency(CurrencySchema):
    id: int
    name: str
    time_generated: datetime.datetime
    code: str
    
    class Config:
        orm_mode = True

class EodIngestorDataStore(BaseModel):
    id: int
    name: str
    time_generated: datetime.datetime
    url: Optional[str] = None
    subscription_id: str
    container: str
    tenant_id: Optional[str] = None
    
    class Config:
        orm_mode = True

class EodIngestorJobStatusSchema(BaseModel):
    name: str
    status: str
    message: Optional[str] = None
    data_store_id: int
    ticker_id: int
    start_date: datetime.date
    end_date: datetime.date
    timezone_id: int

class EodIngestorJobStatusCreate(EodIngestorJobStatusSchema):
    pass
    
class EodIngestorJobStatus(EodIngestorJobStatusSchema):
    id: int
    time_generated: datetime.datetime
    
    class Config:
        orm_mode = True

class EodIngestorJobDataLocationSchema(BaseModel):
    name: str
    data_store_id: int
    ticker_id: int
    job_status_id: int
    blob: str

class EodIngestorJobDataLocationCreate(EodIngestorJobDataLocationSchema):
    pass

class EodIngestorJobDataLocation(EodIngestorJobDataLocationSchema):
    id: int
    time_generated: datetime.datetime
    
    class Config:
        orm_mode = True