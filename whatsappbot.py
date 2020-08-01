from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Teste Bot do Whatsapp"
        self.grupos = ["Suellen Suemi"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagem(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for pessoas in self.grupos:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{pessoas}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagem()
