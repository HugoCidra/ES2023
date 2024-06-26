import random
import string
from time import sleep
import allure
import pytest
import sys
import logging
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
        You must have already created a user with the username 'justAUser1' and
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
    create_quiz_button = driver.find_element(By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a")
    create_quiz_button.click()

    expected_url = "http://localhost:3000/create-quizz"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Create Quiz button")
        return False
    
    return True

@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ3')
@allure.story('Testa a maneira correta de submeter um quiz')
def test_submit():

    """
        This function test a correct way to submit a quiz and verifys if the page it changes is the expected one (http://localhost:3000/create-quizz)


        Logs in with the credentials of 'justAUser1' and goes to the quiz creation page
        
        Fills options from 1-6 and the optional text and question boxes with random strings
        It also selects the first option as the correct one and presses submit.

        If the page isn't the expected one, the test fails
    """

    # TEST FOR INPUT BOXES
    # driver = webdriver.Chrome(ChromeDriverManager().install()) # or driver = webdriver.Chrome('./chromedriver')
    
    driver = webdriver.Chrome()
    login(driver)

    goto_createQuiz(driver)

    driver.maximize_window()

    inputboxes = driver.find_elements(By.ID,'option')

    # # Write in all boxes
    for i, box in enumerate(inputboxes):
        # Fill up with more than MAX (ERROR SHOULD APPEAR WHEN SUBMITING)
        box.send_keys("option number " + str(i))
    
    justification_box = driver.find_element(By.NAME,'justification')
    justification_box.send_keys("An amazing optional text")
    question_box = driver.find_element(By.ID,'question')
    question_box.send_keys(get_random_string(20))  
    check_button = driver.find_element(By.ID,"check")   
    check_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "react-select-3-input")))

    x = driver.find_element(By.ID, "react-select-3-input")
    x.send_keys("PPP")
    x.send_keys(Keys.ENTER)
    
    submit_button = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[3]/div/button[3]')
    submit_button.click()

    # Find pop up
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div[1]/article/div")))
    if driver.find_element(By.XPATH,"//*[@id=\"root\"]/div[1]/article/div").get_attribute("textContent") != "ERROR: Question contains misspelled words. Submit anyway?":
        assert False, "Expected a different error message when submitting quiz"

    # Clicks on the cancel button
    driver.find_element(By.XPATH,"//*[@id=\"root\"]/div[1]/article/footer/div[2]/button[2]").click()

    expectedUrl_submitButton = "http://localhost:3000/create-quizz"
    if expectedUrl_submitButton != driver.current_url:
        print("Expected a different redirection when submitting quiz")
        print(driver.current_url)
        assert False, "Expected a different redirection when submitting quiz"
    driver.close()
    assert True, "Test had success"

    
if __name__ == "__main__":
    pytest.main([__file__])
    
