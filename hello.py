from flask import Flask
from flask import request
from flask import url_for, redirect, render_template, flash, session
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'3d0fb209bba6fd45601f560a75c335210665d06fce2c15c182e3cfbd8604d9aa'

# @app.route('/')
# def index():
#     # app.logger.debug('Accessing index page...')
#     # app.logger.warning('A warning occurred (%d apples)', 42)
#     # app.logger.error('An error occurred')
#     # return '<h1>Index Page</h1>'
#     return redirect(url_for('login'))

'''
@app.route('/hello')
def hello_world():
    return '<h1>Hello, World!!!</h1>'

@app.route("/<name>")
def hello(name):
    return f"<h1>Olá, {escape(name)}!</h1>"
'''

'''
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello_world'))
    print(url_for('hello', name='John Doe'))
'''

''' Métodos HTTP - GET, POST, etc '''
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
'''
''' FORMA ALTERNATIVA 
@app.get('/login')
def login_get():
    return show_the_login_form()
@app.post('/login')
def login_post():
    return do_the_login()
'''
@app.route('/')
def home():
    # template_data = set(())
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        # title = {
        #     'shortTitle' : 'HomE', 
        #     'longTitle' : '---HOME---'
        # }
        title = 'Home'
        article = {
            'title': 'Lorem Ipsum',
            'content': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent luctus urna et neque bibendum, at ultrices velit sodales. Proin at feugiat tortor. Vestibulum ligula lorem, placerat eget erat eget, fermentum rutrum mi. Nulla ut molestie lectus.</p><p>Pellentesque condimentum venenatis velit, non blandit urna mattis sit amet. Praesent dignissim nunc et lorem convallis, a commodo dolor rhoncus. Cras hendrerit id quam a congue.</p><p>In et augue id ex semper volutpat a et augue.</p>'
        }
        return render_template('home.html', title=title, article=article)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     if name not in session:
#         return redirect(url_for('login'))
#     return render_template('hello.html', name=name)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = None
    
    # Verifica se usuário já está logado
    if 'username' in session:
        return log_the_user_in(session['username'])
    
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            return log_the_user_in(request.form['username'])
        else:
            error = 'Credenciais inválidas. (admin:admin)'
    # o código abaixo vai executar quando a requisição for GET 
    # ou as credenciais forem inválidas
    return render_template('login.html', error=error)

# @app.route('/adminlte/')
# def adminlte():
#     return render_template('fixed-sidebar.html')

@app.route('/logout/')
def logout():
    # remover a variável username da sessão
    session.pop('username', None)
    # flash('Vc foi deslogado do sistema')
    return redirect(url_for('login'))

def valid_login(username, password):
    return (username == 'admin' and password == 'admin')

def log_the_user_in(username):
    # flash('Login realizado com sucesso')
    # app.logger.debug('Login realizado com sucesso')
    return redirect(url_for('home'))

@app.route('/graficos')
def graficos():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        title = 'Gráficos'
        # Carregar script específico dessa página
        scripts = ['charts.js']
        return render_template('graficos.html', title=title, scripts=scripts)

@app.route('/tabelas')
def tabelas():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        title = 'Tabelas'
        scripts = ['tables.js']
        return render_template('tabelas.html', title=title, scripts=scripts)

