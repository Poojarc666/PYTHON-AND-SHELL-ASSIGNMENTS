
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np 
from pandas import DataFrame

df = pd.DataFrame({'regno': ["01","02","03"], 'name': ["aaa","bbb","ccc"]})

df.columns = ['regno','name']
print(df)

regno=["01","02","03"]
name=["aaa","bbb","ccc"]
df = {'regno': [], 'name': []}
df['regno'].append(regno)
df['regno'].append(name)
print(df['regno'])

