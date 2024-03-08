from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange

class ClienteForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    email = EmailField('Endereço de Email', validators=[DataRequired(), Email()])
    telefone = IntegerField('Número de Telefone', validators=[DataRequired()])