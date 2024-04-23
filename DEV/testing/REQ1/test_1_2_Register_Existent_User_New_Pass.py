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
import allure
import pytest
logging.basicConfig(filename="log.txt", level=logging.INFO)



@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('REQ1 - Pagina de Login e Registo')
@allure.story('login com username existente na aplicação')
def test_existent_user_new_pass():
    '''Function responsible for the unsuccessful register in the application with an existent username
    
    Arguments:
        None

    Returns:
        1 if the test is successful (App's response is the intended), 0 otherwise
    
    Raises:
        Exception if the login page could not be loaded
    '''

    i = 0

    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")

    if not "Login Page" in driver.title:
        assert False, "Page title does not match the expected ('Login Page')"

    driver.maximize_window()
    
    username = "justAUser1"
    password = "admin1234"
    email = "david@gmail.com"



    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "email").send_keys(email)
    register_button = driver.find_element(By.ID, "login")
    register_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-register")))
    
    time.sleep(1)

    alert = driver.find_element(By.XPATH, '//*[@id="form-register"]/p')

    if (alert.text == "Username already exists!"):
        i+=1
    
    driver.close()
    if i == 1:
        assert True, "Test had success"
    else:
        assert False, "Test failed"

if __name__ == "__main__":
    pytest.main([__file__])
