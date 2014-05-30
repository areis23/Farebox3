from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite://', echo=True)

from sqlalchemy import Column, Integer, Float, String

class Data(Base):
	__tablename__ = 'data'

	id = Column(Integer, primary_key=True)
	LINE_NUMBER = Column(Integer)
	ZONE_NUMBER = Column(Integer)
	TIME_RANGE = Column(String)
	DIRECTION = Column(String)
	TOTAL_OPERATING_COST = Column(Float)
	FARE_COLLECTED = Column(Float)
	FAREBOX_RECOVERY = Column(Integer)
	SIGN_ON_DATE = Column(String)
	COUNTY = Column(String)
	TYPE = Column(String)

	def __init__(self, LINE_NUMBER, ZONE_NUMBER, TIME_RANGE, DIRECTION, TOTAL_OPERATING_COST, FARE_COLLECTED, FAREBOX_RECOVERY, SIGN_ON_DATE, COUNTY, TYPE):
		self.LINE_NUMBER = LINE_NUMBER
		self.ZONE_NUMBER = ZONE_NUMBER
		self.TIME_RANGE = TIME_RANGE
		self.DIRECTION = DIRECTION
		self.TOTAL_OPERATING_COST = TOTAL_OPERATING_COST
		self.FARE_COLLECTED = FARE_COLLECTED
		self.FAREBOX_RECOVERY = FAREBOX_RECOVERY
		self.SIGN_ON_DATE = SIGN_ON_DATE
		self.COUNTY = COUNTY
		self.TYPE = TYPE

	def __repr__(self):
		return "<Data('%d','%d', '%s')>" % (self.LINE_NUMBER, self.ZONE_NUMBER, self.TIME_RANGE)

