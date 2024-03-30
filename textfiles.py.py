#!/usr/bin/env python
# coding: utf-8

# In[1]:


person = " Maya"


# In[2]:


print(f"My name is {person}")


# In[3]:


d = {'a': 7203, 'b': 2034}


# In[2]:


d = {'a': 7203, 'b': 2034}
print(f"my number is {d['a']}")


# In[3]:


my_list = [0,1,2]
print(f"my number is {my_list[1]}")


# In[ ]:


#alignment and padding 


# In[6]:


library = [('Author','Topic','Pages'),('Pickman','Contracts','457'),('Ikenna','Economics','350'),('Ramirez','Family Law','227')]
library        


# In[7]:


for book in library: 
    print(book)


# In[8]:


# print only the authors
for book in library: 
    print(book[0])


# In[12]:


for book in library: 
    print(f"Author is {book[0]}")


# In[13]:


for author, topic, pages in library: 
    print(f"{author} {topic} {pages}")


# In[14]:


#passing in a minimum width 


# In[18]:


for author, topic, pages in library: 
    print(f"{author:{10}} {topic:{30}} {pages:->{10}}")


# In[23]:


#Date formating, helpful website, strftime.org


# In[25]:


from datetime import datetime


# In[30]:


today = datetime(year=2024,month= 3,day=24)
print(f"{today:%B %d, %Y}")


# In[ ]:




