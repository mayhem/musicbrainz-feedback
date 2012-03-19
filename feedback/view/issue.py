from flask import g, Flask, render_template, request, flash, redirect, url_for
from feedback.feedback import app
from feedback.model.issue import Issue
from feedback.form.issue import CreateIssueForm
from feedback.feedback import db
from flaskext.login import current_user

# TODO: Catch database errors

@app.route('/issue/create', methods=['GET', 'POST'])
def create_issue():
    return edit_issue(0)

@app.route('/issue/<int:id>/edit', methods=['GET', 'POST'])
def edit_issue(id):
    form = CreateIssueForm(request.form)
    if request.method == 'POST' and form.validate():
        id = int(form.id.data)
        if id:
            issue = Issue.query.filter_by(id=id).first()
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

        flash("issue saved")
        return redirect(url_for('index'))

    if id:
        issue = Issue.query.filter_by(id=int(id)).first()
        if not issue:
            flash("there is no issue %d" % id)
            return redirect(url_for('index'))
        form.id.data = issue.id
        form.description.data = issue.description
        form.tickets.data = issue.tickets
        form.user_id.data = issue.user_id
        form.title.data = issue.title
        form.expires.data = issue.expires()
        return render_template("issue/main", form=form, title="Feedback: Edit issue", action="edit")

    return render_template("issue/main", form=form, title="Feedback: Create issue", action="edit")

@app.route('/issue/<int:id>')
def view_issue(id):
    issue = Issue.query.filter_by(id=int(id)).first()
    if not issue:
        flash("there is no issue %d" % id)
        return redirect(url_for('index'))
    return render_template("issue/main", issue=issue, title="Feedback: issue %s" % issue.title, action="view")

@app.route('/issue/<int:id>/delete', methods=['GET', 'POST'])
def delete_issue(id):
    issue = Issue.query.filter_by(id=id).first()
    if not issue:
        flash("there is no issue %d" % id)
        return redirect(url_for('index'))
    if request.method == 'POST':
        db.session.delete(issue)
        db.session.commit()
        flash("issue %d deleted" % id)
        return redirect(url_for('index'))

    return render_template("issue/delete", title="Feedback: Delete issue", issue=issue)
