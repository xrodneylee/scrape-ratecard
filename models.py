from sqlalchemy import Column, Integer, String
from database import Base

class AzureRateCard(Base):
    __tablename__ = 'azure-ratecard'
    id = Column(Integer, primary_key=True)
    MeterId = Column(String(120), unique=True)
    Unit = Column(String(50), unique=False)

    def __init__(self, MeterId=None, Unit=None):
        self.MeterId = MeterId
        self.Unit = Unit

    def __repr__(self):
        return '<azure-ratecard %r>' % (self.Unit)