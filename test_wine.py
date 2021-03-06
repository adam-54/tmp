#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
url = 'https://github.com/cbrownley/foundations-for-analytics-with-python/blob/master/statistics/winequality-both.csv?raw=true'
wine = pd.read_csv(url,sep=',',header=0)

print(wine.head(5))

# Display descriptive statistics for all variables
print(wine.describe())

# Identify unique values
print(sorted(wine.quality.unique()))

# Calculate value frequencies
print(wine.quality.value_counts())

# Display descriptive statistics for quality by wine type
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

# Calculate correlation matrix for all variables
print(wine.corr())


# In[ ]:




