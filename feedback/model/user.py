# -*- coding: utf-8 -*-
from flaskext.sqlalchemy import SQLAlchemy
from feedback.feedback import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return self.username != ""

    def is_active(self):
        return True

    def is_anonymous(self):
        return self.username == ""

    def get_id(self):
        return self.username

    def __repr__(self):
        return '<User %d>' % self.username
