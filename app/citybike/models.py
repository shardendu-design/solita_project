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

    # Define a property that returns the duration in minutes
    @property 
    def duration_in_minutes(self):
        return '{:.2f}'.format(self.duration_sec / 60)
    
    @property
    def covered_distance_km(self):
        kilometers = self.covered_distance_m / 1000
        return '{:.2f}'.format(kilometers)
    
    @staticmethod
    def get_departure_count(station_id):
        return Citybike.query.filter_by(departure_station_id=station_id).count()
    
    
    
    @staticmethod
    def get_return_count(station_id):
        return Citybike.query.filter_by(return_station_id=station_id).count()