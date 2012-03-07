from flask import g, Flask, render_template, request, flash, redirect, url_for
from feedback.feedback import app
from feedback.model.issue import Issue
from feedback.form.issue import CreateIssueForm

@app.route('/issue/create', methods=['GET', 'POST'])
def create_issue():
    form = CreateIssueForm(request.form)
    if request.method == 'POST' and form.validate():
        flash("Issue created.")
        return redirect(url_for('create_issue'))
    return render_template("issue/create", form=form, title="Feedback: Create issue")
