#%%
import pytest
from Selenium.Lego.Legoscraper import Scraper
from selenium.webdriver.common.by import By

def test_scraper():
    ws = Scraper("https://www.lego.com/en-gb")
    yield ws
    ws.quit()

#%%
#
        
#def test_constructor(self):
    #ws = Scraper("https://www.lego.com/en-gb")
    #assert ws._driver.session_id
    #ws.quit(self)