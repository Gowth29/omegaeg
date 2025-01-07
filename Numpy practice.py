#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
#create 1d array
arr=np.array([1,2,3,4,5])
print("1D Arraay: ", arr)


# In[6]:


#create 2D array
arr2=np.array([[1,2,3],[4,5,6]])
arr2


# In[37]:


#create 3D array
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr3


# In[13]:


#Array properties
print("\n Array properties:")
print("Shape: ", arr2.shape)
print("Size: ",arr2.size)
print("Data type: ", arr2.dtype)


# In[14]:


ze=np.zeros((2,3))
ze


# In[16]:


one=np.ones((3,4,5))
one


# In[20]:


id1=np.eye(10)
id1


# In[23]:


arr_arrange=np.arange(0,10,5)
arr_arrange


# In[27]:


line_array=np.linspace(0,2000,5)
line_array


# In[28]:


arr_a=np.array([[1,2,3]])
arr_b=np.array([[4,5,6]])
add=arr_a+arr_b
add


# In[29]:


mul=arr_a*arr_b
mul


# In[30]:


scal_mul=arr_a*3
scal_mul


# In[34]:


mat_a=([[1,2],[4,5]])
mat_b=([[7,8],[10,11]])
mul2=np.dot(mat_a,mat_b)
mul2


# In[42]:


arr_1=np.array([13,23,56,78,98,45,34,42])
print("slicing: ", arr_1[2:4])


# In[53]:


print("sum: ",arr_1.sum())
print("mean: ",arr_1.mean())
print("standard deviation: ",arr_1.std())
print("maximum: ",arr_1.max())
print("minimum: ",arr_1.min())


# In[55]:


#Reshape array
arr_re=arr_1.reshape(2,4)
arr_re


# In[56]:


ran_arr=np.random.random((3,4))
ran_arr


# In[58]:


ran_int=np.random.randint(1,10,size=(2,3))
ran_int


# In[59]:


import pandas as pd


# In[ ]:





# In[ ]:




