# -*- coding: utf-8 -*-
from flaskext.sqlalchemy import SQLAlchemy
from feedback.feedback import db
from feedback.model import user

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    tickets = db.Column(db.Text)
    is_open = db.Column(db.Boolean)
    created = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('Issue', lazy='dynamic'))

    def __init__(self, id, user, description, tickets, is_open, created):
        self.id = id
        self.user = user
        self.description = description
        self.tickets = tickets
        self.is_open = is_open
        self.created = created

    def __repr__(self):
        return '<Issue %d>' % self.id

