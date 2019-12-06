from selenium import webdriver
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

url = "https://www.google.com/search?q=hola&oq=hola&aqs=chrome..69i57j0l5.721j0j7&sourceid=chrome&ie=UTF-8"
driver.get(url)

val = driver.find_element_by_id('resultStats')
print(val.text)

