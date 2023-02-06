from flask_wtf import FlaskForm
from wtforms import SubmitField,SelectField
from wtforms.validators import DataRequired


class AssociationForm(FlaskForm):
    product =SelectField('product', validators=[DataRequired()],choices=['Wines','Fruits','Sweets','Gold','Meat','Fish'])
    segment =SelectField('segment', validators=[DataRequired()],choices=['Frequent Buyer','Normal Buyer','Low Buyer'])
    submit = SubmitField('Submit')