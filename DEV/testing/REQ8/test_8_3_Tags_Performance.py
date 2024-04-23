import time
from selenium.common.exceptions import TimeoutException

import logging
from typing import final 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import allure
logging.basicConfig(filename="log.txt", level=logging.INFO)

logging.basicConfig(filename="log.txt", level=logging.INFO)

def login(driver,username,password):
    '''Function responsible for login in the application with a valid account
    
    Arguments:
        driver (webdriver): Selenium webdriver created in the function test_username()

    Returns:
        Username
    '''
    driver.get("http://localhost:3000/login")
    driver.maximize_window()

    
    

    try:
    
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys(username)

       
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        driver.find_element(By.ID, "password").send_keys(password)

        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        login_button = driver.find_element(By.ID, "login")
        login_button.click()

        

        return username
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        raise
    except TimeoutException as e:
        print(f"Timeout while waiting for element: {e}")
        raise



def goto_Profile(driver):
    '''Function responsible for going to the Profile page from Home page.

    Arguments:
        driver (webdriver): Selenium webdriver created in the function test_username().
    
    Returns:
        True if the redirection is correct, False otherwise.
    '''
    try:
        
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"menuButton")))
        menu_button = driver.find_element(By.ID, "menuButton")
        menu_button.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ProfileButton")))
        profile_button = driver.find_element(By.ID, "ProfileButton") 
        profile_button.click()

       
        expected_url = "http://localhost:3000/profile"
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))

        return True
    except TimeoutException:
        print("Failed to navigate to the profile page or the page did not load in time.")
        return False


    

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("REQ8")
@allure.story("Pagina de perfil")

def test_profile_performance_solver():
    driver = webdriver.Chrome()
    driver.maximize_window()  
    try:
        user = login(driver, 'justAUser1', 'admin123')
        assert goto_Profile(driver), "Redirection to Profile page failed"
        
        wait = WebDriverWait(driver, 30)
        
        # Encontrar todos os containers de gráficos e títulos
        graph_containers = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "recharts-responsive-container"))
        )
        title_elements = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "quiz-flag"))
        )
        
        # Verifica se existem dois gráficos e dois títulos
        assert len(graph_containers) == 2, "Quantidade de gráficos esperada não encontrada."
        assert len(title_elements) == 2, "Quantidade de títulos esperada não encontrada."

        # Verifica os títulos dos gráficos
        expected_titles = ["Quizzes", "Answers"]
        for i, title in enumerate(expected_titles):
            title_text = title_elements[i].text
            assert title_text == expected_titles[i], f"Título do gráfico incorreto, esperado: {expected_titles[i]}, obtido: {title_text}"
        
        # Verifica as tags em cada gráfico
        for i, container in enumerate(graph_containers):
            # Encontrar todas as tags para o gráfico atual
            axis_ticks = container.find_element(By.CLASS_NAME, 'recharts-cartesian-axis-ticks')
            axis_tick_layers = axis_ticks.find_elements(By.CLASS_NAME, 'recharts-cartesian-axis-tick')
            number_of_tick_layers = len(axis_tick_layers)
            print(f'Número de tags no eixo do gráfico {i+1}:', number_of_tick_layers)

            # Verifica cada tag para presença e visibilidade
            for tick_element in axis_tick_layers:
                tick_text = tick_element.text
                print(tick_text)
                assert tick_text, "Uma tag está vazia."
                assert tick_element.is_displayed(), "Uma tag não está visível."

    except TimeoutException as e:
        print(f"Timeout while waiting for element: {e}")
        raise
    finally:
        driver.quit()





def test_profile_performance_solver_no_tests():
    driver = webdriver.Chrome()
    driver.maximize_window()  
    try:
        user = login(driver, 'justAUser2', 'admin123')
        assert goto_Profile(driver), "Redirection to Profile page failed"
        
        wait = WebDriverWait(driver, 10)
        
        # Encontrar todos os containers de gráficos e títulos
        graph_containers = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "recharts-responsive-container"))
        )
        title_elements = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "quiz-flag"))
        )
        message = wait.until(EC.presence_of_element_located((By.ID,"profile_msg")))
        content = message.text
        expected_text = 'You have not solved any tests yet!'
        assert content != expected_text, f"Wrong message received, it should be: {expected_text}"
        
        # Verifica se existe um gráfico e apenas um título
        assert len(graph_containers) == 1, "Quantidade de gráficos esperada não encontrada."
        assert len(title_elements) == 1, "Quantidade de títulos esperada não encontrada."



        # Verifica os títulos dos gráficos
        expected_titles = ["Quizzes"]
        for i, title in enumerate(expected_titles):
            title_text = title_elements[i].text
            assert title_text == expected_titles[i], f"Título do gráfico incorreto, esperado: {expected_titles[i]}, obtido: {title_text}"
        
        # Verifica as tags em cada gráfico
        for i, container in enumerate(graph_containers):
            # Encontrar todas as tags para o gráfico atual
            axis_ticks = container.find_element(By.CLASS_NAME, 'recharts-cartesian-axis-ticks')
            axis_tick_layers = axis_ticks.find_elements(By.CLASS_NAME, 'recharts-cartesian-axis-tick')
            number_of_tick_layers = len(axis_tick_layers)
            print(f'Número de tags no eixo do gráfico {i+1}:', number_of_tick_layers)

            # Verifica cada tag para presença e visibilidade
            for tick_element in axis_tick_layers:
                tick_text = tick_element.text
                print(tick_text)
                assert tick_text, "Uma tag está vazia."
                assert tick_element.is_displayed(), "Uma tag não está visível."

    except TimeoutException as e:
        print(f"Timeout while waiting for element: {e}")
        raise
    finally:
        driver.quit()

def test_profile_performance_creator():
    driver = webdriver.Chrome()
    driver.maximize_window()  
    try:
        user = login(driver, 'justAUser4', 'admin123')
        assert goto_Profile(driver), "Redirection to Profile page failed"
        
        wait = WebDriverWait(driver, 30)
        
        # Encontrar todos os containers de gráficos e títulos
        graph_containers = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "recharts-responsive-container"))
        )
        title_elements = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "quiz-flag"))
        )
        
        # Verifica se existe só um gráfico e um título
        assert len(graph_containers) == 1, "Quantidade de gráficos esperada não encontrada."
        assert len(title_elements) == 1, "Quantidade de títulos esperada não encontrada."

        # Verifica os títulos dos gráficos
        expected_titles = ["Quizzes"]
        for i, title in enumerate(expected_titles):
            title_text = title_elements[i].text
            assert title_text == expected_titles[i], f"Título do gráfico incorreto, esperado: {expected_titles[i]}, obtido: {title_text}"
        
        # Verifica as tags em cada gráfico
        for i, container in enumerate(graph_containers):
            # Encontrar todas as tags para o gráfico atual
            axis_ticks = container.find_element(By.CLASS_NAME, 'recharts-cartesian-axis-ticks')
            axis_tick_layers = axis_ticks.find_elements(By.CLASS_NAME, 'recharts-cartesian-axis-tick')
            number_of_tick_layers = len(axis_tick_layers)
            print(f'Número de tags no eixo do gráfico {i+1}:', number_of_tick_layers)

            # Verifica cada tag para presença e visibilidade
            for tick_element in axis_tick_layers:
                tick_text = tick_element.text
                print(tick_text)
                assert tick_text, "Uma tag está vazia."
                assert tick_element.is_displayed(), "Uma tag não está visível."

    except TimeoutException as e:
        print(f"Timeout while waiting for element: {e}")
        raise
    finally:
        driver.quit()

def test_profile_performance_creator_no_quizzes():
    driver = webdriver.Chrome()
    driver.maximize_window()  
    try:
        user = login(driver, 'justAUser5', 'admin123')
        assert goto_Profile(driver), "Redirection to Profile page failed"
        
        wait = WebDriverWait(driver, 10)
        
        message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "caixa-texto")))
        content = message.text.strip()
        expected_text = 'You do not have approved or not approved quizzes!'

        if content != expected_text:
            assert False,f"Wrong message received: {content}, it should be: {expected_text}"


    except TimeoutException as e:
        print(f"Timeout while waiting for element: {e}")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
