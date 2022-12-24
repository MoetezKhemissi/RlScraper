from utile import all_platform_list
from utile import all_paint_list
from utile import all_item_list
from Selector import fresh_start
from Selector import select_field
from Selector import footer_blocker
from Pajinaotrwaitbutton import getData
from Pajinaotrwaitbutton import parse_data
from Pajinaotrwaitbutton import json_write
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
#test listing
platforms = all_platform_list()
#paints = all_paint_list()
#items = all_item_list()
print(platforms)

#--------------BLOCK to be replaced by auto selector-----------#
driver = webdriver.Chrome()
fresh_start(driver)
select_field(driver,"paint","Titanium White")
select_field(driver,"item","Octane")
select_field(driver,"cert","None")
select_field(driver,"platform","PC (Steam & Epic)")
form = driver.find_element(By.TAG_NAME,"form")
footer_blocker(driver)
form.find_element(By.XPATH,"/html/body/main/div/div/div[1]/div[2]/div/div/form/input").click()

#--------------------------------------

Trades = getData(2,driver)
Parsed_trades=parse_data(Trades)
json_write('TW_Octane',Parsed_trades)
time.sleep(10)


#TODO better logic than from import
#TODO automatically check item