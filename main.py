from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html',
                         title='Avaliação contínua: Aula 030',
                         options=["Home", "Identificacao", "requisicao"])


@app.route('/identificacao')
def identificacao():
  return render_template('identificacao.html',
                         title='Avaliação contínua: Aula 030',
                         aluno='Mayumi Melo',
                         prontuario='PT3020428',
                         instituicao='IFSP')


@app.route('/contexto_requisicao')
def contexto_requisicao():
  navegador = request.user_agent.browser
  ip = request.remote_addr
  host = request.host

  return render_template('contexto_requisicao.html',
                         title='Avaliação contínua: Aula 030',
                         navegador=navegador,
                         ip=ip,
                         host=host)