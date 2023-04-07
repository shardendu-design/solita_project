# import all necessary library

from app import db
from datetime import date, datetime

# create cotybike databse model

class Citybike(db.Model):
    __tablename__ = 'citybiketable'

   
    departure = db.Column(db.Text,primary_key=True)
    returns = db.Column(db.Text)
    departure_station_id = db.Column(db.Integer)
    departure_station_name = db.Column(db.Text)
    return_station_id = db.Column(db.Integer)
    return_station_name = db.Column(db.Text)
    covered_distance_m = db.Column(db.Float)
    duration_sec = db.Column(db.Integer)
