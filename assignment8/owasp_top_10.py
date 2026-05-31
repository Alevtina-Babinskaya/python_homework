from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import csv
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2025/")
top10_list_25 =[]
h3_top_list = driver.find_element(By.CSS_SELECTOR, '[id="top-102025-list"]')
ol_top_list = h3_top_list.find_element(By.XPATH, 'following-sibling::ol[1]')
lis_top_list = ol_top_list.find_elements(By.CSS_SELECTOR, 'li')
for li in lis_top_list:
    a = li.find_element(By.CSS_SELECTOR, 'a')
    text = a.text.strip()
    href = a.get_attribute('href')
    if text and href:
        top10_list_25.append({'Title': text, 'Link': href})
print(top10_list_25) 

df_top10 = pd.DataFrame(top10_list_25)

df_top10.to_csv('owasp_top_10.csv', index=False)