import sys
import unittest
import time
import logging
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import pytest
import allure
logging.basicConfig(filename="log.txt", level=logging.INFO)



lista_butoes = [
    "/html/body/div/div/div/main/main/header/nav/ul/li[1]/a/b",
    "/html/body/div/div/div/main/main/header/nav/ul/li[2]/a/b",
    "/html/body/div/div/div/main/main/header/nav/ul/li[3]/a/b",
    "/html/body/div/div/div/main/main/header/nav/ul/li[4]/a/b",
    "/html/body/div/div/div/main/main/header/nav/ul/li[5]/a/b",
    "/html/body/div/div/div/main/main/header/nav/ul/li[6]/a/b",
    "/html/body/div/div/div/main/main/header/nav/div[3]/a/img"
]

lista_links = [
    "http://localhost:3000/admin",
    "http://localhost:3000/create-quizz",
    "http://localhost:3000/review-quizz",
    "http://localhost:3000/create-test",
    "http://localhost:3000/choose-test",
    "http://localhost:3000/profile",
    "http://localhost:3000/login"
]

lista_nome = [

    "ADMIN",
    "CREATE QUIZZ",
    "REVIEW QUIZZ",
    "CREATE TEST",
    "SOLVE TEST",
    "PROFILE",
    "LOGOUT"
]

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("REQ5- Choose Test")
@allure.story("Test 5.3 - Test all 8 buttons in the Solve Test page")
def test_buttons():
    '''Test all 8 buttons in the Solve Test page
    
    Arguments:
        Driver: a Selenium WebDriver object
        
    Returns:
        The number of buttons that worked
    '''
    i = 0
    driver = webdriver.Chrome()

    choose_test(driver)
    
    login(driver)

    if goto_ChooseTest(driver) == False:
        return False

    if goto_SolveTest(driver) == False:
        return False

    driver.maximize_window()

    # Testar se o botao de logo funciona
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "logo_return_home")))
    logo_button = driver.find_element(By.ID, "logo_return_home")
    logo_button.click()

    expected_url = "http://localhost:3000/"
    current_url = driver.current_url
    if current_url != expected_url:

        print("LOGO - ❌")
        #print("Current URL is: ", current_url)

    else:
        print("LOGO - ✅")
        i += 1

    driver.back()

    for l in range(len(lista_butoes)):

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, lista_butoes[l]))).click()

        expected_url = lista_links[l]
        current_url = driver.current_url
        
        print(f'expected->{expected_url}\nreturned->{current_url}')
        if not current_url.startswith(expected_url):

            print(lista_nome[l] + " - ❌")
            #print("Current URL is: ", current_url)

        else:
            i += 1

            print(lista_nome[l]+" - ✅")

        driver.back()

    driver.close()
    if i == 8:
        assert True, "All buttons are working"
    else:
        assert False, "Some buttons are not working"


def login(driver):
    '''Logs into the website with a valid Solver account
    
    Arguments:
        Driver: a Selenium WebDriver object
    
    Returns:
        None
        
    Raises:
        Exception if the login page could not be loaded
    '''

    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser1"
    password = "admin123"

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return

# Go to the Choose Test page


def goto_ChooseTest(driver):
    '''Navigates to the Choose Test page
    
    Arguments:
        Driver: a Selenium WebDriver object
        
    Returns:
        True if the navigation was successful, False otherwise
    '''

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[5]/a/b")))
        solve_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[5]/a/b")

        solve_button.click()
    except TimeoutException:
        print("❌ Login failed")
        return False


def goto_SolveTest(driver):
    '''Checks if there are tests to solve and solves one
    
    Arguments:
        Driver: a Selenium WebDriver object
        
    Returns:
        True if a test was solved, False otherwise
    '''

    time.sleep(1)

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/main/div/div[1]"))).click()

    except TimeoutException or StaleElementReferenceException as e:

        print("❌ No tests available")

        return False

    expected_url = "http://localhost:3000/solve-test"
    current_url = driver.current_url

    if expected_url not in current_url:
        print("Expected a different redirection from Solve Test button")
        print("Current URL is: ", current_url)
        return False
    else:

        return True

#This tests needs the same prerequisite as the Test5.1 needs
# Test all 8 buttons in the solve-test page



#Melhorar com verificacoes
def choose_test(driver):
    '''Chooses a test to solve
    
    Arguments:
        Driver: a Selenium WebDriver object
        
    Returns:
        True if a test was chosen, False otherwise
    '''

    login(driver)
    
    print("Homepage - ✅")

    # find the solve test button

    goto_ChooseTest(driver)

    print("Solve_button - ✅")

    # click on the button to choose a test
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/main/div/b"))).click()
    except TimeoutException:
        print("❌ No tests available")
        return False

    expected_url = "http://localhost:3000/solve-test"
    current_url = driver.current_url

    if expected_url not in current_url:
        print("Expected a different redirection from Solve Test button")
        print("Current URL is: ", current_url)
        return False
    else:

        return True



#A alterar no futuro
if __name__ == "__main__":
    
    pytest.main([__file__])
    #test_buttons()
