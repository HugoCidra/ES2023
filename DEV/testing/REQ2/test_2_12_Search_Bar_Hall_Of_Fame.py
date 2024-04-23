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

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

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

    if not "Login" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser1"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()


#hall of fame inicial tem três elementos (justAUser1, justAUser2, justAUser3)


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ2')
@allure.story('Testar a search bar do Hall of Fame')

def test_halloffame_searchbars(driver):
    ##########
    # TESTE 1 ->testar  várias matches (input = justAUser, deve encontrar justAUser1, justAUser2 e justAUser3)

    i = 0

    login(driver)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "HOF_SearchBar input.SearchBar_input")))
    search_bar = driver.find_element(By.CLASS_NAME, "HOF_SearchBar input.SearchBar_input")
    search_bar.send_keys("justAUser")

    dropdown_element = driver.find_element(By.CLASS_NAME, "HOFdropdown")
    WebDriverWait(driver, 10).until(EC.visibility_of(dropdown_element))

    hall_of_fame_users = ["justAUser1", "justAUser2"]

    for user in hall_of_fame_users:
        user_element = dropdown_element.find_element(By.XPATH, f".//*[contains(text(), '{user}')]")
        if user_element.is_displayed():
            i += 1

    if (i == len(hall_of_fame_users)):
        assert True, "All expected users displayed"
    else:
        assert False, "Not all expected users displayed"
   
    ##########
    # TESTE 2 -> testar uma única match (input = justAUser1, deve devolver SÓ justAUser1)

    i = 0

    login(driver)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "HOF_SearchBar input.SearchBar_input")))
    search_bar = driver.find_element(By.CLASS_NAME, "HOF_SearchBar input.SearchBar_input")
    search_bar.send_keys("justAUser1")

    # Wait for dropdown to appear
    dropdown_element = driver.find_element(By.CLASS_NAME, "HOFdropdown")
    WebDriverWait(driver, 10).until(EC.visibility_of(dropdown_element))

    # Find and count the usernames in the dropdown
    user_buttons = dropdown_element.find_elements(By.CLASS_NAME, 'dropdownbutton')
    displayed_users = [button.text for button in user_buttons]
    elements_count = len(displayed_users)

    hall_of_fame_users = ["justAUser1"]

    user_elements = dropdown_element.find_elements(By.XPATH, f".//*[contains(text(), '{hall_of_fame_users[0]}')]")
    if (user_elements and user_elements[0].is_displayed()):
        i += 1
    
    # Check if the user element is displayed (and if it's the only user element displayed)
    if (i == 1 and elements_count == 1):
        assert True, "User not displayed"
    else:
        assert False, "More than one user displayed"


    ##########
    # TESTE 3 -> testar com um user que não existe (input = justAUser10, não deve devolver nada, logo, não aparece o dropdown)

    login(driver)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "HOF_SearchBar input.SearchBar_input")))
    search_bar = driver.find_element(By.CLASS_NAME, "HOF_SearchBar input.SearchBar_input")
    search_bar.send_keys("justAUser10")

    try:
        # Attempt to find the dropdown, if found, the test fails
        dropdown_element = driver.find_element(By.CLASS_NAME, "HOFdropdown")
        assert False, "Test failed"
    except NoSuchElementException:
        # If NoSuchElementException is raised, the dropdown is not present, and the test passes
        assert True, "Test passed"


if __name__ == "__main__":
    pytest.main([__file__])