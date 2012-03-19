from wtforms import Form, TextField, TextAreaField, validators, HiddenField

class CreateIssueForm(Form):
    id = HiddenField(u"id", default=0)
    user_id = HiddenField(u"user_id", default=0)
    title = TextField('title', [validators.Length(min=0, max=128)])
    description = TextAreaField('description', [validators.Length(min=0, max=16384)])
    tickets = TextField('related tickets', [validators.Length(min=0, max=1024)])
    expires = TextField('expires')
