from flask import Flask, render_template
from feedback.feedback import app

@app.route('/rank')
def rank():
    return render_template("rank", title="Feedback: Rank")
