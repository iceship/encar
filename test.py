import config
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
import pandas as pd
import time
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import exc
pymysql.install_as_MySQLdb()
import MySQLdb
import telegram

bot = telegram.Bot(token = config.telegram_bot_api)
URL = config.encar_url
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument(config.user_agent)
driver = webdriver.Chrome('./bin/chromedriver', options=options)
driver.get(url=URL)
#driver.implicitly_wait(3)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
items = soup.select('#sr_normal > tr')
carlist = []
for item in items:
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

car_new_df = pd.DataFrame(carlist)

engine = create_engine(config.db_connection, encoding='utf-8')

new_df = pd.DataFrame()
for i in range(len(car_new_df)):
    try:
        new_car = car_new_df.iloc[i:i+1]
        new_car.to_sql(name='car', con=engine, if_exists='append', index=False)
        bot.send_message(chat_id=chat_id, text=new_car.to_string(index=False, header=False))
        new_df = new_df.append(new_car)
    except exc.IntegrityError:
        pass
