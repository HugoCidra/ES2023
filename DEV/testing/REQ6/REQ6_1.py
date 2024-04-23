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

    def test_create_test_page_elements(self):
        driver = self.driver

        # Check if the Title box is present
        title_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "test-title-box"))
        )
        self.assertIsNotNone(title_input)

        # Check for the presence of all 12 tags
        tags = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "tag_button"))
        )
        self.assertEqual(len(tags), 12, "Not all tags are present")

        # Attempt to select the first three tags
        for tag in tags[:3]:
            tag.click()

        # Check if alert is present after attempting to select three tags
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            self.assertTrue("You must select 2 tags." in alert_text, "Alert with expected message is not present")
            alert.accept()  # Accept the alert
        except (NoAlertPresentException, UnexpectedAlertPresentException):
            self.fail("Expected alert not present after clicking tags.")

        # Locate the 'SUBMIT' button by its class name
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit_button"))
        )
        self.assertIsNotNone(submit_button, "Submit button not found")

        # Locate the 'CANCEL' button by its class name
        cancel_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cancel_button"))
        )
        self.assertIsNotNone(cancel_button, "Cancel button not found")





    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)



