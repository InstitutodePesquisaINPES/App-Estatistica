from app import app
from app import db
from flask import render_template, redirect, url_for,  request, session, jsonify
from forms.cliente import *
from forms.orcamento import *
from models.Cliente import *
from models.Orcamento import *
from models.Pesquisa import *
from datetime import datetime

@app.route('/processar_dados', methods=['POST'])
def processar_dados():
    try:
        cliente = ClienteForm()
        nome = cliente.nome.data
        email = cliente.email.data
        telefone = cliente.telefone.data
        
        print(nome, email, telefone)
        
        try:
            
            session['email'] = email
            session['telefone'] = telefone
            session['nome'] = nome
            
            novo_cliente = Cliente(
                nome = nome,
                email = email,
                telefone = telefone
            )
            
            db.session.add(novo_cliente)
            db.session.commit()
            
            return redirect(url_for('formestatistica'))
        except Exception as e:
            print(e)
        
        
    except Exception as e:
        print(e)
        
@app.route('/processar_orcamento', methods=['POST'])
def processar_orcamento():
    try:
        orcamento = PesquisaForm()
        nome_estado = orcamento.nome_estado.data
        nome_cidade = orcamento.nome_cidade.data
        populacao = orcamento.populacao.data
        eleitorado = orcamento.eleitorado.data
        margem_erro = orcamento.margem_erro.data
        confianca = orcamento.confianca.data
        tipo_pesquisa = orcamento.tipo_pesquisa.data
        qnt_perg = orcamento.qnt_perg.data
        qnt_urbanas = orcamento.qnt_urbanas.data
        qnt_rurais = orcamento.qnt_rurais.data
        
        print(nome_estado, nome_cidade, populacao, eleitorado, margem_erro, confianca, tipo_pesquisa, qnt_perg, qnt_urbanas, qnt_rurais)
        
        try:
            
            cliente = Cliente.query.filter_by(email=session.get('email')).first()
            print(cliente.id)
            nova_pesquisa = Pesquisa(
                cliente_id=cliente.id,
                nome_estado=nome_estado,
                nome_cidade = nome_cidade,
                populacao=populacao,
                eleitorado=eleitorado,
                margem_erro=margem_erro,
                confianca=confianca,
                tipo_pesquisa=tipo_pesquisa,
                qnt_perg=qnt_perg,
                qnt_urbanas=qnt_urbanas,
                qnt_rurais=qnt_rurais
            )
            
            print(nova_pesquisa.id)
            
            db.session.add(nova_pesquisa)
            db.session.commit()
            
        except Exception as e:
            print("erro db: ")
            print(e)
    except Exception as e:
        print("erro_rota: ")
        print(e)