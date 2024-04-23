import random
import string
import sys
import logging
import time
from typing import final 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
    return True



def get_random_string(length):
    '''Generates a random string of the specified length
    
    Arguments:
        Length: the length of the string to generate
        
    Returns:
        A random string of the specified length
    '''

    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str

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
@allure.story('Testa o botão reject na página review-quizz')
def test_reject():
    '''Tests the reject button functionality
        
    Returns:
        True if the test passes, False otherwise
    '''

    """Next, create an instance of Chrome with the path of the driver that you downloaded through the websites of the respective browser.
    In this example, we assume that the driver is in the same directory as the Python script that you will execute."""
    driver = webdriver.Chrome() # or driver = webdriver.Chrome('./chromedriver')
    login(driver)
    goto_reviewquiz(driver)

    driver.maximize_window()
    
    #Added WebDriverWait so it can properly load the needed buttons
    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/button[2]")))
    
    # REJECT WITHOUT JUSTIFICATION
    reject_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/button[2]")
    reject_button.click()

    submit_button = driver.find_element(By.ID,"submitRQ")
    submit_button.click()
    try:

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[class="mm-popup__box"]')))
        driver.find_element(By.CSS_SELECTOR, 'button[class="mm-popup__btn mm-popup__btn--ok"]').click()

        print("Alert when submit button and no justification")
        expectedUrl="http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
            assert False, "Test Failed - Expected a different redirection when submitting quiz"
    except TimeoutException:
        print("ALERT DIDN'T SHOW UP! 1") 
        expectedUrl="http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
        assert False, "Exption timeout - Test Failed"

    box_justificacao = driver.find_element(By.ID, "justificationRQ")
    box_justificacao.send_keys(get_random_string(10))
    submit_button.click()

    try:

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[class="mm-popup__box"]')))
        driver.find_element(By.CSS_SELECTOR, 'button[class="mm-popup__btn mm-popup__btn--ok"]').click()
       
        print("Alert when submit and justification is too short")
        expectedUrl="http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
            assert False, "Test Failed - Expected a different redirection when submitting quiz"
    except TimeoutException:
        print("ALERT DIDN'T SHOW UP! 2") 
        expectedUrl="http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
        assert False, "Exption timeout - Test Failed"
    

    box_justificacao.send_keys(get_random_string(100))
    submit_button.click()
    time.sleep(3)

   
    
    expectedUrl_submitButton = "http://localhost:3000/review-quizz"
    if expectedUrl_submitButton != driver.current_url:
        print("Expected a different redirection when submitting quiz")
        print(driver.current_url)
        assert False, "Test Failed - Expected a different redirection when submitting quiz"

    driver.close()
    assert True, "Test Passed"



if __name__ == "__main__":
    pytest.main([__file__])
    