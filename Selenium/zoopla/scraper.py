from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


class Scraper():
    def __init__(self, url : str = 'https://www.zoopla.co.uk/'):
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(url)
if __name__ == '__main__' : 
    bot = Scraper()

    def lego_continue(self, xpath : str = '//span[@class = AgeGatestyles__StyledText-xudtvj-11 eLvrYKButton__Base-sc-1jdmsyi-0 eLFkVi AgeGatestyles__StyledButton-xudtvj-12 hycfPw@]'):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
        except TimeoutException:
            pass


    