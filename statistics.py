
# coding: utf-8

# In[2]:

from collections import Counter
import linear_algebra as la
import math


# In[7]:

def mean(vec):
    return sum(vec) / len(vec)


# In[9]:

def median(vec):
    sorted(vec)
    size = len(vec)
    if (size % 2 != 0):
        i = int(((size-1)/2)-1)
        return vec[i]
    else:
        m = int(size / 2)
        return (vec[m] + vec[m-1]) / 2


# In[11]:

def mode(vec):
    counts = Counter(vec)
    max_count = max(counts.values())
    return [x for x , count in counts.items()
           if count == max_count]


# In[13]:

def data_range(vec):
    return max(vec) + min(vec)


# In[17]:

def deviation(vec):
    pop_mean = mean(vec)
    return [x_i - pop_mean for x_i in vec]


# In[21]:

def squared_deviation(vec):
    pop_mean = mean(vec)
    return [(x_i - pop_mean)**2 for x_i in vec]


# In[23]:

def variance(vec):
    return mean(squared_deviation(vec))


# In[25]:

from math import sqrt


# In[28]:

def standard_deviation(vec):
    return sqrt(variance(vec))


# In[36]:

def sample_standard_deviation(vec):
    return sqrt(sum(squared_deviation(vec)) / (len(vec) - 1))


# In[43]:

def covariance(vec1, vec2):
    n = len(vec1)
    return la.dot_product(deviation(vec1), deviation(vec2)) / (n-1)


# In[46]:

def correlation(vec1, vec2):
    stdev_1 = standard_deviation(vec1)
    stdev_2 = standard_deviation(vec2)
    if (stdev_1 > 0 and stdev_2 > 0):
        return covariance(vec1, vec2) / stdev_1 / stdev_2
    else:
        return 0 #se nao houver amplitude a correlacao eh zero

