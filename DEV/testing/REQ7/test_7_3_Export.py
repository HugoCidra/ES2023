import sys
import unittest
import time
import logging
import os
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import allure
logging.basicConfig(filename="log.txt", level=logging.INFO)

#Melhorar com verificacoes
def login(driver):
    '''Function responsible for login in the application with a valid account

                Arguments:
                    driver (webdriver): Selenium webdriver created in the main

                Returns:
                    None

                Raises:
                    If the page loaded have a title difrent from "Login Page"
    '''
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()

    #TODO alterar para um user que seja solver
    username = "justAUser1"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("REQ7 - Menu")
@allure.story("Export")
def test_export():
    '''Function responsible for testing the export of a file
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the main
    
    Returns:
        0 if the test was a sucess 
    '''
    i = 0

    driver = webdriver.Chrome()
    login(driver)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="menuButton"]'))) # wait for the page to load

    menu_button = driver.find_element(By.CSS_SELECTOR, 'div[id="menuButton"]') # goes to the admin page
    menu_button.click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Export")]'))).click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[class="mm-popup__box"]')))

    text_popup = driver.find_element(By.CSS_SELECTOR, "div[class='mm-popup__box__body']").text

    driver.find_element(By.CSS_SELECTOR, 'button[class="mm-popup__btn mm-popup__btn--ok"]').click()

    if text_popup == "Quizzes exported successfully!":
        i = 0

    driver.close()

    if i == 0:
        assert True, "Test has sucess"
    else:
        assert False, "Test has failed"

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])