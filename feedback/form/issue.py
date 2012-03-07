from wtforms import Form, TextField, TextAreaField, validators

class CreateIssueForm(Form):
    description = TextAreaField('Description', [validators.Length(min=32, max=16384)])
    tickets = TextField('Related tickets', [validators.Length(min=0, max=1024)])
