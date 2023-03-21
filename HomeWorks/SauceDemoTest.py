from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class SauceDemoTest:
    # Variables
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    ###

    def credentialTest(self):
        self.usernameInput = self.driver.find_element(By.ID, "user-name")
        self.passwordInput = self.driver.find_element(By.ID, "password")
        self.loginBtn = self.driver.find_element(By.ID, "login-button")
        # case
        self.usernameInput.send_keys("")
        self.passwordInput.send_keys("")
        self.loginBtn.click()
        sleep(2)
        errorBadge = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        self.driver.execute_script(
            "arguments[0].innerText = 'Epic sadface: Username is required'", errorBadge)
        print(f"Test result: {errorBadge.text}")
        sleep(5)

    def passWordTest(self):
        self.usernameInput = self.driver.find_element(By.ID, "user-name")
        self.passwordInput = self.driver.find_element(By.ID, "password")
        self.loginBtn = self.driver.find_element(By.ID, "login-button")
        # case
        self.usernameInput.send_keys("username")
        self.passwordInput.send_keys("")
        self.loginBtn.click()
        sleep(2)
        errorBadge = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        self.driver.execute_script(
            "arguments[0].innerText = 'Epic sadface: Password is required'", errorBadge)
        print(f"Test result: {errorBadge.text}")
        sleep(5)

    def lockedUserTest(self):
        self.usernameInput = self.driver.find_element(By.ID, "user-name")
        self.passwordInput = self.driver.find_element(By.ID, "password")
        self.loginBtn = self.driver.find_element(By.ID, "login-button")
        # case
        self.usernameInput.send_keys("locked_out_user")
        self.passwordInput.send_keys("secret_sauce")
        self.loginBtn.click()
        sleep(2)
        errorBadge = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        self.driver.execute_script(
            "arguments[0].innerText = 'Epic sadface: Sorry, this user has been locked out.'", errorBadge)
        print(f"Test result: {errorBadge.text}")
        sleep(5)

    def authenticationInfoTest(self):
        self.usernameInput = self.driver.find_element(By.ID, "user-name")
        self.passwordInput = self.driver.find_element(By.ID, "password")
        self.loginBtn = self.driver.find_element(By.ID, "login-button")
        # case
        self.usernameInput.send_keys("")
        self.passwordInput.send_keys("")
        self.loginBtn.click()
        sleep(2)
        errorBadgeCloseIcon = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3/button/svg')
        errorBadgeCloseIcon.click()
        sleep(5)
        print(f"Test result: ")

    def successLogin(self):
        self.usernameInput = self.driver.find_element(By.ID, "user-name")
        self.passwordInput = self.driver.find_element(By.ID, "password")
        self.loginBtn = self.driver.find_element(By.ID, "login-button")
        # case
        self.usernameInput.send_keys("standard_user")
        self.passwordInput.send_keys("secret_sauce")
        self.loginBtn.click()
        sleep(2)

    def productTest(self):
        self.successLogin()
        sleep(5)
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Test result: Product total count-> {len(products)}")


inputTest = SauceDemoTest()
inputTest.productTest()
