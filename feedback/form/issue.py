from wtforms import Form, TextField, TextAreaField, validators, HiddenField

class CreateIssueForm(Form):
    id = HiddenField(u"id", default=0)
    title = TextField('Title', [validators.Length(min=0, max=128)])
    description = TextAreaField('Description', [validators.Length(min=0, max=16384)])
    tickets = TextField('Related tickets', [validators.Length(min=0, max=1024)])
