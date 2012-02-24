from flask import Flask, render_template
from feedback.feedback import app

@app.route('/feedback')
def feedback():
    return render_template("feedback", title="Feedback: Give feedback")
