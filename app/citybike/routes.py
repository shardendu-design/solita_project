# import all the necessary library

from app.citybike import main
from app.citybike.models import Citybike
from app import db
from flask import render_template, request, flash, redirect, url_for
from flask_sqlalchemy import pagination 



# company list display
@main.route('/')

def display_citybike_details():
    page = request.args.get('page', 1, type=int)
    citybike_list = Citybike.query.paginate(page=page, per_page=10)
    
    return render_template('citibyike_list.html', citybike_list=citybike_list)

@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404