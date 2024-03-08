from app import app
from flask import render_template, redirect, url_for
from forms.orcamento import *
from forms.cliente import *


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form")
def form():
    form = ClienteForm()
    return render_template("form.html", form=form)

@app.route("/formestatistica")
def formestatistica():
    form = PesquisaForm()
    return render_template("formestatistica.html", form=form)


@app.route("/estatisticas")
def estatisticas():
    # Adicione a lógica de login conforme necessário
    return render_template("estatisticas.html")