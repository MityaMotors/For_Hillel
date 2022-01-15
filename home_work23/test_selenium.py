import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Lms_Hillel_auth(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://lms.ithillel.ua/auth')
        self.driver.fullscreen_window()

    def test_entrance_with_correct_data(self):
        try:
            """Test with correct login and password"""
            driver = self.driver
            wait = WebDriverWait(driver, 5)
            input_login: WebElement = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[1]/app-login//div[1]/div/input'))
            )
            input_login.click()
            input_login.send_keys("lucavica@ukr.net")
            input_password: WebElement = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[1]/app-login//div[2]/div/input'))
            )
            input_password.click()
            input_password.send_keys("Mitya232")
            click_button: WebElement = driver.find_element(By.XPATH, "/html/body/app-root/div/app-access/div/div[1]/app-login/div/div/form/app-button/button")
            click_button.click()
            driver.execute_script("window.scrollTo(0, +1080)")

            element_exit: WebElement = wait.until(
                EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-page/div/div[2]/div/div/div/div/app-dashboard/div/div[2]/app-profile-simple/div[2]/button'))
            )
            if element_exit.is_displayed():
                print("The entrance was completed")
        except:
            raise Exception("The entrance was failed")

    def test_entrance_with_incorrect_email(self):
        try:
            """Test with incorrect login"""
            driver = self.driver
            wait = WebDriverWait(driver, 5)
            input_login: WebElement = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[1]/app-login//div[1]/div/input'))
            )
            input_login.click()
            input_login.send_keys("lucavica")
            input_login.send_keys(Keys.ENTER)
            error_message: WebElement = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[1]/app-login//form/div[2]/app-validation-messages/ul/li'))
            )
            if error_message.is_displayed():
                print("The error message is shown")
        except:
            raise Exception("The error message isn't shown")

