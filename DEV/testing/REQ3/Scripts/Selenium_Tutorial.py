"""
FULL COMMENTED SCRIPT TO UNDERSTAND A BIT OF SELENIUM

Pre-requisites to run Selenium tests with Python

The easiest way to install Selenium on a Python environment is through the installer pip.
pip install selenium

pip install webdriver-manager for the executables to solve the problem where the Drivers aren't installed on the same Path as the scripts~

First import the WebDriver and Keys classes from Selenium.
"""
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

#Fill up Boxes for example
from selenium.webdriver.common.keys import Keys

#Used o make pauses or wait (
from selenium.webdriver.support.ui import WebDriverWait
import time 

#Helper for conditions
from selenium.webdriver.support import expected_conditions as EC

#Find elements with "BY"
from selenium.webdriver.common.by import By

"""Next, create an instance of Chrome with the path of the driver that you downloaded through the websites of the respective browser.
 In this example, we assume that the driver is in the same directory as the Python script that you will execute."""
driver = webdriver.Chrome(ChromeDriverManager().install()) # or driver = webdriver.Chrome('./chromedriver')


# .get loads a website
driver.get("http://www.python.org")
# driver.get("http://localhost:8000/") for the project

time.sleep(5)

#.title gives the textual title of the webpage (If you wish to check whether the title contains a particular substring, you can use the assert or if statements.)
print(driver.title)


"""Submit a query in the search bar. First, select the element from the HTML DOM and enter a value into it and submit the form by emulating the Return key press.
 You can select the element using its CSS class, ID, its name attribute, or even the tag name.
If you check the source of the query search bar, you notice that the name attribute of this DOM element is “q”.
 Therefore, you can use the .find_element_by_name() method as follows to select the element."""
search_bar = driver.find_element(By.NAME,"q")

#Clear search bar and send an input
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

#URL that should appear
expectedUrl="https://www.python.org/search/?q=getting+started+with+python&submit="

#Get current url after search 
actualUrl= driver.current_url

print(driver.current_url)


assert expectedUrl == actualUrl,"url is wrong"


#driver.switch_to("http://www.python.org")
#print(driver.window_handles)

driver.close()