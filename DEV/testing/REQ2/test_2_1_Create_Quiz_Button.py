import sys
import unittest
import time
import logging
from typing import final 
from selenium import webdriver
import allure
import pytest
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
logging.basicConfig(filename="log.txt", level=logging.INFO)


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
        raise Exception("Não foi possível carregar a página de login")

    driver.maximize_window()

    username = "justAUser1"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ2')
@allure.story('Testa o botão de Criar Quiz')
def test_create_quiz():
    '''
    Function to test the "Create Quiz" button functionality

    This function navigates to the "Create Quiz" page and checks if the URL matches the expected URL

    Arguments:
        driver (webdriver): Selenium webdriver created in the main

    Returns:
        int: 1 if the test is successful (URL matches the expected URL), 0 otherwise

    Raises:
        None
    '''
    driver = webdriver.Chrome()
    login(driver)
    i = 0
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a")))
    create_quiz_button = driver.find_element(By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a")
    create_quiz_button.click()

    expected_url = "http://localhost:3000/create-quizz"
    current_url = driver.current_url
    if current_url == expected_url:
        i = 1
    driver.close()

    if i == 1:
        assert True, "Test passed"
    else:
        assert False, "Test failed"

if __name__ == "__main__":
    pytest.main([__file__])

