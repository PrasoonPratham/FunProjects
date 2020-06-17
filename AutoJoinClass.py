'''Program to automatically join a google meet meeting'''

#Import Libraries and load webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

#Loading Page
link = "https://meet.google.com/cfj-dhum-jqu"
driver.get(link)

#Credentials
emailId = "youemail@domain.com"
password = "yourPasssword"

#Signing into Google Account
signInButton = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[1]/div[2]/div/div/span/span")
signInButton.click()
signInEmailId = driver.find_element_by_id("identifierId")
signInEmailId.send_keys(emailId)
nextButton = driver.find_element_by_id("identifierNext")
nextButton.click()
passwordBox = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
passwordBox.send_keys(password)
nextButton.click()

#Joining meeting with camera and mic off
mic = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div/div[1]")
mic.click()
video = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div/div[1]")
video.click()
joinButton = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
joinButton.click()
    


    
    
