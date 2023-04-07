# import all necessary library

from app import db
from datetime import date, datetime

# create cotybike databse model

class Citybike(db.Model):
    __tablename__ = 'citybiketable'

    departure = db.Column(db.Text)
    returns = db.Column(db.Text)
    departure_station_id = db.Column(db.Bigint)
    departure_dtation_name = db.Column(db.Text)
    return_station_id = db.Column(db.Bigint)
    return_station_name = db.Colum(db.Text)
    covered_distance_m = db.Column(db.Double)
    duration_sec = db.Column(db.Bigint)
