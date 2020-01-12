# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/results?search_query=' + 'ed+sheeran'

response = requests.get(url)

page = response.text 
html = BeautifulSoup(page , 'html.parser')

with open('x.html' , 'w' , encoding = 'utf-8') as f:
    f.write(str(html))