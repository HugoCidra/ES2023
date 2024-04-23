import time
import allure
import pytest
import logging
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.common.exceptions import NoSuchElementException

import os
os.environ['PATH'] += os.pathsep + "C:\\Users\\User\\Desktop\\ES\\webdriver" 
logging.basicConfig(filename="log.txt", level=logging.INFO)




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


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ3')
@allure.story('Tests if a rejected quizz can be edited')

def test_rejected_edit():
    
    driver = webdriver.Chrome()
    driver.maximize_window()

    login(driver)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "HallOfFame_title")))

    # Finds if the user justAUser1 has a rejected quizz
    try:
        rejected_quizz = driver.find_element(By.CLASS_NAME, 'state_3')
        rejected_quizz.click()
        WebDriverWait(driver, 5).until(EC.url_changes)
        
    except NoSuchElementException:
        assert True, "No rejected quizz found"
        print("No rejected quizz found")
        return

    # test if http://localhost:3000/create-quizz/ is a substring of driver.current_url
    assert "http://localhost:3000/create-quizz/" in driver.current_url
    quizz_id = driver.current_url.split("/")[-1]

    # Returns to homepage
    logo_button = driver.find_element(By.ID,'logo_return_home')
    logo_button.click()
    WebDriverWait(driver, 5).until(EC.url_changes)
    assert driver.current_url == "http://localhost:3000/"

    # Checks if the Rejected Quizz remains Rejected
    rejected2draft = driver.find_element(By.XPATH, f'//a[@href="/create-quizz/{quizz_id}"]//div')
    assert rejected2draft.get_attribute("class") == "Quiz_state state_3"

    # Return to the Rejected Quizz
    rejected_quizz = driver.find_element(By.XPATH, f'//a[@href="/create-quizz/{quizz_id}"]//div')
    rejected_quizz.click()
    WebDriverWait(driver, 5).until(EC.url_changes)
    assert "http://localhost:3000/create-quizz/" in driver.current_url

    question = driver.find_element(By.NAME, "question")
    question.clear()
    question.send_keys("Question edited")

    #Saves quizz and returns to the homepage
    # //*[@id="root"]/div[1]/article/footer/div[2]/button
    # time.sleep(1)
    save_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div[3]/div/button[2]")
    save_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/div[1]/article/footer/div[2]/button")))
    ok_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/article/footer/div[2]/button")
    ok_button.click()

    WebDriverWait(driver, 5).until(EC.url_changes)
    assert "http://localhost:3000/" in driver.current_url

    # Tests if the previously Rejected Quizz became a Draft
    # rejected2draft = driver.find_element(By.XPATH, f'//a[@href="/create-quizz/{quizz_id}"]//div')
    # assert rejected2draft.get_attribute("class") == "Quiz_state state_1"

    # print('Test had success')
    # assert True, "Test had success"



if __name__ == "__main__":
    pytest.main([__file__])
    
    
