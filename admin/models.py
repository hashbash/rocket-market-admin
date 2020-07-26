from admin import db
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func


class Tickers(db.Model):
    __tablename__ = 'tickers'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    isin = Column(String, unique=True)
    yf_code = Column(String)
    exchange = Column(String)
    source = Column(String, nullable=False)
    fetch_from_yahoo_finance = Column(Boolean)
    created = Column(DateTime, server_default=func.now())
    updated = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<Ticker(id='%s', code='%s', yf_code='%s' isin='%s')>" % (self.id, self.code, self.yf_code, self.isin)
