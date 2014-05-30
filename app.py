from declarativeBase import Base
from declarativeBase import Data
from declarativeBase import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import csv
from flask import Flask, render_template, request

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

with open('data.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	for row in fb_reader:
		session.add(Data(row['LINE_NUMBER'], row['ZONE_NUMBER'], \
			row['TIME_RANGE'], row['DIRECTION'], \
			row['TOTAL_OPERATING_COST'], row['FARE_COLLECTED'], \
			row['FAREBOX_RECOVERY'], \
			row['SIGN_ON_DATE'], \
			row['COUNTY'], row['TYPE']))

session.commit()

app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')
	

@app.route('/chart', methods=['POST'])
def chart():
	line = int(request.form['line'])
	for instance in session.query(func.sum(Data.FARE_COLLECTED)).filter_by(LINE_NUMBER = line):
		line_sum = instance[0]
	return render_template('chart.html', line= line, line_sum=line_sum)

`