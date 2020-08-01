#pip install selenium if you don't have it installed
from time import sleep
from selenium import webdriver

#insert path to the chromedriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

#open up stackoverflow.com
driver.get("https://stackoverflow.com")

#look for the login button
login_button = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]')
#click on the login button
login_button.click()

#allow some time for the page to load before moving on
sleep(1)

#look for the username field
username = driver.find_element_by_xpath('//*[@id="email"]')
#type in your email
username.send_keys("your email here")

#look for the password field
password = driver.find_element_by_xpath('//*[@id="password"]')
#type in your email
password.send_keys("your password here")

#click on submit button
driver.find_element_by_xpath('//*[@id="submit-button"]').click()
