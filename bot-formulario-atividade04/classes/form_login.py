from classes.form_base import FormBase


class FormLogin(FormBase):
    def __init__(self, nome, usuario, senha):
        super().__init__(nome)
        self.usuario = usuario
        self.senha = senha

    def dados_cadastrados(self):
        super().dados_cadastrados()
        print(f'Usuario: {self.usuario}')
        print(f'Senha: {self.senha}')