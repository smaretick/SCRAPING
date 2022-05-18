#PYTHON SCRAPING
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites")
# I am using Chrome Developer Tool to get the Xpath, you might want to use your own code.
pic = browser.find_element_by_xpath('//*[@id="post-174"]/div/p[5]/a/img')
#VISIT STAKE==XPATH /html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/table/tbody/tr[2]/td[6]/a
position = pic.location
print(position)