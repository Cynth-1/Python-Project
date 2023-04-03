#!/usr/bin/env python
# coding: utf-8

# **Data Analysis with Python**

# In[3]:


get_ipython().system('pip install openpyxl')


# In[4]:


# Importing the required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


# Read data from csv file
financial = pd.read_excel('C:/Users/user/Documents/work/py/financial_data.xlsx')


# In[6]:


financial.head()


# In[7]:


financial.shape


# In[8]:


# Structure of the data
financial.info()


# In[ ]:


# Brief statistical view of the data
financial.describe()


# Numerical Analysis and Visualization

# In[7]:


financial['Manufacturing Price'].describe()


# In[6]:


# Boxplot
financial['Manufacturing Price'].plot(kind='box', vert=False, figsize=(15,6))


# In[8]:


# Density Plot
financial['Manufacturing Price'].plot(kind='density', figsize=(15,6))


# In[19]:


# Mean and Median of the Distibution
stat = financial['Sale Price'].plot(kind='density', figsize=(15,6))
stat.axvline(financial['Sale Price'].mean(), color='red')
stat.axvline(financial['Sale Price'].median(), color='green')


# In[20]:


# Histogram of Product Sales
hist = financial['Sale Price'].plot(kind='hist', figsize=(15,6))
hist.set_ylabel('Units Sold')
hist.set_xlabel('Gross Sales')


# Categorical Analysis and Visualization

# In[ ]:


# Analyzing the Customer Segment 
financial['Segment'].value_counts()


# In[ ]:


# Pie Chart of Customer Segment
financial['Segment'].value_counts().plot(kind='pie', figsize=(6,6))


# In[11]:


# Barchart of Customer Segment
bar = financial['Segment'].value_counts().plot(kind='bar', figsize=(14,6))


# Relationship between Colums

# In[ ]:


corr = financial.corr()
corr


# In[ ]:


# Correlation Matrix
fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum = fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation= 'vertical');
plt.yticks(range(len(corr.columns)), corr.columns);


# In[ ]:


# Scatter Plot of Customer Segemnt and Sales
financial.plot(kind='scatter', x='Segment', y='Sales', figsize=(6,6))


# In[12]:


# Scatter Plot of Customer Segemnt and Sales
financial.plot(kind='scatter', x='Sales', y='Profit', figsize=(6,6))


# In[9]:


# Boxplot Showing Sales per Customer Segment
from pandas.plotting import boxplot
box = financial[['Sales', 'Segment']].boxplot(by='Segment', figsize=(10,6))
box.set_ylabel('Sales')


# In[13]:


col_boxplot = ['Sales', 'Month Number']
financial[col_boxplot].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))


# #### Data Wrangling - 
# Creating new colums and modifying existing colums

# In[14]:


# Add and Calculate Manufacturing Cost per Product
financial['Manufacturing Cost'] = financial['Manufacturing Price'] * financial['Units Sold']


# In[15]:


financial['Manufacturing Cost'].head()


# In[16]:


# Create new price
financial['New Sale Price'] = financial['Sale Price'] *+ 1.03


# In[17]:


financial['New Sale Price'].head()


# In[18]:


financial.head()


# Selection and Indexing

# In[ ]:


# Get all Sales from a Country
financial.loc[financial['Country'] == 'Canada']


# In[ ]:


# Obtain the Mean Revenue for a Segment
financial.loc[financial['Segment'] == 'Government', 'Sales'].mean()

