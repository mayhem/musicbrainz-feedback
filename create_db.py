#!/usr/bin/env python

from feedback.feedback import db
from feedback.model import issue
from feedback.model import user

db.create_all()
