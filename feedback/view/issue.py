from flask import g, Flask, render_template, request, flash, redirect, url_for
from feedback.feedback import app
from feedback.model.issue import Issue
from feedback.form.issue import CreateIssueForm
from feedback.feedback import db
from flaskext.login import current_user, login_required

# TODO: Catch database errors

@app.route('/issue/create', methods=['GET', 'POST'])
@login_required
def create_issue():
    return edit_issue(0)

@app.route('/issue/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_issue(id):
    form = CreateIssueForm(request.form)
    if request.method == 'POST' and form.validate():
        print "id: '%s'" % form.id.data
        print form
        if form.id.data:
            issue = Issue.query.filter_by(id=int(form.id.data)).first()
            issue.title = form.title.data
            issue.description = form.description.data
            issue.tickets = form.tickets.data
            flash("issue saved")
        else:
            issue = Issue()
            issue.description = form.description.data
            issue.tickets = form.tickets.data
            issue.user_id = current_user.id
            issue.title = form.title.data
            db.session.add(issue)
            flash("issue created")

        db.session.commit()

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
        return render_template("issue/main", form=form, title="edit issue", action="edit")

    return render_template("issue/main", form=form, title="create issue", action="create")

@app.route('/issue/<int:id>')
def view_issue(id):
    issue = Issue.query.filter_by(id=int(id)).first()
    if not issue:
        flash("there is no issue %d" % id)
        return redirect(url_for('index'))
    return render_template("issue/main", issue=issue, title="issue %s" % issue.title, action="view")

@app.route('/issue/<int:id>/delete', methods=['GET', 'POST'])
@login_required
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

    return render_template("issue/delete", title="delete issue", issue=issue)
