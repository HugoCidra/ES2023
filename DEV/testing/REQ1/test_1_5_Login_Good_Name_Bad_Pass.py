import sys
import pytest
import allure
import time
import logging
from typing import final
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

logging.basicConfig(filename="log.txt", level=logging.INFO)

##Neste teste, username existente com password diferente


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("REQ1 - Pagina de Login e Registo")
@allure.story("Teste de Login com username válido e password inválida")
def test_login_good_name_bad_pass():
    '''Function responsible for the unsuccessful login with the valid username and invalid password
    
    Arguments:
        None

    Returns:
        1 if the test is successful (App's response is the intended), 0 otherwise
    
    Raises:
        If the login page could not be loaded
    '''
    i = 0
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")

    if not "Login" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser1"
    password = "password1"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-login")))

    time.sleep(1)

    alert = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/p')

    if alert.text == "Invalid Credentials!":
        i += 1

    driver.close()

    if i == 1:
        assert True, "Test passed"
    else:
        assert False, "Test failed"

if __name__ == "__main__":
    pytest.main(["test_1_5_Login_Good_Name_Bad_Pass.py", "-v", "-s"])
