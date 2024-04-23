import sys
import unittest
import time
import logging
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import string
import allure
import pytest
logging.basicConfig(filename="log.txt", level=logging.INFO)



@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("REQ1 - Pagina de Login e Registo")
@allure.story('Registo bem-sucedido na aplicação')
def test_no_problem():
    '''Function responsible for the sucessful register in the application (similar to 1.2)
    
    Arguments:
        None

    Returns:
        1 if the test is successful (App's response is the intended), 0 otherwise
    
    '''
    i = 0

    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")

    
    driver.maximize_window()
    
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    email = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + '@gmail.com'

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "email").send_keys(email)
    register_button = driver.find_element(By.ID, "login")
    register_button.click()

    time.sleep(1)

    expected_url = "http://localhost:3000/"

    current_url = driver.current_url

    if (current_url != expected_url and current_url != "http://localhost:3000"):
        assert False, "The current URL does not match the expected URL ('http://localhost:3000/' or 'http://localhost:3000')"

    driver.close()
    assert True, "Test was successful"

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
    