#How to get the HTML
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'

page = requests.get(url)
print(page) # check if eligble to scrap


soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

# 1. price of the stock
pos = soup.find(['bg-quote'], class_ = ['value']).text
print(pos)

# 2. closing price of the stock
cps = soup.find(['td'], class_ = ['table__cell u-semi']).text
print(cps)

# 3. 52 week range (lower,upper)
## schema 
wrlu = soup.find_all(['div'], class_ = ['range__header'])[2]
print(wrlu)

## content
c_wrlu = wrlu.find('span', class_ = 'secondary').text
print("content: " + c_wrlu)

## lower upper
l_wrlu = wrlu.find_all('span', class_ = 'primary')[0].text
print("lower: " + l_wrlu)

u_wrlu = wrlu.find_all('span', class_ = 'primary')[1].text
print("upper: " + u_wrlu)

# 4. analyst rating
ar = soup.find('li', class_ = 'analyst__option active').text
print(ar)

