#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv('C:/Users/admin/Desktop/houseprices-1.csv')


# In[4]:


data


# In[5]:


price = data.Price
age = data.Age
size = data.LotSize
area = data.LivingArea


# In[7]:


plt.scatter(price,age)
plt.show()


# In[8]:


np.corrcoef(price,age)


# In[9]:


plt.scatter(price,size)
plt.show()


# In[10]:


np.corrcoef(price,size)


# In[11]:


plt.scatter(price,area)
plt.show()


# In[12]:


np.corrcoef(price,area)

