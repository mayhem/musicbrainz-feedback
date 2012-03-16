# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from flaskext.sqlalchemy import SQLAlchemy
from feedback.feedback import db
from feedback.misc.utc import UTC
from feedback.model import user

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    tickets = db.Column(db.Text)
    is_open = db.Column(db.Boolean)
    created = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('Issue', lazy='dynamic'))

    def __init__(self):
        self.is_open = True
        self.created = datetime.utcnow()

    def expires(self):
        expires = self.created + timedelta(14)
        return expires.strftime("%Y-%m-%d %H:%M utc")

    def __repr__(self):
        return '<Issue %d>' % self.id

