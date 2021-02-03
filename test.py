from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
import pandas as pd
import time
import csv

URL = 'http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!%7B%22action%22%3A%22(And.Hidden.N._.Category.%EA%B2%BD%EC%B0%A8._.(C.CarType.Y._.(C.Manufacturer.%EA%B8%B0%EC%95%84._.(C.ModelGroup.%EB%AA%A8%EB%8B%9D._.(C.Model.%EC%98%AC%20%EB%89%B4%20%EB%AA%A8%EB%8B%9D%20(JA_)._.(C.BadgeGroup.%EA%B0%80%EC%86%94%EB%A6%B0%201000cc._.Badge.%ED%94%84%EB%A0%88%EC%8A%A4%ED%8B%B0%EC%A7%80.)))))_.Options.%EC%84%A0%EB%A3%A8%ED%94%84.)%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A%2250%22%7D'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36')
driver = webdriver.Chrome('./bin/chromedriver', options=options)
driver.get(url=URL)
#driver.implicitly_wait(3)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
items = soup.select('#sr_normal > tr')
carlist = []
for item in items:
    temp=[]
    link = 'http://www.encar.com' + item.select_one('tr > td.img > div > a')['href']
    carid = parse.parse_qs(parse.urlparse(link).query)['carid'][0]
    name = item.select_one('tr > td.inf > a').text 
    detail = item.select_one('tr > td.inf > span.detail').text
    price = item.select_one('tr > td.prc_hs').text
    service = item.select_one('tr > td.svc').text
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    carlist.append({
        'ID': carid.strip(),
        'Name': name.strip(),
        'Detail': detail.strip(),
        'Price': price.strip(),
        'Service': service.strip(),
        'Link': link,
        'CreatedDate': now
    })

data = pd.DataFrame(carlist)
print(data)
data.to_csv('carlist.csv')
driver.quit()
