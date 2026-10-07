from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        senha_hash = generate_password_hash(senha)
        
        usuario = database.buscar_usuario_por_email(email)
        
        if not usuario:
            novo_usuario = database.criar_usuario(nome, email, senha_hash)
            database.montar_usuario(linha={'id':novo_usuario.id, 'nome':nome, 'email':email, 'senha_hash':senha_hash})
            return redirect(url_for('auth.login'))
        
        return redirect(url_for("auth.registro"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = database.buscar_usuario_por_email(email)
        if usuario and check_password_hash(usuario.senha_hash, senha):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('index'))
            
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    return redirect(url_for("index"))