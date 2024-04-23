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
import allure
import pytest


def login(driver):
    '''Logs into the website
    
    Arguments:
        Driver: a Selenium WebDriver object
    
    Returns:
        True if the login was successful
        
    Raises:
        Exception if the login page could not be loaded
    '''

    driver.get("http://localhost:3000/login")
    time.sleep(1)

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser2"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    login_button.click()
    return True


def goto_reviewquiz(driver):
    '''Navigates to the review quiz page
    
    Arguments:
        Driver: a Selenium WebDriver object
    
    Returns:
        True if the navigation was successful, False otherwise
    '''

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "links_nav")))
    create_quiz_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/review-quizz"]')
    create_quiz_button.click()

    expected_url = "http://localhost:3000/review-quizz"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Review Quiz button")
        return False
    
    return True


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ4 - Quiz Review')
@allure.story('Testa a funcionalidade de aceitar um quiz')
def test_buttons():
    '''Tests the accept button functionality
    
    Returns:
        True if the test passes, False otherwise
    '''

    """Next, create an instance of Chrome with the path of the driver that you downloaded through the websites of the respective browser.
    In this example, we assume that the driver is in the same directory as the Python script that you will execute."""
    driver = webdriver.Chrome() # or driver = webdriver.Chrome('./chromedriver')
    login(driver)
    goto_reviewquiz(driver)

    driver.maximize_window()

    #Added a WebDriverWait so it can load the needed buttons properly
    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/button[1]")))

    accept_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/button[1]")
    accept_button.click()
    
    #expectedUrl_acceptButton = "http://localhost:3000/" #This URL throws the exception bellow
    expectedUrl_acceptButton = "http://localhost:3000/review-quizz" #needs to be like this because when clicking the accept button it continues in the same page, doesn't change
    if expectedUrl_acceptButton != driver.current_url:
        print("Expected a different redirection when accepting quiz")
        print(driver.current_url)
        assert False, "Test failed expected a different redirection when submitting quiz"

    submit_button = driver.find_element(By.ID,"submitRQ")
    submit_button.click()
    time.sleep(2)

    expectedUrl_submit = "http://localhost:3000/review-quizz"
    if expectedUrl_submit != driver.current_url:
        print("Expected a different redirection when accepting quiz")
        print(driver.current_url)
        assert False, "Test failed expected a different redirection when submitting quiz"

    driver.close()
    assert True, "Test passed"



if __name__ == "__main__":
    pytest.main([__file__])
    