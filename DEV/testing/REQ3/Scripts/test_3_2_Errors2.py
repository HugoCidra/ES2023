import random
import string
import sys
import allure
import pytest
import logging
from typing import final 
from selenium import webdriver
from time import sleep
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

@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ3')
@allure.story('Testa se aparece um alerta quando não é selecionado nenhuma resposta correta ao criar um quiz')

def test_errors2():

    """
       This function tests if a alert is produced when no correct ansewr is selected when creating a quiz

       Logs in with the credentials of 'justAUser1' and goes to the quiz creation page (must be already created)

       Fills options from 1-6, then the question box and finally the
       optional text box (not the justification boxes beneath the option ones)

       Then tests if a alert is produced when clicking in submit without chosing a correct ansewr.
       If it does and the page didn't change, then the project passes the test successfully.
    """


    # TEST FOR INPUT BOXES
    # driver = webdriver.Chrome(ChromeDriverManager().install()) # or driver = webdriver.Chrome('./chromedriver')

    aux = 0
    
    driver = webdriver.Chrome()
    login(driver)
    goto_createQuiz(driver)

    driver.maximize_window()

    # GET ALL OPTION INPUT BOXES
    inputboxes  = driver.find_elements(By.ID,'option')
    question_box = driver.find_element(By.ID,'question')
    justification_box = driver.find_element(By.NAME,'justification')


    # Write in all boxes
    for box in inputboxes:
        # Fill up with more than MAX (ERROR SHOULD APPEAR WHEN SUBMITING)
        box.send_keys(get_random_string(513))
    question_box.send_keys(get_random_string(141))
    justification_box.send_keys(get_random_string(513))


    submit_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[3]/div/button[3]")
    submit_button.click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[class="mm-popup__box"]')))

    text_popup = driver.find_element(By.CSS_SELECTOR, "div[class='mm-popup__box__body']").text

    driver.find_element(By.CSS_SELECTOR, 'button[class="mm-popup__btn mm-popup__btn--ok"]').click()

    if "ERROR: You have to choose a unique correct option" in text_popup:
        aux = 1


    driver.close()
    if aux == 1:
        assert True, "Test had sucess"
    else:
        assert False, "Test had failed"

    
if __name__ == "__main__":
    pytest.main([__file__])   
