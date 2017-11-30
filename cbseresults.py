from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://resultsarchives.nic.in/cbseresults/cbseresults2015/class12/cbse122015_all.htm")

inputElement = driver.find_element_by_id("regno")
inputElement.send_keys('2631559')

inputElement.send_keys(Keys.ENTER)

print(driver.page_source)
