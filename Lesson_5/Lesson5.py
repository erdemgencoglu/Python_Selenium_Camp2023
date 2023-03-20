from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://google.com.tr")
input = driver.find_element(By.NAME, "q")
sleep(5)
input.send_keys("Kodlama io")
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
firstResult = driver.find_element(
    By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a full xpath

listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlama io sitesinde su anda {len(listOfCourses)} adet kurs var.")
firstResult.click()
# sleep(10)
while True:
    continue
# HTML LOCATORS
