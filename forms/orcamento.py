from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class PesquisaForm(FlaskForm):
    nome_estado = StringField('Qual é o nome do estado em que a pesquisa será realizada?', validators=[DataRequired()])
    nome_cidade = StringField('Qual é o nome da cidade em que a pesquisa será realizada?', validators=[DataRequired()])
    populacao = IntegerField('Qual é a população total da cidade?', validators=[DataRequired(), NumberRange(min=0)])
    eleitorado = IntegerField('Qual é o eleitorado total da cidade?', validators=[DataRequired(), NumberRange(min=0)])
    margem_erro = SelectField('Selecione a margem de erro:', choices=[('1', '1%'), ('2', '2%'), ('3', '3%'), ('4', '4%'), ('5', '5%')], validators=[DataRequired()])
    confianca = SelectField('Selecione o nível de confiança:', choices=[('90', '90%'), ('95', '95%'), ('99', '99%')], validators=[DataRequired()])
    tipo_pesquisa = SelectField('Selecione o tipo de pesquisa:', choices=[('setorial', 'Setorial'), ('generalista', 'Generalista')], validators=[DataRequired()])
    qnt_perg = IntegerField('Qual a quantidade de perguntas você deseja realizar?', validators=[DataRequired(), NumberRange(min=0)])
    qnt_urbanas = IntegerField('Qual a quantidade de localidades urbanas?', validators=[DataRequired(), NumberRange(min=0)])
    qnt_rurais = IntegerField('Qual a quantidade de localidades rurais?', validators=[DataRequired(), NumberRange(min=0)])