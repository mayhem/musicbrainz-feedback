# -*- coding: utf-8 -*-
from flaskext.sqlalchemy import SQLAlchemy
from feedback.feedback import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<User %d>' % self.id
