import re
import logging
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

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

#verifica se ao selecionar accepted aparece um quiz específico e se ao selecionar pending n aparece nenhum, de acordo com os dados do utilizador de teste
def test_myquizzes_filter():
    driver = webdriver.Chrome()

    login(driver)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "MyQuizzes_title")))

    #accepted

    select_element = driver.find_element(By.CLASS_NAME, "filter")
    select = Select(select_element)
    select.select_by_value("4")
    time.sleep(1)

    src = driver.page_source
    text_found = re.search(r'What is the function of a primary key?', src)

    if text_found is None:
        assert False, "Test failed"

    # rejected

    select.select_by_value("3")
    time.sleep(1)

    src = driver.page_source
    text_found = re.search(r"Which of the following options best describes strategic analysis?", src)

    if text_found is None:
        assert False, "Test failed"

    # pending

    select.select_by_value("2")
    time.sleep(1)

    src = driver.page_source
    text_found = re.search("From the instructions below, which is the TAL", src) #os parentesis estão a fazer confusão nesta pergunta

    if text_found is None:
        assert False, "Test failed"

    # draft

    select.select_by_value("1")
    time.sleep(1)

    src = driver.page_source
    text_found = re.search(
        r'When is a grammar said to be ambiguous?',
        src)

    if text_found is None:
        assert False, "Test failed"

    # all

    select.select_by_value("0")
    time.sleep(1)

    src = driver.page_source
    text_found = re.search(
        r'What is the primary function of the Transmission Control Protocol',
        src)

    if text_found is None:
        assert False, "Test failed"

    driver.close()

    ###

    assert True, "Test passed"

if __name__ == "__main__":
   pytest.main([__file__])


