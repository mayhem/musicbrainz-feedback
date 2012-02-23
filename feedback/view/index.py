from flask import Flask, render_template
from feedback.feedback import app

@app.route('/')
def hello_world():
    return render_template("index", title="Welcome to MusicBrainz Feedback!")
