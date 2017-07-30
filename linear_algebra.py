
# coding: utf-8

# In[1]:

def vector_add(vec1, vec2):
    return [v1i+ v2i
           for v1i, v2i in zip(vec1, vec2)]


# In[5]:

def vector_subtract(vec1, vec2):
    return [v1i -  v2i
           for v1i, v2i in zip(vec1, vec2)]


# In[8]:

from functools import reduce

def vector_sum(vectors):
    return reduce(vector_add, vectors)


# In[11]:

def scalar_mult(scalar, vector):
    return [ scalar * vi for vi in vector]


# In[13]:

def dot_product(vec1, vec2):
    return sum(v1i * v2i
              for v1i , v2i in zip(vec1, vec2))


# In[15]:

def sum_of_squares(vec):
    return dot_product(vec, vec)


# In[17]:

import math

def magnitude(vec):
    return math.sqrt(sum_of_squares(vec))


# In[19]:

def distance(vec1, vec2):
    return magnitude(vector_subtract(vec1, vec2))


# In[21]:

def is_orthogonol(vec1, vec2, tolerance=1e-10):
    return abs(dot_product(vec1, vec2)) < tolerance;


# In[25]:

def is_zero(vec, tolerance=1e-10):
    return magnitude(vec) < tolerance


# In[26]:

from math import pi

def angle(vec1, vec2, in_degrees = False):
    return 0;


# In[27]:

def is_parallel(vec1, vec2):
    return (is_zero(vec1) or
           is_zero(vec2) or
           angle(vec1,vec2) == 0 or
           angle(vec1,vec2) == pi)

