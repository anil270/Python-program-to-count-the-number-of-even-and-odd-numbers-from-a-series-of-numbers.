#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to count the number of even and odd numbers from a series of numbers.

# In[63]:


numberseries = int(input())
print("Series of numbers :")
count = 0
count1 = 0
for x in range(1,numberseries):
    if x%2==0:
        count = count + 1
    else:
        count1 = count1 + 1
    print(x) 
print("Number of even numbers =",count)
print("Number of odd numbers =",count1)


# In[ ]:




