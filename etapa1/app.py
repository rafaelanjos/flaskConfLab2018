from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route("/")
@app.route("/index.php")
def hello():
	return "Olá Mundo!"


@app.route("/rota1")
def view_da_rota1():
	return "Essa é uma nova view da /rota1"


@app.route("/rota2/<nome>")
def view_da_rota2(nome):
	return "Bem vindo, " + nome + "! Essa é a view da /rota2!"


@app.route("/ola/<nome>")
def view_com_template(nome):
	return render_template("index.html", nome_template=nome)


@app.route("/api")
def view_com_json():
	return jsonify({"mensagem": "Bem vindo a sua primeira API REST!"})

