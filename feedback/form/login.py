from wtforms import Form, BooleanField, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=2, max=25)])
    password = PasswordField('New Password', [validators.Required()])
