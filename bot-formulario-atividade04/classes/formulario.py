class FormBase:
    def __init__(self, nome):
        self.nome = nome

    def dados_cadastrados(self):
        print(f'Nome: {self.nome}')


class FormContato(FormBase):
    def __init__(self, nome, email, mensagem, telefone, assunto):
        super().__init__(nome)
        self.email = email
        self.mensagem = mensagem
        self.telefone = telefone
        self.assunto = assunto

    def dados_cadastrados(self):
        super().dados_cadastrados()
        print(f'Email: {self.email}')
        print(f'Assunto: {self.assunto}')
        print(f'Mensagem: {self.mensagem}')
        print(f'telefone: {self.telefone}')

class FormLogin(FormBase):
    def __init__(self, nome, usuario, senha):
        super().__init__(nome)
        self.usuario = usuario
        self.senha = senha

    def dados_cadastrados(self):
        super().dados_cadastrados()
        print(f'Usuario: {self.usuario}')
        print(f'Senha: {self.senha}')