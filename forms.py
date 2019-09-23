from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.html5 import DateTimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange
import datetime

class SetupForm(FlaskForm):
    eventName = StringField('Event Name', validators=[DataRequired()])
    startDateTime = DateTimeField('Start Date/Time',  format='%Y-%m-%d %H:%M', default=datetime.datetime.now(), validators=[DataRequired()])
    duration = IntegerField('Length (minutes)', default=60,validators=[NumberRange(min=30, max=300)])
    slotTime = IntegerField('Time per practice slot', default=10, validators=[NumberRange(min=5,max=60)])
    numFields = IntegerField('Number Fields', default=1, validators=[NumberRange(min=1)])
    numPerSide = IntegerField('Teams per side', default=2, validators=[NumberRange(min=1, max=3)])
    twoSides = BooleanField('Two Sides',default=True)
   
    submit = SubmitField('Create Event')