#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import diffusion as df


# In[3]:


infile2 = open('/Users/suneherahasib/Desktop/iPad Quarterly Sales 2010 2017.csv', mode = 'r')


# In[4]:


header2 = infile2.readline()
ipad = infile2.readlines()


# In[5]:


ipad_data = []
ipad_data = [line.strip() for line in ipad]
ipad_data = [line.split(',') for line in ipad]
ipad_data


# In[6]:


time = []
number = []
for i in ipad_data:
    time.append(i[0])
    number.append(float(i[1]))
    


# In[7]:


plt.plot(number)
plt.xlabel('Time')
plt.ylabel('Number of units (M)')
plt.title('iPad Sales 2010 - 2017 (M Units)')


# In[ ]:




