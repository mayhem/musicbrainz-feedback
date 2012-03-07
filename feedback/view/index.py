from flask import Flask, render_template, g
from feedback.feedback import app
from flaskext.login import current_user
from feedback.model.issue import Issue

@app.route('/')
def index():
    issues = Issue.query.filter_by(is_open=True).order_by(Issue.created)
    return render_template("index", title="Welcome to MusicBrainz Feedback!", issues=issues)
