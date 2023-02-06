from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

class PredictForm(FlaskForm):
    input_file = FileField('input_file',validators=[DataRequired(),FileAllowed(['csv'])])
    cluster_model = SelectField('cluster_model',validators=[DataRequired()],choices=['K-means','Gaussian Mixtures'])
    submit = SubmitField('Submit')