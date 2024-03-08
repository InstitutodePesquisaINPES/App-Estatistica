from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    telefone = db.Column(db.String(14))

    def __repr__(self):
        return f'<Cliente {self.nome}>'