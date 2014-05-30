from declarativeBase import Base
from declarativeBase import Data
from declarativeBase import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import csv

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

"""
ed_user = User('ed', 'Ed Jones', 'edspassword')
session.add(ed_user)
session.add_all([
	User('wendy', 'Wendy Williams', 'foobar'),
	User('mary', 'Mary Contrary', 'xxg527'),
	User('fred', 'Fred Flinstone', 'blah')])
ed_user.password = 'f8s7ccs'
our_user = session.query(User).filter_by(name = 'ed').first()
"""
with open('data.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	for row in fb_reader:
		session.add(Data(row['LINE_NUMBER'], row['ZONE_NUMBER'], \
			row['TIME_RANGE'], row['DIRECTION'], \
			row['TOTAL_OPERATING_COST'], row['FARE_COLLECTED'], \
			row['FAREBOX_RECOVERY'], \
			row['SIGN_ON_DATE'], \
			row['COUNTY'], row['TYPE']))


#print our_user
#session.new
session.commit()
for instance in session.query(func.sum(Data.FARE_COLLECTED)).filter_by(LINE_NUMBER = 1):
	line_sum = instance[0]
print line_sum

