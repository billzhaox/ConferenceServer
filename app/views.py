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
    meetings = [
        {
            '会议名称': 'html加冕礼',
            '会议地点': '行政办公楼三楼会议室',
            '会议开始时间': '2018-5-16 15:30:00',
            '会议时长': '3小时',
            '会议状态': '待发布',
            '会议嘉宾': '姜局，平行宇宙守护者，银河系元老级法师，凹凸曼带盐人，塞博坦星大祭司',
            '详细内容': 'preview'
        },
        {
            '会议名称': 'html加冕礼',
            '会议地点': '行政办公楼三楼会议室',
            '会议开始时间': '2018-5-16 15:30:00',
            '会议时长': '3小时',
            '会议状态': '待发布',
            '会议嘉宾': '姜局，平行宇宙守护者，银河系元老级法师，凹凸曼带盐人，塞博坦星大祭司',
            '详细内容': 'preview'
        }, {
            '会议名称': 'html加冕礼',
            '会议地点': '行政办公楼三楼会议室',
            '会议开始时间': '2018-5-16 15:30:00',
            '会议时长': '3小时',
            '会议状态': '待发布',
            '会议嘉宾': '姜局，平行宇宙守护者，银河系元老级法师，凹凸曼带盐人，塞博坦星大祭司',
            '详细内容': 'preview'
        }
    ]
    return render_template('previewlist.html', user=user, tag=tag, meetings=meetings)


@app.route('/preview')
def preview():
    user = {'username': 'HHX'}
    tag = {'name': 'preview'}
    meeting = {
        '会议名称': '我是名称!',
        '会议简介': '海外网5月15日电韩联社15日称，韩国统一部表示，朝鲜共邀请韩国8名记者参观'
                '丰溪里核试验场废弃仪式，包括4名通信社记者和4名电视台记者。他们将在朝鲜驻华'
                '使馆获得签证后，22日从北京乘坐专机，与其他外国记者一道前往朝鲜元山葛麻机场，'
                '并使用元山的宿舍和记者中心。其后，记者们将乘坐列车前往核试验场，结束摄影后再'
                '返回元山记者中心。预计26日或27日从元山葛麻机场乘专机返回。记者的差旅费、通信'
                '费等所有费用自行负担。',
        '会议地点': '行政办公楼三楼会议室',
        '会议时间': '2018-5-16 15:30:00',
        '会议时长': '3小时',
        '会议状态': '待发布',
        '嘉宾介绍': '姜局，平行宇宙守护者，银河系元老级法师，凹凸曼带盐人，塞博坦星大祭司',
        '参加人员': ['hhx', 'dsz', '...'],
        '备注信息': '我是备注'
    }
    return render_template('preview.html', user=user, tag=tag, meeting=meeting)


@app.route('/login')
def login():
    return render_template('login.html');