from flask import g, Flask, render_template, request, flash, redirect, url_for
from flaskext.login import login_user, logout_user, login_required, current_user
from feedback.feedback import app
from feedback.model.user import User
from feedback.form.login import LoginForm

@app.login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(username=userid).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # check password here!
        user = User(3, "rob") #form.username.data)
        login_user(user) # TODO remember=True
        flash("You're logged in!")
        return redirect("/") #url_for('index'))
    return render_template("login", form=form, title="Feedback: Login")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
