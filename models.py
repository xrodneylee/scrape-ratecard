from sqlalchemy import Column, Integer, String, DateTime, Float
from database import Base

class AzureRateCard(Base):
    __tablename__ = 'azure-ratecard'
    id = Column(Integer, primary_key=True)
    MeterId = Column(String(120), unique=True)
    MeterRates = Column(String(120))

    def __init__(self, MeterId=None, MeterRates=None):
        self.MeterId = MeterId
        self.MeterRates =MeterRates

    def __repr__(self):
        return '<azure-ratecard %r>' % (self.MeterRates)

class AzureUsage(Base):
    __tablename__ = 'azure-usage'
    id = Column(Integer, primary_key=True)
    ResourceGroups = Column(String)
    Providers = Column(String)
    Name = Column(String)
    SubscriptionId = Column(String)
    UsageStartTime = Column(DateTime)
    UsageEndTime = Column(DateTime)
    MeterName = Column(String)
    MeterCategory = Column(String)
    MeterId =  Column(String)
    Quantity = Column(Float)

    def __init__(self, ResourceGroups=None,
            Providers=None,
            Name=None,
            SubscriptionId=None,
            UsageStartTime=None,
            UsageEndTime=None,
            MeterName=None,
            MeterCategory=None,
            MeterId=None,
            Quantity=None):
        self.ResourceGroups = ResourceGroups
        self.Providers = Providers
        self.Name = Name
        self.SubscriptionId = SubscriptionId
        self.UsageStartTime = UsageStartTime
        self.UsageEndTime = UsageEndTime
        self.MeterName = MeterName
        self.MeterCategory = MeterCategory
        self.MeterId = MeterId
        self.Quantity = Quantity

    def __repr__(self):
        return '<azure-usage %r>' % (self.SubscriptionId)