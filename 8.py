
# coding: utf-8

# In[4]:


tuple_a = ('Apple', 'Banana', 'Orange', 'Grapes')
tuple_b = ('Potato', 'Brinjal', 'Carrot', 'tomato')
my_list = list(zip(tuple_a,tuple_b))
for val in range(len(my_list)):
	print (my_list[val])

