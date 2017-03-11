from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField, SubmitField, RadioField
from wtforms.validators import InputRequired, NumberRange

class LoginForm(FlaskForm):
    f_name = StringField('First Name', validators=[InputRequired()])
    l_name = StringField('Last Name', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired(),NumberRange(min=13,max=110)])
    gender = RadioField('Gender',choices = [('male','Male'),('female','Female')])
    image = FileField('User Image', validators=[FileRequired(),FileAllowed(['png','jpg'],'Images only ')])
    bio = StringField('Biography', validators=[InputRequired()])
    submit= SubmitField("Submit")
    
