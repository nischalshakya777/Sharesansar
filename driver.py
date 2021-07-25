from selenium import webdriver
import time
from datetime import date
from selenium.webdriver.common.keys import Keys
from scrape_table_all import scrape_table
from return_dates import return_dates

# Open the link
browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.maximize_window()
browser.get("https://www.sharesansar.com/today-share-price")
# Select the type of data to scrape

# Select Commercial Bank
searchBar = browser.find_element_by_id('sector')
searchBar.send_keys('All Sector')

sdate = date(2010, 1, 3)
edate = date(2021, 7, 24)
dates = return_dates(sdate, edate)

for day in dates:
    # Enter the date
    date_box = browser.find_elements_by_id('fromdate')
    date_box[0].clear()
    date_box[0].send_keys(day)
    # Click Search
    searchBar = browser.find_element_by_id('btn_todayshareprice_submit')
    searchBar.click()
    time.sleep(3)  # Needed for this sites
    searchBar.send_keys(Keys.ENTER)
    time.sleep(8)  # Wait for data to show up longer wait time ensures data has loaded before scraping begins
    # Scrape the table
    html = browser.page_source
    scrape_table(data=html, date=day)

browser.close()
