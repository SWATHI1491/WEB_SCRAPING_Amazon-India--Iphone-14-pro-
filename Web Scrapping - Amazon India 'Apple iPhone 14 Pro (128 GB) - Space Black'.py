#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


URL = 'https://www.amazon.in/s?k=iphone+14+pro&rh=n%3A1389401031&ref=nb_sb_noss'


# In[3]:


HEADERS = ({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",'Accept- Language':'en-US,en;q=0.5'})


# In[4]:


# HTTP Request
webpage = requests.get(URL, headers=HEADERS)


# In[8]:


webpage


# In[5]:


type(webpage.content)


# In[6]:


# Soup Object containiang all data
soup = BeautifulSoup(webpage.content, "html.parser")


# In[7]:


soup


# In[9]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


# In[10]:


links


# In[11]:


link = links[0].get('href')


# In[12]:


product_list = "https://amazon.in" + link


# In[13]:


product_list


# In[14]:


new_webpage = requests.get(product_list, headers=HEADERS)


# In[15]:


new_webpage


# In[16]:


# Soup Object containiang all data
new_soup = BeautifulSoup(new_webpage.content, "html.parser")


# In[17]:


new_soup


# In[18]:


new_soup.find("span", attrs={"id":'productTitle'}).text.strip()


# In[19]:


new_soup.find("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"}).find("span", attrs={"class": "a-offscreen"}).text.strip()


# In[20]:


new_soup.find("span", attrs={"class":'a-icon-alt'}).text.strip()


# In[ ]:




