class FormBase:
    def __init__(self, nome):
        self.nome = nome

    def dados_cadastrados(self):
        print(f'Nome: {self.nome}')