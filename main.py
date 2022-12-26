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
    request_time = datetime.now()
    time.sleep(1)
    get_selling_json(driver,item,n,request_time)
#--------------BLOCK to be replaced by auto selector-----------#
item1={"paint":"Cobalt","item":"Zomba"}
item2={"paint":"Crimson","item":"Zomba"}
item3={"paint":"Lime","item":"Zomba"}
item4={"paint":"Titanium White","item":"Zomba"}
item5={"paint":"Saffron","item":"Zomba"}
item6={"paint":"Cobalt","item":"Octane"}
item7={"paint":"Crimson","item":"Octane"}
item8={"paint":"Lime","item":"Octane"}
item9={"paint":"Titanium White","item":"Octane"}
item10={"paint":"Saffron","item":"Octane"}
item11={"paint":"Cobalt","item":"Draco"}
item12={"paint":"Crimson","item":"Draco"}
item13={"paint":"Lime","item":"Draco"}
item14={"paint":"Titanium White","item":"Draco"}
item15={"paint":"Saffron","item":"Draco"}
list_items=[]
list_items.append(item1)
list_items.append(item2)
list_items.append(item3)
list_items.append(item4)
list_items.append(item5)
list_items.append(item6)
list_items.append(item7)
list_items.append(item8)
list_items.append(item9)
list_items.append(item10)
list_items.append(item11)
list_items.append(item12)
list_items.append(item13)
list_items.append(item14)
list_items.append(item15)
driver = webdriver.Chrome()
driver.maximize_window()
fresh_start(driver)
for item in list_items:
    driver.refresh()
    request_time = datetime.now()
    time.sleep(1)
    export_buy_sell_data_json(driver,item,1,request_time)
#--------------------------------------

time.sleep(10)


#TODO automatically check item
#TODO fix intercepted error
