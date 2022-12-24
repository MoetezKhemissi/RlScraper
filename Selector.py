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
def fresh_start(driver):
    driver.get("https://rocket-league.com/trading")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    Button =  driver.find_element(By.ID, "acceptPrivacyPolicy")
    Button.click()
    return current_time
def get_fields_select(driver,name):

    path_to_fields="rlg-itemfilter__"+name
    Selected_options = driver.find_element(By.CLASS_NAME, path_to_fields)
    Selected_options.click()
    list = Selected_options.find_element(By.CLASS_NAME, "chosen-results")
    final_list = list.find_elements(By.TAG_NAME, "li")
    return final_list


#Possible select_from values:
#   "item"
#   "paint"
#   "platform"
def select_field(driver,select_from,value_to_be_selected):
    fields = get_fields_select(driver,select_from)
    for element in fields:
        if(element.text==value_to_be_selected):
            element.click()

def get_all_possible_values(driver,select_from):
    values=[]
    fields = get_fields_select(driver,select_from)
    for element in fields:
        values.append(element.text)
    return values
def get_possible_values_and_export_csv(driver,select_from):
    utils.json_write(select_from,get_all_possible_values(driver,select_from))

items=[]
test_with_string="All Decals"
name="item"
driver = webdriver.Chrome()
fresh_start(driver)
get_possible_values_and_export_csv(driver,"platform")

driver.close()
# todo get item list paint list platform

def search_list_export_pdf():
    pass
