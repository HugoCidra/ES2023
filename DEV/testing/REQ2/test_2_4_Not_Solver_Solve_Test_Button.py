import sys
import allure
import pytest
import time
import logging
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
os.environ['PATH'] += os.pathsep + "C:\\Users\\User\\Desktop\\ES\\webdriver" 
logging.basicConfig(filename="log.txt", level=logging.INFO)

#Melhorar com verificacoes
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

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser3"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    
@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ2')
@allure.story('Testa o Butão Solv test - Not Solver')
def test_solve_test():
    '''
    Function to test the "Solve Test" button functionality for non-solver users

    This function navigates to the "Solve Test" page, checks if the alert message matches the expected message,
    accepts the alert, and checks if the URL matches the expected URL after the alert

    Arguments:
        driver (webdriver): Selenium webdriver created in the main

    Returns:
        int: 2 if the test is successful (alert message and URL match the expected values), 0 otherwise

    Raises:
        None
    '''
    driver = webdriver.Chrome()

    login(driver)

    i = 0
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"links_nav\"]/li[4]/a")))

    solve_button = driver.find_element(By.XPATH, "//*[@id=\"links_nav\"]/li[4]/a")

    solve_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/div[1]/article/div")))
    popup = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/article/div")
    msg = popup.text
    # alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    # msg = alert.text

    if msg == "Must be a Solver":
        i+=1
    
    # alert.accept()

    expected_url = "http://localhost:3000/"
    current_url = driver.current_url

    if current_url == expected_url:
        i+=1

    driver.close()

    if i == 2:
        assert True, "Test passed"
    else:
        assert False, "Test failed"
    

#PATH = "C:\Program Files (x86)\Chromedriver.exe"

if __name__ == "__main__":
    pytest.main([__file__])
