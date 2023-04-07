# import all the necessary library

from app.citybike import main
from app.citybike.models import Citybike
from app import db
from flask import render_template, request, flash, redirect, url_for



# company list display
@main.route('/journey')

def display_todo_name():
    
    citybike_list = Citybike.query.all()
    return render_template('citibyike_list.html', citybike_list=citybike_list)

# home page display


@main.route('/')

def display_dashboard():
    return render_template('home.html')

# route error handling

@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404