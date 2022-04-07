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

    def cookies_accept(self):
        xpath = '//*[@id="sp-cc-accept"]'
        #'//span[@id="a-autoid-0-announce"]'
        try:
            time.sleep(2)
            WebDriverWait(self.driver,2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
        except TimeoutException:
            pass
    def search(self):
        xpath ='//*[@id="twotabsearchtextbox"]'
        #'//*[@id="twotabsearchtextbox"]'
        xpath1 = '//*[@id="nav-search-submit-button"]'

        try:
            time.sleep(2)
            #WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
            self.driver.find_element(By.XPATH,xpath).send_keys("Lego Duplo")
            self.driver.find_element(By.XPATH, xpath1).click()
        except TimeoutException:
            print('no elements found')

    def legobrand_checkbox(self):
        xpath = '//*[@id="p_89/LEGO"]/span'
        #'//*[@id="p_89/LEGO"]/span/a/div/label/i'
        #//*[@id="p_89/LEGO"]/span/a/span
        try:
            time.sleep(2)
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
        except TimeoutException:
            print('no elements found')

    def age_checkbox(self):
        xpath = '//*[@id="p_n_age_range/391968011"]/span/a/span'
        self.driver.find_element(By.XPATH, xpath).click()
    
    def customer_rating(self):
        xpath = '//*[@id="p_72/184319031"]/span/a/section/i'
        #'//*[@id="p_72/184319031"]/span/a/section/span'
        self.driver.find_element(By.XPATH, xpath).click()

    def find_container(self):
        '//*[@class="sg-col-4-of-12"]'
        #sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20
        #'//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]'
        #//*[@id="search"]/div[1]/div[1]/div/span[3]/div[1]'
        return self.driver.find_elements(By.XPATH, '//div[contains(@class="sg-col-4-of-12")]')
    
if __name__ == '__main__' : 
    
    bot = Scraper()
    bot.cookies_accept()
    bot.search()
    bot.legobrand_checkbox()
    bot.age_checkbox()
    bot.customer_rating()
    bot.find_container()
    #list = container.find_element(By.XPATH, './div')

