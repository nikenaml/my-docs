#How to get the HTML
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

# Tags (warna ungu di inspect)
soup.header
soup.div

# Navigable Strings (warna hitam di inspect/konten)
tag = soup.header.p
tag.string
soup.header.p.string

# Attributes (warna kuning di inspect -> class, style, summary dkk)
tag = soup.header.a
tag.attrs
tag['data-toggle']
tag['attribute'] = 'this is a atrribute'
tag.attrs