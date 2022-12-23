from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
driver = webdriver.Chrome()
driver.get("https://rocket-league.com/trading")
# lazy timing TODO get server time for synchro
Button =  driver.find_element(By.ID, "acceptPrivacyPolicy")
# click it

# lazy timing TODO get server time for synchro
Button.click()
traders = []
indiv_trade={"trader":"","time": "","Hasitems": [],"WantItems":[]}
time.sleep(1)

#---------------------Get Data from each page of site----------------
for _ in range(0,1):
     #TODO better logic for not overloading unstable click load time AND try catch HIDE banner thingy
    el = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable( driver.find_element(By.CLASS_NAME, "rlg-trading__loadmore").find_element(By.TAG_NAME, "button")))
    time.sleep(1)
    aanoyingfooter=driver.find_elements(By.CLASS_NAME, "vm-footer-content ")
    if (len(aanoyingfooter)!=0):
        driver.execute_script("document.getElementsByClassName('vm-footer-content')[0].style.display = 'none';")
        print("----------SUCCESSFUL FOOTER BLOCK ---------------")
    LoadMore_button = driver.find_element(By.CLASS_NAME, "rlg-trading__loadmore").find_element(By.TAG_NAME, "button").click()
Trades = driver.find_elements(By.CLASS_NAME, "rlg-trade")  

#---------------------Get individual items from each trade----------------
def item_parse(items):
    array_items=[]
    for item in items:
            itemf = item.find_element(By.CLASS_NAME, "rlg-item__text").find_element(By.CLASS_NAME, "rlg-item__name")
            item_type=itemf.text
    #TODO more granular data like color and exception handling
            size=len(item.find_elements(By.CLASS_NAME, "rlg-item__quantity"))
            if (size!=0):
                Value=item.find_element(By.CLASS_NAME, "rlg-item__quantity").text
                item_type=item_type+Value
            array_items.append(item_type)
    return array_items

#---------------------Get Fields from each trade----------------
for trade in Trades:
    name_trader = trade.find_element(By.CLASS_NAME, "rlg-trade__username").text
    has_items = trade.find_element(By.CLASS_NAME, "rlg-trade__itemshas").find_elements(By.CLASS_NAME, "rlg-item")
    want_items=trade.find_element(By.CLASS_NAME, "rlg-trade__itemswants").find_elements(By.CLASS_NAME, "rlg-item")
    array_has_items = item_parse(has_items)
    array_want_items = item_parse(want_items)
        #time parser
    time_trade = trade.find_element(By.CLASS_NAME, "rlg-trade__time").find_element(By.TAG_NAME, "span").text
    indiv_trade.update({"trader":name_trader,"time": time_trade,"Hasitems": array_has_items,"WantItems":array_want_items})
    traders.append(indiv_trade)
    print(indiv_trade)

json_trades = json.dumps(traders)
print(json_trades)
driver.close()

#TODO URGENT has items want items + has items  1 to 1 mapping + credit 
#GENERAL TODO  is to make it load up individual items
#TODO individual item load prices
#click to find logic you can start lazy by getting link
# if one to one mapping && credit load it up 
