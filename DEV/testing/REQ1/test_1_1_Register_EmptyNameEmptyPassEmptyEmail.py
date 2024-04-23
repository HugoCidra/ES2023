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




@allure.feature('REQ1 - Pagina de Login e Registo')
@allure.story('Registo com username e/ou password vazios')
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_name_empty_pass():
    '''Function responsible for an unsuccessful register with an empty username and password, with a valid username and empty password and with an empty username and a valid password
    
    Arguments:
        None

    Returns:
        int: 1 if the test is successful (App's response is the intended), 0 otherwise
    
    Raises:
        Exception if the login page could not be loaded
    '''

    i = 0

    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()
    
    username = "justAUser1"
    password = "admin123"
    email = "david@gmail.com"
    vazia = ""

    
    #EMPTY EMAIL, USERNAME AND PASS

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(vazia)
    driver.find_element(By.ID, "password").send_keys(vazia)
    driver.find_element(By.ID, "email").send_keys(vazia)
    register_button = driver.find_element(By.ID, "login")
    register_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-register")))

    alert = driver.find_element(By.XPATH, '//*[@id="form-register"]/p')

    if (alert.text == "Email field is empty\nUsername must be between 6 and 18 characters\nPassword must be between 8 and 18 characters"):
        i+=1
        

    #VALID USERNAME, EMPTY PASS AND EMAIL
    driver.refresh()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(vazia)
    driver.find_element(By.ID, "email").send_keys(vazia)
    register_button = driver.find_element(By.ID, "login")
    register_button.click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-register")))

    alert = driver.find_element(By.XPATH, '//*[@id="form-register"]/p')
    
    if (alert.text == "Email field is empty\nPassword must be between 8 and 18 characters"):
        i+=1


    #VALID PASS, EMPTY USERNAME AND EMAIL
    driver.refresh()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(vazia)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "email").send_keys(vazia)
    register_button = driver.find_element(By.ID, "login")
    register_button.click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-register")))

    alert = driver.find_element(By.XPATH, '//*[@id="form-register"]/p')
    
    if (alert.text == "Email field is empty\nUsername must be between 6 and 18 characters"):
        i+=1


    #VALID EMAIL, EMPTY USERNAME AND PASS
    driver.refresh()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(vazia)
    driver.find_element(By.ID, "password").send_keys(vazia)
    driver.find_element(By.ID, "email").send_keys(email)
    register_button = driver.find_element(By.ID, "login")
    register_button.click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-register")))

    alert = driver.find_element(By.XPATH, '//*[@id="form-register"]/p')
   
    if (alert.text == "Username must be between 6 and 18 characters\nPassword must be between 8 and 18 characters"):
        i+=1

    driver.close()
    if i == 4:
        assert True, "Test had success"
    else:
        assert False, "Test failed"

if __name__ == "__main__":
    pytest.main([__file__])
    
