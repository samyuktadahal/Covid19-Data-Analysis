#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Python Data Analysis\Covid19 Data Analysis\4. covid_19_data.csv")
df


# In[5]:


df.info()


# In[6]:


df.shape


# In[7]:


df.dtypes


# In[8]:


df.isnull().sum()


# In[9]:


df.count()


# In[10]:


df.nunique()


# In[11]:


df.groupby('Region').sum()


# In[12]:


df.groupby('Region')['Confirmed'].sum()


# In[18]:


d2= df.groupby('Region')['Confirmed'].sum().sort_values(ascending= False).head()
d2


# In[19]:


d2.plot(kind= 'bar')


# In[20]:


d1= df.groupby('Region')['Deaths'].sum().sort_values(ascending= False).head()
d1


# In[22]:


d1.plot()


# In[25]:


death_percentage = (df['Deaths']/df['Confirmed'])*100
print(death_percentage)


# In[24]:


recovered_percentage = (df['Recovered']/df['Confirmed'])*100
print(recovered_percentage)


# In[26]:


df['Confirmed'].sort_values(ascending= True).head(10)


# In[31]:


df


# In[32]:


df1= df[~(df['Confirmed']<10)]
df1


# In[33]:


df['Region'].nunique()


# In[34]:


df[df['Region']=='Nepal']


# In[35]:


df[df['Region']=='US']


# In[36]:


df.sort_values(by= 'Confirmed', ascending= True)


# In[37]:


df.sort_values(by= 'Deaths', ascending= False).head(20)


# In[38]:


df.groupby('Region').describe()


# In[39]:


pd.set_option('display.max.rows', 187)


# In[40]:


d2= df.groupby('Region').describe()
d2


# In[41]:


d2['Confirmed'].sort_values(by= 'count', ascending= False).head(10)


# In[ ]:




