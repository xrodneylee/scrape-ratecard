from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import time

url = 'https://aws.amazon.com/tw/ec2/pricing/on-demand/'

driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
pageSource = driver.page_source
# print(pageSource.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
soup = BeautifulSoup(pageSource, 'lxml')

# print(soup.prettify(encoding='utf-8'))
for caption in soup.find_all('caption'):
  print('caption', caption.get_text())

driver.quit()