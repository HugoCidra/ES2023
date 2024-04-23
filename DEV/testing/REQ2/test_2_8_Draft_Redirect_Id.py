import sys
import allure
import pytest
import time
import logging
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
@allure.feature('REQ2')
@allure.story('Testa o Butão de Rascunho')

def test_draft():
    '''Function responsible for test the "Draft" button
    This function clicks on a draft button and checks if it occurs correctly
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the main
    
    Returns:
        Int(1 if it correctly accesses the page of the creation of quiz, 0 otherwise)
    
    Raises:
        None
    
    '''
    driver = webdriver.Chrome()

    login(driver)
    i = 0
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "links_nav")))
    
    element_to_be_tested =  driver.find_element(By.CSS_SELECTOR, 'p[class="MyQuizzes_quiz state_1"]')
    
    if element_to_be_tested == None:
        i = 1

    if i == 0:
        element_to_be_tested.click()

        expected_url = "http://localhost:3000/create-quizz/"

        current_url = driver.current_url
        
        if expected_url in current_url:
            i+=1

    driver.close()

    if i == 1:
        assert True, "Test passed"
    else:
        assert False, "Test failed"

# PATH = "C:\Program Files (x86)\Chromedriver.exe"

if __name__ == "__main__":
    pytest.main([__file__])
