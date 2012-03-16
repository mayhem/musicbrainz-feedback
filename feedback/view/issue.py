from flask import g, Flask, render_template, request, flash, redirect, url_for
from feedback.feedback import app
from feedback.model.issue import Issue
from feedback.form.issue import CreateIssueForm
from feedback.feedback import db
from flaskext.login import current_user

@app.route('/issue/create', methods=['GET', 'POST'])
def create_issue():
    form = CreateIssueForm(request.form)
    if request.method == 'POST' and form.validate():
        id = int(request.form.get("id") or '0')
        if id:
            issue = Issue.query.filter_by(id=int(id)).first()
            issue.title = form.title.data
            issue.description = form.description.data
            issue.tickets = form.tickets.data
        else:
            issue = Issue()
            issue.description = form.description.data
            issue.tickets = form.tickets.data
            issue.user_id = current_user.id
            issue.title = form.title.data
            db.session.add(issue)

        db.session.commit()

        flash("Issue created.")
        return redirect(url_for('create_issue'))
    return render_template("issue/create", form=form, title="Feedback: Create issue")

@app.route('/issue/<int:id>')
def view_issue(id):
    issue = Issue.query.filter_by(id=int(id)).first()
    return render_template("issue/view", issue=issue, title="Feedback: issue %s" % issue.title)
