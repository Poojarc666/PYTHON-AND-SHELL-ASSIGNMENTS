
# coding: utf-8

# In[7]:


def uppercase(str_data):
    result = ''
    for char in str_data:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result
print(uppercase('abcde--#λ'))

