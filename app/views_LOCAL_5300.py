# -*- coding: UTF-8 -*-

from flask import render_template
from app import app
from app.forms import AddConferenceForm
from app.models import *


@app.route('/index')
def index():
    user = { 'username': 'HHX'} # fake user
    tag = {'name': 'index'}
    return render_template("index.html", user=user, tag=tag)


@app.route('/add_conference', methods = ['GET', 'POST'])
def add_conference():
    form = AddConferenceForm()
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

@app.route('/previewlist')
def previewlist():
    user = {'username': 'HHX'}
    tag = {'name': 'previewlist'}
    meetings = [{'name': 'xxx', '':''},
                {}]# 列表，键值对，每个大括号是一个条目，调用的时候直接写meetings.键
    return render_template('previewlist.html', user=user, tag=tag)

@app.route('/preview')
def preview():
    user = {'username': 'HHX'}
    tag = {'name': 'preview'}
    meeting = {
        '':'',


    }
    return render_template('preview.html', user=user, tag=tag, )
