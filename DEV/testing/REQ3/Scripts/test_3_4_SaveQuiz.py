import random
import string
import sys
import allure
import pytest
import logging
import time
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
logging.basicConfig(filename="log.txt", level=logging.INFO)
os.environ['PATH'] += os.pathsep + "C:\\Users\\User\\Desktop\\ES\\webdriver" 



"""
INFO ABOUT THE BOXES
Quizz Structure:

1. Question: 20 - 140
2. Description: 0 - 512
3. 6 Options: only 1 is Correct

Question box with a mark box (to the correct one)
Only one mark box can be selected (when user selects: unmark the other)
'Submit', 'Save' and 'Cancel' button

"""



def get_random_string(length):
    
    """
        Returns a random string with the length specified by the length attribute
    """

    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str

def login(driver):

    """
        You must have already created a user with the username 'justAUSer1' and
        password 'password' so that the login is successful.

        This function starts by going to http://localhost:3000/login and maximizes the browser window.

        Waits a maximum of 5 seconds for the html element with 'fullname' id loads
        Looks for the username and password box and inserts the credentials 'justAUser1' and 'password'
        
        Finally finds the login button and presses it.
    """

    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()
    
    username = "justAUser1"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    login_button.click()
    return True

def goto_createQuiz(driver):

    """
        Waits a maximum of 5 seconds for the html element with 'links_nav' id loads

        Finds the 'Create Quiz' button and presses it.
        Then checks if the current url is the quiz creation one. If not raises an exception
    """

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "links_nav")))
    create_quiz_button = driver.find_element(By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[1]/a")
    create_quiz_button.click()

    expected_url = "http://localhost:3000/create-quizz"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Create Quiz button")
        return False
    
    return True

# def goto_mainPage(driver):
    
    """
        Waits a maximum of 5 seconds for the html element with 'links_nav' id loads

        Finds the 'QuirkedUp Softwarw' button and presses it.
    
        Then checks if the current url is the main page one. If not raises an exception
        
    """

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "links_nav")))
    main_page_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/header/nav/div[1]")
    main_page_button.click()

    expected_url = "http://localhost:3000"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from main page button")
        return False
    
    return True

@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ3')
@allure.story('Testa se guarda um teste como rascunho')
def test_save_draft():
    
    """
    This function tests whether a quiz is saved as a draft correctly

    Log in with the 'justAUser1' credentials and go to the quiz creation page (it must already be created)
    
    Tests whether a quiz is correctly saved as a draft on the home page regardless of whether it is pre-filled or not.
    
    If this happens and the page has not changed, the project passes the test successfully.
       
    """
    

    driver = webdriver.Chrome()
    login(driver)
        
    initial_elements_collums = driver.find_elements(By.XPATH, "/html/body/div/div/div/main/div[1]")
    
    goto_createQuiz(driver)

    driver.maximize_window()

    save_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[3]/div/button[2]")
    save_button.click()
    
    ok_button = driver.find_element(By.XPATH,"/html/body/div/div/article/footer/div/button[1]")
    ok_button.click()
    
    time.sleep(1)
    
    #Check if the page changed correctly
    expectedUrl="http://localhost:3000/"
    if driver.current_url != expectedUrl:
        print("ERROR: Page CHANGED")
        assert False, "ERROR: Page CHANGED"
    
    confirmation_collums = driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[1]")
          
    if initial_elements_collums == confirmation_collums:
        assert False, "ERROR: Draft not created"
        
    driver.close()
    assert True, "Test had sucess"

    

if __name__ == "__main__":
    pytest.main([__file__])

