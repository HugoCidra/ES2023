import sys
import unittest
import time
import logging
from typing import final 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import allure
import pytest
logging.basicConfig(filename="log.txt", level=logging.INFO)


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("REQ1 - Pagina de Login e Registo")
@allure.story('Login com username e password vazios')
def test_empty_name_empty_pass():
    '''Function responsible for an insucessful login with an empty username and password
    
    Arguments:
        None

    Returns:
        1 if the test is successful (App's response is the intended), 0 otherwise
    
    Raises:
        If the login page could not be loaded
    '''

    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")

    driver.maximize_window()

    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    register_button = driver.find_element(By.ID, "login")
    register_button.click()

    time.sleep(1)

    
    alert = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/p')

    if (alert.text != "Invalid Credentials!"):
        assert False, "Alert text does not match the expected ('Invalid Credentials!')"
    else:
        assert True, "Test successful." 
        
    
if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
