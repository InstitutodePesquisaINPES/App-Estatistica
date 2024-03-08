# app.py
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "relampagomarquinhos"

from controllers.home import *
from controllers.formularios import *

if __name__ == "__main__":
    app.run(debug=True)
