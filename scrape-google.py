from selenium import webdriver
import sys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://aws.amazon.com/tw/ec2/pricing/on-demand/')
pageSource = driver.page_source
print(pageSource.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

driver.close()