# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://cryptomaniaks.com/stake-review/'
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)