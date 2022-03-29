from lib2to3.pgen2 import driver
from logging import exception
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
class Scraper():
    def __init__(self,url:str = 'https://www.amazon.co.uk/'):
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(url)

    def search (self, xpath: str = "//input[contains(@id,'twotabsearchtextbox')]"):
        try:

            time.sleep(10)
            self.driver.find_element(By.XPATH,xpath).send_keys("Lego Duplo")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
        except TimeoutException:
            print('no elements found')

    #def lego_continue(self, xpath : str = '//div[@class = AgeGatestyles__StyledText-xudtvj-11 eLvrYKButton__Base-sc-1jdmsyi-0 eLFkVi AgeGatestyles__StyledButton-xudtvj-12 hycfPw@]'):
        #try:
        
            #WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            #self.driver.find_element(By.XPATH, xpath).click()
        #except TimeoutException:
            #print('No butons found')

if __name__ == '__main__' : 
    bot = Scraper()
    bot.search()
    