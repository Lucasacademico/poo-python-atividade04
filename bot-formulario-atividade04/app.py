from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para o cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para o login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para processar o formulário de cadastro
@app.route('/submit_cadastro', methods=['POST'])
def submit_cadastro():
    # Processamento do formulário de cadastro
    return '''
        <h1>Formulário de cadastro enviado com sucesso!</h1>
        <p>Você será redirecionado para a página de login em 3 segundos...</p>
        <script>
            setTimeout(function() {
                window.location.href = "/login";
            }, 3000);  // 3000 milissegundos = 3 segundos
        </script>
    '''

# Rota para processar o formulário de login
@app.route('/submit_login', methods=['POST'])
def submit_login():
    # Processamento do formulário de login
    return '''
        <h1>Usuário logado com sucesso!</h1>
        <p>Você será redirecionado para a página inicial em 3 segundos...</p>
        <script>
            setTimeout(function() {
                window.location.href = "/";
            }, 3000);  // 3000 milissegundos = 3 segundos
        </script>
    '''

if __name__ == '__main__':
    app.run(debug=True)
