# import all the necessary library

from app.citybike import main
from app.citybike.models import Citybike
from app import db
from flask import render_template, request, flash, redirect, url_for
from flask_sqlalchemy import pagination 
from flask_paginate import Pagination, get_page_args



# company list display
@main.route('/')

def display_citybike_details():
    page = request.args.get('page', 1, type=int)
    citybike_list = Citybike.query.paginate(page=page, per_page=10)
    
    return render_template('citibyike_list.html', citybike_list=citybike_list)

@main.route('/stationlist')
def display_station_list():
    page = request.args.get('page', 1, type=int)
    station_list = Citybike.query.paginate(page=page, per_page=10)
    return render_template('list_all_station.html', station_list=station_list)

@main.route('/singlelstationview')
def display_single_station_view():
    page = request.args.get('page', 1, type=int)
    single_station_view = Citybike.query.paginate(page=page, per_page=10)
    stations = set([(trip.departure_station_id, trip.departure_station_name) for trip in single_station_view.items] + [(trip.return_station_id, trip.return_station_name) for trip in single_station_view.items])
    station_counts = {}
    for station_id, station_name in stations:
        station_counts[station_id] = {
            'departure_count': Citybike.get_departure_count(station_id),
            'return_count': Citybike.get_return_count(station_id)
        }
    return render_template('single_station_view.html', single_station_view=single_station_view, station_counts=station_counts)

@main.route('/departuresearch')
def departure_search():
    page = request.args.get('page', 1, type=int)
    station_id = request.args.get('station_id',type=int)
    if station_id:
        single_station_wise = Citybike.query.filter_by(departure_station_id=station_id).paginate(page=page, per_page=10)
    else:
        single_station_wise = Citybike.query.paginate(page=page, per_page=10)

    return render_template('search_departure_wise.html', single_station_wise=single_station_wise)

@main.route('/returnsearch')
def return_search():
    page = request.args.get('page', 1, type=int)
    station_id = request.args.get('station_id',type=int)
    if station_id:
        single_station_idwise = Citybike.query.filter_by(return_station_id=station_id).paginate(page=page, per_page=10)
    else:
        single_station_idwise = Citybike.query.paginate(page=page, per_page=10)

    return render_template('search_return_wise.html', single_station_idwise=single_station_idwise)



    
@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404