#!/usr/bin/env python
# coding: utf-8

# **NUMPY**

# In[3]:


import sys
import numpy as np


# In[4]:


# Creating an Array - One Dimentional Array (Vector)
np.array([1,2,3,4,5])


# In[13]:


a = np.array([1,2,3,4,5])
a


# In[14]:


# Indexing
a[0]


# In[15]:


a[-1]


# In[16]:


a[1:3]


# In[17]:


a[:3]


# In[18]:


# Multi Indexing
a[0],a[2],a[4]


# In[19]:


a[[0, 2, -1]]


# Array Types

# In[20]:


a


# In[21]:


a.dtype


# In[22]:


# Creating an Array and Specify Type
np.array([1,2,3,4,5],dtype=np.float)


# Dimensions and Shape

# In[23]:


# Multi-Dimentional Array - Matrix
# 3 by 3 array
b = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
b


# In[24]:


# 2 by 3 array
c = np.array([[1, 2, 3],[4, 5, 6]])
c


# In[25]:


c.shape


# In[26]:


# Three Dimentional Array
d = np.array([[[1, 2, 3],[4, 5, 6]],
              [[7, 8, 9], [3, 2, 1]]
              ])
d


# In[27]:


d.shape


# In[28]:


# Obtain Dimention
d.ndim


# In[29]:


# Count Elements
d.size


# In[30]:


# Index and Slice Matrix
sq = np.array([
#     0, 1, 2
      [1,2,3], #0
      [4,5,6], #1
      [7,8,9]  #2
               ])


# In[31]:


sq


# In[32]:


sq[1]


# In[33]:


sq[:2, :2]


# In[34]:


sq[0,0] = np.array([9])


# In[35]:


sq


# In[36]:


sq[0] = np.array([9,8,7])


# In[37]:


sq


# Summary Statistics

# In[38]:


# Mean of the Matrix
sq.mean()


# In[39]:


# Sum the entire matrix
sq.sum()


# In[40]:


# Sum of each column
sq.sum(axis=0)


# In[41]:


# Sum of each row
sq.sum(axis=1)


# In[42]:


# Standard deviation of the matrix
sq.std()


# In[43]:


# Standard deviation of each columns
sq.std(axis=0)


# Broadcasting and Vectorized Operations

# In[44]:


a = np.arange(4)
a


# In[45]:


a/10


# In[46]:


a


# In[47]:


a+=2
a


# In[48]:


l = [0,1,2,3]
l


# In[49]:


[i*10 for i in l]


# In[50]:


a = np.arange(4)
a


# In[51]:


b = np.array([5,5,5,5])
b


# In[52]:


a*b


# In[53]:


a/b


# Boolean Arrays

# In[54]:


a = np.arange(4)
a


# In[55]:


a[0], a[-1]


# In[56]:


a[[True, False, False, True]]


# In[57]:


a>=2


# In[58]:


a[a>=2]


# In[59]:


a.mean()


# In[60]:


a[a>a.mean()]


# In[61]:


a[(a==0) | (a==1)]


# In[62]:


A = np.random.randint(100, size=(3,3))
A


# In[63]:


A[np.array([
    [True, False, True],
    [False, True, False],
    [True, False, True]
     ])]


# In[64]:


A>30


# In[65]:


A[A>30]


# Linear Algebra

# In[66]:


A = np.array([
    [1,2,4],
    [4,5,6],
    [7,8,9]
])


# In[67]:


B = np.array([
    [6,5],
    [4,3],
    [7,1]
])


# In[68]:


A.dot(B)


# In[69]:


A@B


# In[70]:


A.T


# In[71]:


A


# In[72]:


B.T @ A


# Size of Objects in Memory

# In[73]:


# An integer is 24bytes
sys.getsizeof(1)


# In[74]:


# Longs are larger
sys.getsizeof(10**100)


# In[75]:


# Numpy is much smaller
np.dtype(int).itemsize


# In[76]:


# List are larger
sys.getsizeof([1])


# In[77]:


# An array of one element in numpy
np.array([1]).nbytes


# Performance

# In[78]:


l = list(range(50))


# In[79]:


a= np.arange(1000)


# In[80]:


get_ipython().run_line_magic('time', 'np.sum(a**2)')


# In[81]:


get_ipython().run_line_magic('time', 'np.sum([x**2 for x in l])')

