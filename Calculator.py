#!/usr/bin/env python
# coding: utf-8

# In[2]:


a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number:"))
print('Select to perform operation')
print("1. add")
print("2. subtract")
print("3. product")
print("4. division")
print("5. modulus")
print("6. exp")
choice= int(input("Enter the choice: "))
if choice== 1:
    add= a+b
    print("The result is: ",add)
elif choice== 2:
    sub= a-b
    print("The result is: ",sub)
elif choice== 3:  
    product= a*b
    print("The result is: ",product)  
elif choice== 4:
    div= a/b
    print("The result is: ",div)  
elif choice== 5:
    modulus= a%b
    print("The result is: ",modulus) 
elif choice== 6:
    exp= a**b
    print("The result is: ",exp)
else:
    print("Error")    


# In[ ]:




