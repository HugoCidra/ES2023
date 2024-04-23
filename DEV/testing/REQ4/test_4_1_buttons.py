import time
import logging
from typing import final 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
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
    time.sleep(2)

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser2"
    password = "admin123"

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
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
@allure.story('Testa os botões logo e cancel da página de revisão de um quiz')
def test_buttons():
    '''Runs a test of the LOGO and CANCEL buttons
    
    Returns:
        True if test passes, False otherwise
    '''
    
    """Next, create an instance of Chrome with the path of the driver that you downloaded through the websites of the respective browser.
    In this example, we assume that the driver is in the same directory as the Python script that you will execute."""
    driver = webdriver.Chrome() # or driver = webdriver.Chrome('./chromedriver')
    login(driver)
    goto_reviewquiz(driver)

    driver.maximize_window()


    #TEST LOGO BUTTON
    #Easy way to find buttons 
    
    logo_button = driver.find_element(By.ID,'logo_return_home')
    expectedUrl_logoButton="http://localhost:3000/"
    logo_button.click()

    actualUrl= driver.current_url
    if actualUrl != expectedUrl_logoButton:
        print("Expected a different redirection from LOGO button")
        assert False, "Expected a different redirection from LOGO button"
    
    driver.back()
    

    goto_reviewquiz(driver)
    time.sleep(0.5)
    cancel_button = driver.find_element(By.ID, "cancelRQ")
    cancel_button.click()

    expectedUrl_cancelButton="http://localhost:3000/"
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[class="mm-popup__box"]')))
        driver.find_element(By.CSS_SELECTOR, 'button[class="mm-popup__btn null"]').click()

        print("Alert accepted")
        if driver.current_url != expectedUrl_cancelButton:
            assert False, "Test Failed - Expected a different redirection when canceling review"
    except TimeoutException:
        print("ALERT DIDN'T SHOW UP!") 
        if driver.current_url != expectedUrl_cancelButton:
            print("ERROR: Page CHANGED")
        assert False, "Exption timeout - Test Failed"
    actualUrl= driver.current_url
    if expectedUrl_cancelButton != actualUrl:
        print("Expected a different redirection from Cancel button")
        assert False, "Expected a different redirection from Cancel button"
    driver.back()


    print("TEST SUCCESSFUL! ALL BUTTONS WORKING")
    driver.close()
    assert True, "Test had sucess"


if __name__ == "__main__":
    #pytest.main([__file__])
    test_buttons()