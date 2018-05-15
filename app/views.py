# -*- coding: UTF-8 -*-

from flask import render_template
from app import app
from app.forms import AddConferenceForm
from app.models import *


@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'HHX'} # fake user
    tag = {'name': 'index'}
    return render_template("index.html", user=user, tag=tag)


@app.route('/add_conference', methods = ['GET', 'POST'])
def add_conference():
    form = AddConferenceForm()
    user = {'username': 'HHX'}
    tag = {'name': 'add_conference'}
    if form.validate_on_submit():
        name = form.name.data
        date = form.date.data
        place = form.place.data
        conference = Conference(name=name, date=date, place=place)
        db.session.add(conference)
        db.session.commit()
    return render_template('add_conference.html', user=user, form=form, tag=tag)
