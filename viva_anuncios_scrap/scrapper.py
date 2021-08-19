# Dependencies and libraries
import requests
import pandas as pd

from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


url = 'https://www.vivanuncios.com.mx/s-venta-inmuebles/distrito-federal/v1c1097l1008p1'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
print(soup)