from flask import Flask, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy 
from flask_sslify import SSLify

app = Flask(__name__)
app.secret_key = "relampagomarquinhos"
app.config.from_pyfile('config.py')
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
ssl = SSLify(app)

from controllers.home import *
from controllers.formularios import *

if __name__ == "__main__":
    app.run(debug=True)
