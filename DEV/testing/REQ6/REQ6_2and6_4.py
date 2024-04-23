import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException, TimeoutException


class CreateTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/login")
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("justAUser1")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("admin123")
        submit_button = self.driver.find_element(By.ID, "login")
        submit_button.click()
        create_test_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create Test"))
        )
        create_test_link.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "test-title-box"))
        )

    def test_alert_for_insufficient_tags(self):
        driver = self.driver

        # Enter a valid title with at least 10 characters
        title_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "test-title-box"))
        )
        title_input.send_keys("Valid Title with Enough Characters")

        # Check for the presence of the tag buttons and select the correct number of tags
        tags = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "tag_button"))
        )

        required_number_of_tags = 1  # Example: if 2 tags are required
        for tag in tags[:required_number_of_tags]:
            tag.click()

        # Attempt to submit the form
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit_button"))
        )
        submit_button.click()

        # Check if alert is present after attempting to submit with insufficient tags
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            self.assertTrue("You must select 2 tags" in alert_text, "Alert with expected message is not present")
            alert.accept()  # Accept the alert
        except (NoAlertPresentException, UnexpectedAlertPresentException):
            self.fail("Expected alert not present after attempting to submit with insufficient tags.")

    def test_successful_test_creation_alert(self):
        def test_successful_test_creation_alert(self):
            driver = self.driver

            # Enter a title with the minimum required number of characters
            title_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "test-title-box"))
            )
            title_input.send_keys("Valid Title")

            # Check for the presence of the tag buttons and select the correct number of tags
            tags = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "tag_button"))
            )

            required_number_of_tags = 2  # Example: if 2 tags are required
            for tag in tags[:required_number_of_tags]:
                tag.click()

            # Attempt to submit the form
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "submit_button"))
            )
            submit_button.click()

            # Check if one of the success or failure alerts is present
            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                # Check if one of the expected messages is in the alert text
                expected_messages = ["Test created successfully!",
                                     "Cannot create test; Not enough quizzes to make a test."]
                self.assertTrue(any(msg in alert_text for msg in expected_messages),
                                "The alert text does not match any of the expected messages.")
                alert.accept()  # Accept the alert since we've verified the message

                # Wait for redirection to the homepage
                WebDriverWait(driver, 10).until(EC.url_to_be("http://127.0.0.1:3000/"))
                current_url = driver.current_url
                self.assertEqual(current_url, "http://127.0.0.1:3000/",
                                 "The browser did not redirect to the homepage after accepting the alert.")

            except TimeoutException:
                self.fail(
                    "Expected alert not present or redirection did not occur after submitting the form with valid inputs.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
