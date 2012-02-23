# -*- coding: utf-8 -*-
from flaskext.sqlalchemy import SQLAlchemy
from feedback.feedback import db

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    tickets = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('issue', lazy='dynamic'))

    def __init__(self, description, tickets):
        self.description = description
        self.tickets = tickets

    def __repr__(self):
        return '<Issue %d>' % self.id
