#!/usr/bin/env python
# coding: utf-8

# # Viva anuncios scrapper

# ### Set-up

# In[1]:


# Dependencies and libraries
import requests
import pandas as pd
import re

from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Loading page
url = 'https://www.vivanuncios.com.mx/s-venta-inmuebles/distrito-federal/v1c1097l1008p1'
browser.visit(url)


# In[4]:


# Getting the page
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
soup2 = soup.findAll('div', class_='tileV2 REAdTileV2 regular mapView')


# In[5]:


id = 1
scrapped_data = {id:{}}
for ad in soup2:
    scrapped_data[id]['price'] = (ad.find(class_="ad-price").text)
    try:
        scrapped_data[id]['square_meters'] = (ad.find(class_="chiplets-inline-block surface-area").text)
    except:
        scrapped_data[id]['square_meters'] = ('0')
    try:
        scrapped_data[id]['bedrooms'] = (ad.find(class_="chiplets-inline-block re-bedroom").text)
    except:
        scrapped_data[id]['bedrooms'] = ('0')
    try:
        scrapped_data[id]['bathrooms'] = (ad.find(class_="chiplets-inline-block re-bathroom").text)
    except:
        scrapped_data[id]['bathrooms'] = ('0')
    try:
        scrapped_data[id]['parking_spaces'] = (ad.find(class_="chiplets-inline-block car-parking").text)
    except:
        scrapped_data[id]['parking_spaces'] = ('0')
    try:
        scrapped_data[id]['address'] = (ad.find(class_="tile-location one-liner").text)
    except:
        scrapped_data[id]['address'] = ('0')
    try:
        scrapped_data[id]['description'] = (ad.find(class_="href-link tile-title-text").text)
    except:
        scrapped_data[id]['description'] = ('0')
    id += 1
    scrapped_data[id] = {'price':[], 'square_meters':[], 'bedrooms': [], 'bathrooms': [],
                         'parking_spaces': [], 'address':[], 'description':[]}
scrapped_data
    


# ### Reformatting

# In[6]:


i = 1
for i in range(1,len(scrapped_data)+1):
    # Reformatting price
    scrapped_data[i]['price'] = re.sub("[^0-9]", "", scrapped_data[i]['price'])
    # Reformatting square meters
    scrapped_data[i]['square_meters'] = re.sub("[^0-9]", "", scrapped_data[i]['square_meters'])
    
    print (scrapped_data)


# In[7]:


scrapped_data


# In[ ]:





# In[ ]:




