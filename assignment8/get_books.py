from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import csv
import pandas as pd
from time import sleep


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
results = []
search_list = driver.find_elements(By.CSS_SELECTOR, 'li.row.cp-search-result-item')
for li in search_list:
    title = li.find_element(By.CSS_SELECTOR, 'span.title-content').text

    authors = li.find_elements(By.CSS_SELECTOR, 'a.author-link')
    authors_list = [a.text for a in authors]
    authors_text = "; ".join(authors_list)
    format_year = li.find_element(By.CSS_SELECTOR, 'span.display-info-primary').text
    if title and authors_text and format_year:
        results.append({'Title': title, 'Author': authors_text, 'Format-Year': format_year})
results_df = pd.DataFrame(results)

# Here I tried to get the list of links from pagination and use them to get data from all the pages, but somehow driver finds only one link in the list. 
# I assume that driver doesn't download the page correctly or do it too fast too download all the links.
# sleep(20)
# pages_section = driver.find_element(By.CSS_SELECTOR, 'ul.pagination__desktop-items')
# pages_links = pages_section.find_elements(By.TAG_NAME, 'a')
# print(pages_section.get_attribute("outerHTML"))
# print(len(pages_links))
# for link in pages_links:
#     print(link.get_attribute('href'))


results_df.to_csv('get_books.csv', index=False)
    

with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)




