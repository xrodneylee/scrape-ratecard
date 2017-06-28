from sqlalchemy import Column, Integer, String
from database import Base

class AzureRateCard(Base):
    __tablename__ = 'azure-ratecard'
    id = Column(Integer, primary_key=True)
    MeterId = Column(String(120), unique=True)
    MeterRates = Column(String(120), unique=False)

    def __init__(self, MeterId=None, MeterRates=None):
        self.MeterId = MeterId
        self.MeterRates =MeterRates

    def __repr__(self):
        return '<azure-ratecard %r>' % (self.MeterRates)

class AzureUsage(Base):
    __tablename__ = 'azure-usage'
    id = Column(Integer, primary_key=True)
    subscriptionId = Column(String(120), unique=False)

    def __init__(self, subscriptionId=None):
        self.subscriptionId = subscriptionId

    def __repr__(self):
        return '<azure-usage %r>' % (self.subscriptionId)