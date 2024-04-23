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

##Neste teste, username vazio ou password vazia


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("REQ1 - Pagina de Login e Registo")
@allure.story("Teste de Login com username e password válidos")
def test_no_problem():
    '''
    Function to test a successful login with valid credentials

    This function navigates to the login page, enters valid username and password,
    clicks the login button, waits for the page to load, and checks if the URL matches the expected URL

    Arguments:
        None

    Returns:
        int: 1 if the test is successful (URL matches the expected value), 0 otherwise

    Raises:
        If the page loaded have a title difrent from "Login Page"
    '''
    i = 0

    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")

    if not "Login" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()
    
    username = "justAUser1"
    password = "admin123"
    
    #USERNAME E PASS VAZIOS

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    time.sleep(1)

    expected_url = "http://localhost:3000/"

    current_url = driver.current_url

    if (current_url == expected_url or current_url == "http://localhost:3000"):
        i+=1
    
    driver.close()
    if i == 1:
        assert True, "Test passed"
    else:
        assert False, "Test failed"

if __name__ == "__main__":
    pytest.main(["test_1_6_Login_No_Problem.py", "-v", "-s"])
