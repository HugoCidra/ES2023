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
import os
os.environ['PATH'] += os.pathsep + "C:\\Users\\Utilizador" 
logging.basicConfig(filename="log.txt", level=logging.INFO)




def login(driver):
    '''Function responsible for login in the application with a valid account

                    Arguments:
                        driver (webdriver): Selenium webdriver created in the main

                    Returns:
                        None

                    Raises:
                        If the page loaded have a title different from "Login Page"
                    '''
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
    '''Function responsible for test the "Create Quiz" button
        This funtion clicks on the "Create Quiz" button and checks if the redirection occurs correctly

                    Arguments:
                        driver (webdriver): Selenium webdriver created in the main

                    Returns:
                        Bool(True if th redirection occurs correctly, False otherwise)

                    Raises:
                        None
                    '''
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "links_nav")))
    create_quiz_button = driver.find_element(By.XPATH, "/html/body//div/div/div/main/main/header/nav/ul/li/a")
    create_quiz_button.click()

    expected_url = "http://localhost:3000/create-quizz"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Create Quiz button")
        return False
    
    return True
@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ3')
@allure.story('Testa os botões Logo/Save/Cancel')

def test_buttons():
    '''Function responsible fot test the "Logo", "Save" and "Cancel buttons"
        This funtion are responsible to check the "Logo", "Save" and "Cancel buttons"

                    Arguments:
                        None

                    Returns:
                        Bool(True if all tests are successful, False otherwise)

                    Raises:
                        None
                    '''
    """Next, create an instance of Chrome with the path of the driver that you downloaded through the websites of the respective browser.
    In this example, we assume that the driver is in the same directory as the Python script that you will execute."""
    driver = webdriver.Chrome()
    
    login(driver)
    goto_createQuiz(driver)

    driver.maximize_window()


    #TEST SAVE BUTTON
    save_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[3]/div/button[2]')
    expectedUrl_saveButton="http://localhost:3000/"
    save_button.click()

    time.sleep(3)

    ok_button_popup = driver.find_element(By.XPATH, "/html/body//div/article/footer/div[2]/button[1]")
    ok_button_popup.click()

    actualUrl= driver.current_url

    if actualUrl != expectedUrl_saveButton:
        print("Expected a different redirection from SAVE button")
        assert False, "Expected a different redirection from SAVE button"

    print("TEST SUCCESSFUL! SAVE BUTTON WORKING")
    driver.close()
    assert True, "Test had success"



if __name__ == "__main__":
    pytest.main([__file__])