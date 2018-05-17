# -*- coding: UTF-8 -*-

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(64))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return {'id':self.id, 'username':self.username, 'email':self.email, 'password':self.password}


class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    date = db.Column(db.DateTime, index=True)
    # date = db.Column(db.String(64), index=True)
    place = db.Column(db.String(64), index=True)
    introduction = db.relationship('Introduction', backref='conference',  lazy='dynamic')

    def __repr__(self):
        return '<Conference %r>' & self.name

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'date': self.date, 'place': self.place,
                'introduction': self.introduction}


#会议简介
class Introduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128))
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))

    def __repr__(self):
        return '<Introduction %r>' & self.id

    def to_dict(self):
        return {'id': self.id, 'url': self.url}