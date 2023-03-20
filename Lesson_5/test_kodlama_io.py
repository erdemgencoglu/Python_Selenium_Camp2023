from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class TestInValidLogin:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(5)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(5)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(10)
        errorMessage = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "HATALI GİRİŞ"
        print(f"Test sonucu : {testResult}")
        while True:
            print("")


testClass = TestInValidLogin()
testClass.test_invalid_login()
