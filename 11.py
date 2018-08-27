
# coding: utf-8

# In[4]:


def Area (radius):
    PI = 3.14
    area = float (PI * radius * radius)
    return area
def Area_triangle(h,b):
    areat=float(h*b)
    return areat
def Area_square(a):
    areas=float(a*a)
    return areas

radius = int (input("enter radius"))
h= float(input("enter height"))
b=float(input("enter base"))
a=float(input("enter side of square"))


print("area of circle:" ,Area(radius))
print("area of triangle:", Area_triangle(h,b))
print("area of square:", Area_square(a))

