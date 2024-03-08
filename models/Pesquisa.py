from app import db

class Pesquisa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente', backref=db.backref('pesquisas', lazy=True))
    nome_estado = db.Column(db.String(255), nullable=False)
    nome_cidade = db.Column(db.String(255), nullable=False)
    populacao = db.Column(db.Integer, nullable=False)
    eleitorado = db.Column(db.Integer, nullable=False)
    margem_erro = db.Column(db.Integer, nullable=False)
    confianca = db.Column(db.Integer, nullable=False)
    tipo_pesquisa = db.Column(db.String(255), nullable=False)
    qnt_perg = db.Column(db.Integer, nullable=False)
    qnt_urbanas = db.Column(db.Integer, nullable=False)
    qnt_rurais = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'<Pesquisa {self.id}>'