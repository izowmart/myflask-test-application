from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(max=140)])
