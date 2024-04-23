import logging
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(filename="log.txt", level=logging.INFO)

def login(driver):
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception("Unable to load Login Page")

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
@allure.story('Testar o filtro do MyQuizzes')

#verifica se ao selecionar o icon da navbar ele vai para a pagina de profile
def test_logout_button():
    driver = webdriver.Chrome()

    login(driver)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "MyQuizzes_title")))

    moreButton = driver.find_element(By.ID, "menuButton")
    moreButton.click()

    time.sleep(1)

    hurl = "/login"
    logout = driver.find_element(By.XPATH, '//a[@href="'+hurl+'"]')
    logout.click()

    if driver.current_url == "http://localhost:3000/login":
        driver.close()
        assert True, "Test passed"
    else:
        driver.close()
        assert False, "Test failed"


if __name__ == "__main__":
   pytest.main([__file__])