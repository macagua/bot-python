import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

USER_IG = os.getenv('USER_IG')
PASSWORD_IG = os.getenv('PASSWORD_IG')
DRIVER_PATH = os.getenv('DRIVER_PATH')
LINK_DO_POST = os.getenv('LINK_DO_POST')


class InstagramBot:
    def __init__(self, userName, password, link_do_post, driver):
        """ Class constructor """
        self.userName = userName
        self.password = password
        self.link_do_post = link_do_post
        self.driver = webdriver.Firefox(executable_path=driver)

    def login(self):
        """ Instagram login function """

        driver = self.driver
        # The link for instagram login
        driver.get(
            "https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(4)
        # The username field
        userfield = driver.find_element_by_xpath('//input[@name="username"]')
        userfield.click()
        userfield.clear()
        userfield.send_keys(self.userName)
        # The password field
        pswdfield = driver.find_element_by_xpath("//input[@name='password']")
        pswdfield.click()
        pswdfield.clear()
        pswdfield.send_keys(self.password)
        pswdfield.send_keys(Keys.RETURN)
        time.sleep(5)

    @staticmethod
    def typing(phrase, wheretype):
        """ Function for typing the comment to post """
        for letters in phrase:
            wheretype.send_keys(letters)
            time.sleep(random.randint(1, 5)/30)

    def coment(self):
        """ Function of comments to post """
        driver = self.driver
        # The link to do post
        driver.get(self.link_do_post)
        time.sleep(4)
        driver.execute_script('window.scrollTo(0,300);')

        for i in range(0, 1000):
            try:
                # The comments random to post
                coments = [
                    'Quero ganhar!', 'Contando com a sorte', 'Qualquer Coisa', 'Comentando',
                    'Vou ganhar', 'Já ganhei!', 'Quero', 'Espero muito ganhar', 'Tentando',
                    'Não custa nada tentar', 'Quero muito!', 'Espero ganhar!', '$$$', '$', '$$',
                    '$$$', '$$$$$', '$$$$', '$$$$$$$$$$$$$' '$$$$$$' '$$$$$$$'
                ]
                driver.find_element_by_class_name("Ypffh").click()
                # The coment field
                comentfield = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(4, 10))
                self.typing(random.choice(coments), comentfield)
                time.sleep(random.randint(15, 40))
                # The Post button
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Post')]").click()
                time.sleep(random.randint(4, 10))
                # The link to do post
                driver.get(self.link_do_post)
                time.sleep(random.randint(4, 10))
                driver.execute_script('window.scrollTo(0,300);')

                print(i)
            except Exception as e:
                print('erro: ')
                print(i)
                print(e)
                time.sleep(2)


bot = InstagramBot(USER_IG, PASSWORD_IG, LINK_DO_POST, DRIVER_PATH)
bot.login()
time.sleep(5)
bot.coment()

