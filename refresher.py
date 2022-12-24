from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import utile
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
for _ in range(0,5):
    time.sleep(2)
    driver.refresh()