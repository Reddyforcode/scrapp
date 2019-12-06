from selenium import webdriver
import os

#url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

url = "https://www.google.com/search?q=hola&oq=hola&aqs=chrome..69i57j0l5.721j0j7&sourceid=chrome&ie=UTF-8"
driver.get(url)
#driver.set_page_load_timeout(45)
#driver.maximize_window()
#driver.implicitly_wait(2)
#driver.get_screenshot_as_file("E:\\Python\\Tatacliq.png")
#print ("Executed Succesfull")
#driver.find_element_by_xpath("//div[@class='pdp-promo-title pdp-title']").click()
#SpecialPrice =driver.find_element_by_xpath("//div[]").text
val = driver.find_element_by_id('resultStats')
print(val.text)

