from app import app
from flask import render_template, redirect, url_for,  request, session, jsonify

@app.route('/orcamento')
def orcamento():
    return 0