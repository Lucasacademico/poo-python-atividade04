from classes.form_base import FormBase


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