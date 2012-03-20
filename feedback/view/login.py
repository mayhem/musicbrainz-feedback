import urllib2
from flask import g, Flask, render_template, request, flash, redirect, url_for
from flaskext.login import login_user, logout_user, login_required, current_user
from feedback.feedback import app
from feedback.model.user import User
from feedback.form.login import LoginForm
from feedback.feedback import db

PASSWORD_CHECK_TIMEOUT=15

@app.login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(username=userid).first()

# Stolen from acoustid login
class DigestAuthHandler(urllib2.HTTPDigestAuthHandler):
    """Patched DigestAuthHandler to correctly handle Digest Auth according to RFC 2617.

    This will allow multiple qop values in the WWW-Authenticate header (e.g. "auth,auth-int").
    The only supported qop value is still auth, though.
    See http://bugs.python.org/issue9714

    @author Kuno Woudt
    """
    def get_authorization(self, req, chal):
        qop = chal.get('qop')
        if qop and ',' in qop and 'auth' in qop.split(','):
            chal['qop'] = 'auth'
        return urllib2.HTTPDigestAuthHandler.get_authorization(self, req, chal)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():

        url = 'http://musicbrainz.org/ws/2/release/76df3287-6cda-33eb-8e9a-044b5e15ffdd?inc=user-tags'
        auth = DigestAuthHandler()
        auth.add_password('musicbrainz.org', 'http://musicbrainz.org/', form.username.data, form.password.data)
        opener = urllib2.build_opener(auth)
        opener.addheaders = [('User-Agent', 'MusicBrainz-Feedback +https://github.com/mayhem/musicbrainz-feedback')]

        try:
            opener.open(url, timeout=PASSWORD_CHECK_TIMEOUT)
        except urllib2.HTTPError, err:
            flash("Login incorrect")
            return redirect(url_for('login'))
        except StandardError, err:
            flash("Sorry we could not verify your login on musicbrainz.org. Please try again in a few minutes.")
            return redirect(url_for('login'))

        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(form.username.data)
            db.session.add(user)
            db.session.commit()

        login_user(user) # TODO remember=True
        flash("You're logged in!")
        return redirect(url_for('index'))
    return render_template("login", form=form, title="login")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
