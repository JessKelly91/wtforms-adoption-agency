from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

species = ["Cat", "Dog", "Porcupine"]

class PetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])

    species = SelectField("Species", choices=[(species, species) for species in species], validators=[InputRequired()])

    photo_url = URLField("Photo Link", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField("Notes", validators=[Optional()])