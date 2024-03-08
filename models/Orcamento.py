from app import db

class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pesquisa_id = db.Column(db.Integer, db.ForeignKey('pesquisa.id'), nullable=False)
    cliente = db.relationship('Cliente', backref=db.backref('orcamentos', lazy=True))
    ambpg = db.Column(db.Float, nullable=False)
    ambeg = db.Column(db.Float, nullable=False)
    ambps = db.Column(db.Float, nullable=False)
    ambes = db.Column(db.Float, nullable=False)
    vp_bps = db.Column(db.Float, nullable=False)
    vp_bes = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Orcamento {self.id}>'