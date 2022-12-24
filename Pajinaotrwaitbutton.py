from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from datetime import datetime
from utile import progress_bar


#---------------------Get Data from each page of site----------------
def getData(n,driver):
    for _ in range(1,n):
        el = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable( driver.find_element(By.CLASS_NAME, "rlg-trading__loadmore").find_element(By.TAG_NAME, "button")))
        aanoyingfooter=driver.find_elements(By.CLASS_NAME, "vm-footer-content ")
        if (len(aanoyingfooter)!=0):
            driver.execute_script("document.getElementsByClassName('vm-footer-content')[0].style.display = 'none';")
            print("----------SUCCESSFUL FOOTER BLOCK ---------------")
        LoadMore_button = driver.find_element(By.CLASS_NAME, "rlg-trading__loadmore").find_element(By.TAG_NAME, "button").click()
    Trades = driver.find_elements(By.CLASS_NAME, "rlg-trade")  
    return Trades
#---------------------Get individual items from each trade----------------
def item_parse(items):
    array_items=[]
    dict_item={}
    for item in items:
            itemf = item.find_element(By.CLASS_NAME, "rlg-item__text").find_element(By.CLASS_NAME, "rlg-item__name")
            item_name=itemf.text
    #TODO name without prefixes
            dict_item.update({"name":item_name})
            quantity_exists=len(item.find_elements(By.CLASS_NAME, "rlg-item__quantity"))
            if (quantity_exists!=0):
                Value=item.find_element(By.CLASS_NAME, "rlg-item__quantity").text
                item_quantity=Value
                dict_item.update({"quantity":item_quantity})
            color_exists=len(item.find_elements(By.CLASS_NAME, "rlg-item__paint"))
            if (color_exists!=0):
                Value=item.find_element(By.CLASS_NAME, "rlg-item__paint").text
                item_color=Value
                dict_item.update({"color":item_color})
            array_items.append(dict_item.copy())
    return array_items

#---------------------Get GENERAL Fields from each trade----------------

def parse_data(Trades):
    indiv_trade={"trader":"","time": "","Hasitems": [],"WantItems":[]}
    Parsed_trades = []
    progress_bar(0,len(Trades))
    i=0
    for trade in Trades:
        i=i+1
        name_trader = trade.find_element(By.CLASS_NAME, "rlg-trade__username").text
        has_items = trade.find_element(By.CLASS_NAME, "rlg-trade__itemshas").find_elements(By.CLASS_NAME, "rlg-item")
        want_items=trade.find_element(By.CLASS_NAME, "rlg-trade__itemswants").find_elements(By.CLASS_NAME, "rlg-item")
        array_has_items = item_parse(has_items)
        array_want_items = item_parse(want_items)
            #time parser
        time_trade = trade.find_element(By.CLASS_NAME, "rlg-trade__time").find_element(By.TAG_NAME, "span").text
        indiv_trade.update({"trader":name_trader,"time": time_trade,"Hasitems": array_has_items,"WantItems":array_want_items})
        Parsed_trades.append(indiv_trade.copy())
        print(indiv_trade)
        progress_bar(i+1,len(Trades))
    return Parsed_trades

#---------------------Transform to json and print to file ----------------
def json_write(name,Parsed_trades):
    json_trades = json.dumps(Parsed_trades)
    full_name=name+'.json'
    with open(full_name, 'w') as outfile:
        outfile.write(json_trades)


#----------------MAIN---------------------------------

#TODO URGENT has items want items + has items  1 to 1 mapping + credit 
#TODO individual item load prices
#click to find logic you can start lazy by getting link
# if one to one mapping && credit load it up 
