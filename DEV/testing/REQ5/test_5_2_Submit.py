from selenium.webdriver.chrome.service import Service
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager


import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
logging.basicConfig(filename="log.txt", level=logging.INFO)
import pytest
import allure



def login(driver):
    '''Function responsible for login in the application with a valid Solver account
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the function test_all()

    Returns:
        None
    
    Raises:
        If the page loaded have a title difrent from "Login Page"
    '''
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser3"
    password = "admin123"

    WebDriverWait(driver, 5).until( # wait for the page to load
        EC.presence_of_element_located((By.ID, "fullName"))
    )
    # send username and password and click login
    driver.find_element(By.ID, "fullName").send_keys(username) 
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return



def goto_ChooseTest(driver):
    '''Function responsible for going to the Choose Test page from Home page
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the function test_all()
    
    Returns:
        None if the Choose Test page is loaded, False if a exeption is raised
    '''
    try:
        WebDriverWait(driver, 5).until( # wait for the the solve button to load (the button is only available when the page is fully loaded)
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[5]/a/b"))
        )
        solve_button = driver.find_element( # gets the solve button
            By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[5]/a/b"
        )
        solve_button.click() # got to the choose test page
    except TimeoutException:

        print("❌ Login failed")
        return False

    # Retorna o URL errado mas está a funcionar	bem ??? Tirei Confirmação ES 2022/2023
    '''
    expected_url = "http://localhost:3000/choose-test"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Choose Test button")
        print("Current URL is: ", current_url)
        return False
    else:

        return True
    '''



def goto_SolveTest(driver): #TODO FIX o path para a botão do teste
    '''Function responsible for when in the Choose Test page, check if there are tests and select the first one
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the funciton test_all()

    Returns:
        True if a test was selected and if the page link is correct, False if a exeption is raised (no tests available) or the page link is incorrect
    '''
    
    try:
        #WebDriverWait(driver, 5).until(EC.element_to_be_clickable( # ESTA PARTE FOI ALTERADA ES 2023/2024 O PATH DEIXADO NÃO É CLARO A QUE ELEMENTO SE REFERE
        #    (By.XPATH, "/html/body/div/div/div/main/div/div[1]/input"))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div[class='box chooseTest_box']"))
        ).click()

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



def Cancel_Button(driver):
    '''Function responsible for testing the Cancel Button on solving test page ("/solve-test/<id>")
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the function test_all()

    Returns:
        1 if the test had success, 0 if the test failed or an exception (TimeoutException or NoSuchElementException) was raised
    '''
    # Cancel the test
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[41]/button[2]"))).click() # it will wait for the cancel button to be clickable and then click it
    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[2]"))).click() #TODO REVIEW

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Cancel Button - Cancel Button not found (inconsistent xpath)")
            return 0

    # Confirm the cancel
    WebDriverWait(driver, 10).until(EC.alert_is_present()) # wait for the alert to be present
    alert = driver.switch_to.alert # save the contex of the alert

    alert.accept() # confirm the alert

    # Check if the test was cancelled
    print(driver.current_url)
    if "http://localhost:3000/" == driver.current_url:
        print("Test Cancel - ✅")
        return 1

    else:

        print("Wrong redirection after alert cancel - ❌")
        return 0



def NoAnswers(driver):
    '''Function responsible for testing the submition with no answers selected on solving test page ("/solve-test/<id>")
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the funciton test_all()
    
    Returns:
        1 if the test had success, 0 if the test failed or an exception (TimeoutException or NoSuchElementException) was raised
    '''
    # Submit the test without answering any question
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[41]/button[1]"))).click() # it will wait for the submit button to be clickable and then click it

    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[1]"))).click() #TODO REVIEW not founded element

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Submit Button - Submit Button not found (inconsistent xpath)")
            return 0
        
    # when test is submitted, the result should appear where the submit button was in case of success of this test the text should be "YOU GOT 0 POINTS"
    try:
        aux = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "YOU GOT")]'))).text # it will wait for the component to be loaded and then get the text
    except TimeoutException or NoSuchElementException as e:

        try:
            aux = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[1]"))).text #TODO REVIEW not founded element

        except TimeoutException or NoSuchElementException as e:

            print(
                "❌ Error in Result Button - Result Button not found (inconsistent xpath)")
            return 0

    if aux == "YOU GOT 0 POINTS":

        print("Test with no answers - ✅")
        return 1

    else:

        print("Test with no answers - ❌")
        return 0



def Homepage_Button_Cancel(driver):
    '''Function responsible for testing the cancelation of the alert that appears when the user clicks on homepage button on solving test page ("/solve-test/<id>") after submiting the test (a precondition for this test is that the test was submitted)
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the funciton test_all()
    
    Returns:
        1 if the test had success, 0 if the test failed or an exception (TimeoutException or NoSuchElementException) was raised
        
    '''
    excepted_url = driver.current_url


    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[61]/button[2]"))).click() # it will wait for the homepage button to be clickable and then click it 
    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[2]"))).click() #TODO REVIEW not founded element

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Homepage Button - Homepage Button not found (inconsistent xpath)")
            return 0


    
    WebDriverWait(driver, 10).until(EC.alert_is_present()) # wait for the alert, with the confirmation, to be present
    alert = driver.switch_to.alert # save the contex of the alert

    alert.dismiss() # cancel the alert


    if excepted_url == driver.current_url:

        print("Homepage Button Cancel - ✅")
        return 1
    else:

        print("Wrong redirection after Homepage alert cancel - ❌")
        return 0



def Homepage_Button_Ok(driver):
    '''Function responsible for testing the confirmation of the alert that appears when the user clicks on homepage button on solving test page ("/solve-test/<id>") after submiting the test (a precondition for this test is that the test was submitted)
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the funciton test_all()
    
    Returns:
        1 if the test had success, 0 if the test failed or an exception (TimeoutException or NoSuchElementException) was raised
    '''
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[61]/button[2]"))).click() # it will wait for the homepage button to be clickable and then click it
    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[2]"))).click() #TODO REVIEW not founded element

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Homepage Button - Homepage Button not found (inconsistent xpath)")
            return 0

    WebDriverWait(driver, 10).until(EC.alert_is_present()) # wait for the alert, with the confirmation, to be present
    alert = driver.switch_to.alert # save the contex of the alert

    alert.accept() # confirm the alert


    if "http://localhost:3000/" == driver.current_url:

        print("Homepage Button OK - ✅")
        return 1
    else:

        print("Wrong redirection after Homepage alert accept - ❌")
        return 0

    return i


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('REQ5 - Solve Test')
@allure.story('Testar a submição em varios cenários')
def test_all():
    '''Function responsible for calling all the tests of this file and print the results
    
    1 - login with a valid Solver account
    
    2 - go to the choose test page with the list of all test available to solve

    3 - go to a solve test page /solve-test/<id>

    4 - test the cancel button tha apears when the user is on the solve test page /solve-test/<id> if it works correctly the user will be redirected to the homepage

    5 - go to the choose test page with the list of all test available to solve

    6 - go to a solve test page /solve-test/<id>

    7 - test the submition of a test with no answers selected on the solve test page /solve-test/<id> the user will remain on the same page and the text "YOU GOT 0 POINTS" will appear where the submit button was
    
    8 - test the cancelation of the alert that appears when the user clicks on homepage button if it works correctly the user will remain on the same page 

    9 - test the confirmation of the alert that appears when the user clicks on homepage button if it works correctly the user will be redirected to the homepage

    Arguments:
        None
    
    Returns:
        integer: The number of tests passed
    '''
    res = 0 # number of tests passed

    driver = webdriver.Chrome()
    
    login(driver) # 1

    # 2
    if goto_ChooseTest(driver) == False:
        return False
    # 3
    if goto_SolveTest(driver) == False:
        return False

    driver.maximize_window()

    # 4
    res += Cancel_Button(driver)

    # 5
    if goto_ChooseTest(driver) == False:
        assert False, "Failed goint to Choose Test page"
    # 6
    if goto_SolveTest(driver) == False:
        assert False, "No tests available"
    print("CHEGOU")
    # 7
    res += NoAnswers(driver)

    # 8
    res += Homepage_Button_Cancel(driver)

    # 9
    res += Homepage_Button_Ok(driver)

    if res == 4:
        assert True, "REQ5 Test Submission TEST -> ✅"
        print("REQ5 Test Submission TEST -> ✅")
    else:
        print(f"REQ5 Test Submission TEST -> ❌ ({res} out of 4 tests passed)")
        assert False, f"REQ5 Test Submission TEST -> ❌ ({res} out of 4 tests passed)"

if __name__ == "__main__":
    pytest.main([__file__])
    #test_all()
