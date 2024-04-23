# Selenium for Python Documentation

## Table of Contents

- [Selenium for Python Documentation](#selenium-for-python-documentation)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
    - [Python Installation](#python-installation)
    - [Selenium Installation](#selenium-installation)
    - [Web Drivers](#web-drivers)
  - [Setting Up Web Drivers](#setting-up-web-drivers)
    - [Chrome WebDriver](#chrome-webdriver)
    - [Firefox WebDriver](#firefox-webdriver)
  - [Basic Selenium Operations](#basic-selenium-operations)
    - [Initializing WebDriver](#initializing-webdriver)
    - [Navigating to a URL](#navigating-to-a-url)
    - [Locating Elements Using By Class Methods](#locating-elements-using-by-class-methods)
    - [Interacting with Elements](#interacting-with-elements)
    - [Handling Alerts](#handling-alerts)
    - [Closing WebDriver](#closing-webdriver)

---

## Prerequisites

### Python Installation

Selenium for Python requires Python to be installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

To verify your Python installation and version, open a terminal and run:

```bash
python --version
```

### Selenium Installation

Install Selenium using pip, the Python package manager:

```bash
pip install selenium
```

### Web Drivers

Selenium interacts with web browsers using web drivers. You need to download the appropriate driver for the browser you want to automate. The most commonly used drivers are:

- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver)

Download the driver that matches your **browser version** and operating system. Ensure the driver is in your system's PATH.

If you dont wish to add the webdriver path to your PATH environment variable you can add it temporarily in the beggining of your Selenium programs by doing:

```python
import os
os.environ['PATH'] += <path> # Replace path with the path to your webdriver
```


> To see the version of your Chrome browser open it and go to chrome://version the first line should provide the information you need:
> e.g. 117.0.5938.134 (Compilação oficial) (64 bits) (cohort: Stable) 

> In case of Firefox you should be able to see the version by going to the application menu (click the 3 horizontal lines located on the top right corner of your screen). Then click on 'help' and then 'About Firefox'. Your first line should look like this: 118.0.1 (64-bit) 


---

## Setting Up Web Drivers

### Chrome WebDriver

1. Download ChromeDriver: Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/) and download the version compatible with your Chrome browser.

2. Place the `chromedriver` executable in a directory that is in your system's PATH.

### Firefox WebDriver

1. Download GeckoDriver: Visit the [GeckoDriver download page](https://github.com/mozilla/geckodriver/releases) and download the version compatible with your Firefox browser.

2. Place the `geckodriver` executable in a directory that is in your system's PATH.

---

## Basic Selenium Operations

### Initializing WebDriver

To start using Selenium, you need to create a WebDriver instance for your chosen browser. Here's how to initialize it for Chrome:

```python
from selenium import webdriver

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
```

### Navigating to a URL

You can navigate to a URL using the `get` method:

```python
# Navigate to a URL
driver.get("https://example.com")
```

### Locating Elements Using By Class Methods

The `By` class in Selenium provides a standardized way to locate elements based on various criteria. You can use these methods with the `find_element` function to locate elements in a more structured manner.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to a web page
driver.get("https://example.com")

# Locate an element by its ID
element_by_id = driver.find_element(By.ID, "element_id")

# Locate an element by its name
element_by_name = driver.find_element(By.NAME, "element_name")

# Locate an element by XPath
element_by_xpath = driver.find_element(By.XPATH, "//div[@class='example']")

# Locate an element by CSS selector
element_by_css_selector = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
```

- `By.ID`: Locates an element using its unique id attribute.
- `By.NAME`: Locates an element using its name attribute.
- `By.XPATH`: Locates an element using an XPath expression.
- `By.CSS_SELECTOR`: Locates an element using a CSS selector.

Using the `By` class methods provides a clear and consistent way to locate elements in different ways, making your code more readable and maintainable.

### Interacting with Elements

You can interact with elements by performing actions like clicking, typing, or extracting text:

```python
# Keys allows you to send special keys like ENTER and TAB
from selenium.webdriver.common.keys import Keys

# Click an element
element.click()

# Type text into an input field
element.send_keys("Hello, World!")

# Send the special key ENTER
element.send_keys(Keys.ENTER)

# Extract text from an element
text = element.text
```

### Handling Alerts

You can handle JavaScript alerts, confirms, and prompts using the `Alert` class:

```python
from selenium.webdriver.common.alert import Alert

# Accept an alert
alert = Alert(driver)
alert.accept()
```

### Closing WebDriver

Don't forget to close the WebDriver when you're done:

```python
# Close the WebDriver
driver.quit()
```

This documentation covers the basics of setting up Selenium for Python and performing common operations. For more advanced usage and detailed documentation, refer to the official Selenium documentation and browser-specific documentation.

Happy Selenium automation! 🚀
