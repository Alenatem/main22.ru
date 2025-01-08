from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.lambdatest.com/selenium-playground/iframe-demo/')
driver.maximize_window()

iframe = driver.find_element(By.XPATH, '//*[@id="iFrame1"]')
driver.switch_to.frame(iframe)
lon = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]')
sleep(2)
lon.send_keys(Keys.CONTROL + 'a')
lon.send_keys(Keys.DELETE)
bold_button_iframe = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[1]')
bold_button_iframe.click()
lon.send_keys('Hello')
