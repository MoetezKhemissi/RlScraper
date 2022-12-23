from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.get("https://rocket-league.com/trading")
#find accept button
Button =  driver.find_element(By.ID, "acceptPrivacyPolicy")
# click it
Button.click()
Trades = driver.find_elements(By.CLASS_NAME, "rlg-trade")
traders = []
for _ in range(0,5):
    LoadMore_button = driver.find_element(By.CLASS_NAME, "rlg-trading__loadmore").find_element(By.TAG_NAME, "button").click()
    for trade in Trades:
        traders.append(trade.find_element(By.CLASS_NAME, "rlg-trade__username").text)
    time.sleep(4)
for trader in traders:
    print(trader)
driver.close()