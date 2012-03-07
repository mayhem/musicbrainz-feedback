from flask import Flask, render_template, g
from feedback.feedback import app
from flaskext.login import current_user

@app.route('/')
def hello_world():
    return render_template("index", title="Welcome to MusicBrainz Feedback!")
