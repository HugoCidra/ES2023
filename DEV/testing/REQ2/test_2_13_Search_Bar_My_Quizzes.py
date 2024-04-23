import re
import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(filename="log.txt", level=logging.INFO)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def login(driver):
    """Function responsible for login in the application with a valid account

    Arguments:
        driver (webdriver): Selenium webdriver created in the main

    Returns:
        None

    Raises:
        If the page loaded have a title difrent from "Login Page"
    """

    driver.get("http://localhost:3000/login")

    if not "Login" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser1"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("REQ2")
@allure.story("Testar a search bar do Hall of Fame")
def test_halloffame_searchbars(driver):
    ##########
    # TESTE 1 -> testar se a search bar funciona (input = marketed, deve devolver 1 quiz: "The individual who uses the product after it has been fully developed and marketed is called:")

    login(driver)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "my-quizzes-search-bar input.SearchBar_input")
        )
    )
    search_bar = driver.find_element(
        By.CLASS_NAME, "my-quizzes-search-bar input.SearchBar_input"
    )
    search_bar.send_keys("marketed")

    filtered_quiz = [
        "The individual who uses the product after it has been fully developed and marketed is called:"
    ]

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Quiz_card"))
    )

    my_quizzes_field = driver.find_element(By.CLASS_NAME, "MyQuizzes_field")
    columns = my_quizzes_field.find_elements(By.XPATH, "./*")
    # Initialize an empty list to store the QuizCards
    quiz_cards = []

    # Iterate over each column
    for column in columns:
        # Find all the QuizCards within the column
        cards = column.find_elements(By.CLASS_NAME, "Quiz_card")
        # Add the QuizCards to the list
        quiz_cards.extend(cards)

    # Assuming 'quiz_cards' is your list of WebElement objects representing the cards
    for card in quiz_cards:
        # Find the question element within the card
        question_element = card.find_element(By.CLASS_NAME, "MyQuizzes_quiz")
        # Print the text of the question

    # Check if the question is in the list of filtered quizzes
    if question_element.text in filtered_quiz:
        # assert that the test passed
        assert True, "Test passed"
    else:
        assert False, "Test failed"

    ##########
    # TESTE 1 -> testar se a search bar funciona (input = 'waterfall', não deve devolver o quiz: "The individual who uses the product after it has been fully developed and marketed is called:")
    i = 0
    login(driver)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "my-quizzes-search-bar input.SearchBar_input")
        )
    )
    search_bar = driver.find_element(
        By.CLASS_NAME, "my-quizzes-search-bar input.SearchBar_input"
    )
    search_bar.send_keys("waterfall")

    filtered_quiz = [
        "The individual who uses the product after it has been fully developed and marketed is called:"
    ]

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Quiz_card"))
    )

    my_quizzes_field = driver.find_element(By.CLASS_NAME, "MyQuizzes_field")
    columns = my_quizzes_field.find_elements(By.XPATH, "./*")
    # Initialize an empty list to store the QuizCards
    quiz_cards = []

    # Iterate over each column
    for column in columns:
        # Find all the QuizCards within the column
        cards = column.find_elements(By.CLASS_NAME, "Quiz_card")
        # Add the QuizCards to the list
        quiz_cards.extend(cards)

    # Assuming 'quiz_cards' is your list of WebElement objects representing the cards
    for card in quiz_cards:
        # Find the question element within the card
        question_element = card.find_element(By.CLASS_NAME, "MyQuizzes_quiz")
        # Print the text of the question
        if filtered_quiz[0] == question_element.text:
            i += 1

        if i == 0:
            assert True, "Test passed"
        else:
            assert False, "Test failed"

    # Close the driver
    driver.quit()
