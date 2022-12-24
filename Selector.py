#element = driver.find_element(By.XPATH, "//select[@name='name']")
#all_options = element.find_elements(By.TAG_NAME, "option")
#for option in all_options:
#    print("Value is: %s" % option.get_attribute("value"))
#    option.click()
#rlg-itemfilter__item
#chosen-drop.chosen-results
#active-result["name"].click()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import utils
driver = webdriver.Chrome()
driver.get("https://rocket-league.com/trading")
Button =  driver.find_element(By.ID, "acceptPrivacyPolicy")
# click it

# lazy timing TODO get server time for synchro
Button.click()
#with specific value
test_with_string="All Decals"
Selected_options = driver.find_element(By.CLASS_NAME, "rlg-itemfilter__item")
Selected_options.click()
Inside_div =Selected_options.find_element(By.TAG_NAME, "div")
inside_inside_div=Selected_options.find_element(By.TAG_NAME, "div")
list = Selected_options.find_element(By.TAG_NAME, "ul")
final_list = Selected_options.find_elements(By.TAG_NAME, "li")
for element in final_list:
    if(element.text==test_with_string):
        print(element.text)
        element.click()
#Selected_fields = driver.find_element(By.CLASS_NAME, "rlg-itemfilter__item").find_element(By.CLASS_NAME, "chosen-with-drop").find_element(By.CLASS_NAME, "chosen-drop").find_element(By.CLASS_NAME, "chosen-drop").find_elements(By.CLASS_NAME, "active-result")
#for field in Selected_fields:
#    if field.text == test_with_string:
#        print(test_with_string)
#        field.click()
time.sleep(10)
driver.close()
utils.json_write("items",)
# todo get item list paint list platform