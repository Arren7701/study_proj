from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    query = StringField("query",validators=[
        DataRequired(message = "用户提问时必须的"),
        Length(max=2000,message = "最大长度不能超过2000字")
    ])


