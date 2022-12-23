from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.get("https://rocket-league.com/trading")
#find accept button
Button =  driver.find_element(By.ID, "acceptPrivacyPolicy")
# click it

# lazy timing TODO get server time for synchro
Button.click()
Trades = driver.find_elements(By.CLASS_NAME, "rlg-trade")
traders = []
indiv_trade={"trader":"","time":""}

for _ in range(0,5):
    LoadMore_button = driver.find_element(By.CLASS_NAME, "rlg-trading__loadmore").find_element(By.TAG_NAME, "button").click()
    for trade in Trades:
        name_trader = trade.find_element(By.CLASS_NAME, "rlg-trade__username").text
        #time parser
        time_trade = trade.find_element(By.CLASS_NAME, "rlg-trade__time").find_element(By.TAG_NAME, "span").text
        indiv_trade.update({"trader":name_trader,"time": time_trade})
        print(indiv_trade)
    #TODO better logic for not overloading probably await for clickable
    time.sleep(4)
for trader in traders:
    print(trader)
driver.close()


#GENERAL TODO  is to make it load up individual items
#TODO individual item load prices
#click to find logic you can start lazy by getting link
# if one to one mapping && credit load it up 
