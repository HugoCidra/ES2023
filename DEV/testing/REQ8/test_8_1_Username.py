import time
from selenium.common.exceptions import TimeoutException

import logging
from typing import final 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import allure
logging.basicConfig(filename="log.txt", level=logging.INFO)




def login(driver):
    '''Function responsible for login in the application with a valid account
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the function test_username()

    Returns:
        Username
    '''
    driver.get("http://localhost:3000/login")
    driver.maximize_window()

    username = "justAUser1"
    password = "admin123"

    try:
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys(username)

        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        driver.find_element(By.ID, "password").send_keys(password)

        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        login_button = driver.find_element(By.ID, "login")
        login_button.click()

        

        return username
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        raise
    except TimeoutException as e:
        print(f"Timeout while waiting for element: {e}")
        raise

def goto_Profile(driver):
    '''Function responsible for going to the Profile page from Home page.

    Arguments:
        driver (webdriver): Selenium webdriver created in the function test_username().
    
    Returns:
        True if the redirection is correct, False otherwise.
    '''
    try:
        
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"menuButton")))
        menu_button = driver.find_element(By.ID, "menuButton")
        menu_button.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ProfileButton")))
        profile_button = driver.find_element(By.ID, "ProfileButton") 
        profile_button.click()

       
        expected_url = "http://localhost:3000/profile"
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))

        return True
    except TimeoutException:
        print("Failed to navigate to the profile page or the page did not load in time.")
        return False



@allure.severity(allure.severity_level.NORMAL)
@allure.feature("REQ8")
@allure.story("Pagina de perfil")
def test_username():
    '''Function responsible for testing profile page
    
    Arguments:
        None
    
    Returns:
        True if the test is a sucess
    '''
    driver = webdriver.Chrome()
    user = login(driver)
    if not goto_Profile(driver):
        assert False, "Redirection to Profile page failed"
    

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"menuButton")))
    menu_button = driver.find_element(By.ID, "menuButton")
    menu_button.click()
    username_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "nome"))
)
    username = username_element.text

    if (user == username):
        assert True, "Username is correct"
    
    

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])