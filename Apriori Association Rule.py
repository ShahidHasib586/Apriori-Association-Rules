#!/usr/bin/env python
# coding: utf-8

# # Apriori
# 

# ## importing the libraries

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)


# In[4]:


dataset


# ### Dataset processing

# In[5]:


transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])


# In[6]:


transactions


# ## Training Apriori on the dataset

# In[7]:


get_ipython().system('pip install apyori')


# In[8]:


from apyori import apriori


# In[9]:


rules = apriori(transactions, min_support = 0.003, min_confidence = 0.4, min_lift = 3, min_length =2)


# ### Visualising the result

# In[10]:


results = list(rules)


# In[11]:


results


# In[ ]:




