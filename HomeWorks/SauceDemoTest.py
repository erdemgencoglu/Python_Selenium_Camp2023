from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class UserInputTest:

    def userNameAndPasswordTest(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorBadge = driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        if usernameInput.text.strip() == "" and passwordInput.text.strip() == "":
            driver.execute_script(
                "arguments[0].innerText = 'Epic sadface: Username is required'", errorBadge)
        if passwordInput.text.strip() == "":
            driver.execute_script(
                "arguments[0].innerText = 'Epic sadface: Password is required'", errorBadge)
        if usernameInput.text.strip() == "locked_out_user" and passwordInput.text.strip() == "secret_sauce":
            driver.execute_script(
                "arguments[0].innerText = 'Epic sadface: Sorry, this user has been locked out.'", errorBadge)
        if usernameInput.text.strip() == "" and passwordInput.text.strip() == "":
            usernameInput = driver.find_element(By.ID, "user-name")
            passwordInput = driver.find_element(By.ID, "password")
            errorBadgeCloseIcon = driver.find_element(By.XPATH, "//*[@id="login_button_container"]/div/form/div[3]/h3/button/svg")
            usernameInput.send_keys("")
            passwordInput.send_keys("")
            errorBadgeCloseIcon.click()

        if usernameInput.text.strip() == "standard_user" and passwordInput.text.strip() == "secret_sauce":
            driver.get("https://www.saucedemo.com/inventory.html")
        while True:
            print()


inputTest = UserInputTest()
inputTest.userNameAndPasswordTest()
