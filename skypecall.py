#!/usr/bin/env python
import time
import json
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

parser = argparse.ArgumentParser()
parser.add_argument('--user', help='Microsoft username')
parser.add_argument('--passwd', help='Microsoft password')
parser.add_argument('--callto', help='A Skype friend to call to')
args = parser.parse_args()

# driver
options = webdriver.ChromeOptions()
options.Proxy = None
options.add_argument('headless')
options.add_argument('window-size=1920,1080')
options.add_argument('use-fake-device-for-media-stream')
options.add_argument('use-fake-ui-for-media-stream')
driver = webdriver.Chrome(options=options)

# login
driver.get("https://web.skype.com")
time.sleep(10)
driver.find_element(By.NAME, "loginfmt").send_keys(args.user)
time.sleep(3)
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(3)
driver.find_element(By.ID, "i0118").send_keys(args.passwd)
time.sleep(3)
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(20)

# call
driver.find_element(By.XPATH, '//button[@aria-label="Got it!"]').click()
driver.find_element(By.XPATH, '//button[@title="Calls"]').click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//button[@aria-label="%s, start voice call."]' % args.callto)
ActionChains(driver).move_to_element(element).click(element).perform()
time.sleep(20)

# quit
driver.quit()