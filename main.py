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
#platforms = all_platform_list()
#paints = all_paint_list()
#items = all_item_list()
#print(platforms)


#TODO shorten down by having common elements in functions
def get_selling_json(driver,item,NbPages,request_time):
    select_field(driver,"paint",item["paint"])
    select_field(driver,"item",item["item"])
    select_field(driver,"cert","None")
    select_field(driver,"platform","PC (Steam & Epic)")
    form = driver.find_element(By.TAG_NAME,"form")
    footer_blocker(driver)
    form.find_element(By.XPATH,"/html/body/main/div/div/div[1]/div[2]/div/div/form/input").click()
    print("Selling data collection for ",item["item"],":")
    Trades = getData(NbPages,driver)
    Parsed_trades=parse_data(Trades,request_time)
    #TODO filename with fiename = buyin + nameitem + timestamp
    filename='selling_'+item["item"]+"_"+item["paint"]
    json_write(filename,Parsed_trades)
def get_buying_json(driver,item,NbPages,request_time):
    select_field(driver,"paint",item["paint"])
    select_field(driver,"item",item["item"])
    select_field(driver,"cert","None")
    select_field(driver,"platform","PC (Steam & Epic)")
    select_field(driver,"searchtype","I have this item")
    form = driver.find_element(By.TAG_NAME,"form")
    footer_blocker(driver)
    form.find_element(By.XPATH,"/html/body/main/div/div/div[1]/div[2]/div/div/form/input").click()
    print("Buying data collection for ",item["item"],":")
    Trades = getData(NbPages,driver)
    Parsed_trades=parse_data(Trades,request_time)
    filename='Buying_'+item["item"]+"_"+item["paint"]
    json_write(filename,Parsed_trades)
#TODO add max date 
def export_buy_sell_data_json(driver,item,n,request_time):
    get_buying_json(driver,item,n,request_time)
    driver.refresh()
    time.sleep(1)
    request_time = fresh_start(driver)
    get_selling_json(driver,item,n,request_time)
#--------------BLOCK to be replaced by auto selector-----------#
item={"paint":"Cobalt","item":"Zomba"}
driver = webdriver.Chrome()
driver.maximize_window()
request_time = fresh_start(driver)
export_buy_sell_data_json(driver,item,3,request_time)
#--------------------------------------

time.sleep(10)


#TODO automatically check item
