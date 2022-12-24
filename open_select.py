from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from datetime import datetime
driver = webdriver.Chrome()
#TODO individual item load prices how to : URL making
# function select with field and value
driver.get("https://rocket-league.com/trading?filterItem=968&filterCertification=0&filterPaint=7&filterSeries=A&filterTradeType=0&filterMinCredits=0&filterMaxCredits=100000&filterSearchType=1&filterItemType=0")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
Button =  driver.find_element(By.ID, "acceptPrivacyPolicy")
# click it

# lazy timing TODO get server time for synchro
Button.click()
Parsed_trades = []
indiv_trade={"trader":"","time": "","Hasitems": [],"WantItems":[]}
time.sleep(1)

#---------------------Get Data from each page of site----------------
def getData(n,driver):
    for _ in range(1,n):
        NomorePage = len(driver.find_element(By.CLASS_NAME, "rlg-trading__loadmore").find_elements(By.TAG_NAME,"p"))
        if NomorePage>0:
            pass
        else:
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
    Parsed_trades = []
    for trade in Trades:
        name_trader = trade.find_element(By.CLASS_NAME, "rlg-trade__username").text
        has_items = trade.find_element(By.CLASS_NAME, "rlg-trade__itemshas").find_elements(By.CLASS_NAME, "rlg-item")
        want_items=trade.find_element(By.CLASS_NAME, "rlg-trade__itemswants").find_elements(By.CLASS_NAME, "rlg-item")
        array_has_items = item_parse(has_items)
        array_want_items = item_parse(want_items)
            #TODO time parser
        time_trade = trade.find_element(By.CLASS_NAME, "rlg-trade__time").find_element(By.TAG_NAME, "span").text
        indiv_trade.update({"trader":name_trader,"time": time_trade,"Hasitems": array_has_items,"WantItems":array_want_items})
        Parsed_trades.append(indiv_trade.copy())
        print(indiv_trade)
    return Parsed_trades

#---------------------Transform to json and print to file ----------------
def json_write(name,Parsed_trades):
    json_trades = json.dumps(Parsed_trades)
    full_name=name+'.json'
    with open(full_name, 'w') as outfile:
        outfile.write(json_trades)


#----------------MAIN---------------------------------

Trades = getData(2,driver)
Parsed_trades=parse_data(Trades)
json_write('GreyZigzag',Parsed_trades)
driver.close()

#click to find logic you can start lazy by getting link
# if one to one mapping && credit load it up 
#TODO DELETE THIS PAGE AND JUST IMPORT FUNCTION