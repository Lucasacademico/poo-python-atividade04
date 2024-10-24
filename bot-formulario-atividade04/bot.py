
from botcity.web import WebBot, Browser, By
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False
from webdriver_manager.chrome import ChromeDriverManager

from classes.form_base import FormBase
from classes.form_contato import FormContato
from classes.form_login import FormLogin


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    # Preencher os campos do formulário de cadastro
    contato1 = FormContato(nome="Lucas", email="lucas.andrade@ifam.edu.br", telefone="(92)98145-8913", assunto="Suporte", mensagem="Preciso de ajuda")
    contato1.dados_cadastrados()
    
    # Implement here your logic...
    bot.browse("http://127.0.0.1:5000/cadastro")
    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(contato1.nome)
    bot.wait(500)
    bot.find_element('//*[@id="email"]', By.XPATH).send_keys(contato1.email)
    bot.wait(500)
    bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(contato1.telefone)
    bot.wait(500)
    bot.find_element('//*[@id="assunto"]', By.XPATH).send_keys(contato1.assunto)
    bot.wait(500)
    bot.find_element('//*[@id="mensagem"]', By.XPATH).send_keys(contato1.mensagem)
    bot.wait(500)
    bot.find_element('/html/body/div/form/input[5]', By.XPATH).click()
    bot.wait(500)
    
    contato1 = FormLogin(nome='', usuario='Lukinhas', senha='asd123')
    bot.find_element('//*[@id="usuario"]', By.XPATH).send_keys(contato1.usuario)
    bot.wait(500)
    bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(contato1.senha)
    bot.wait(500)
    bot.find_element('/html/body/div/form/input[3]', By.XPATH).click()
    bot.wait(500)


    bot.wait(3000)
    bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
