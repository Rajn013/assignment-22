#!/usr/bin/env python
# coding: utf-8

# 1. What is the result of the code, and explain?
# 
# 
# >>> X = 'iNeuron'
# >>> def func():
# print(X)
# 

# In[3]:


X = 'iNeuron'
def func():
    print(X)
func()


# 2. What is the result of the code, and explain?
# 
# 
# >>> X = 'iNeuron'
# >>> def func():
# X = 'NI!'
# 
# 
# >>> func()
# >>> print(X)
# 

# The output of the code will be "iNeuron".
# 
# This is because the function func() defines a new variable X inside its local scope which shadows the global variable X. The global variable X remains unaffected by the assignment inside the function. When the function is called, it does not return or print anything. Then, outside of the function, when print(X) is called, it refers to the global variable X which still holds the value "iNeuron".
# 

# 3.What does this code print, and why?
# 
# 
# >>> X = 'iNeuron'
# >>> def func():
# X = 'NI'
# print(X)
# 
# 
# >>> func()
# >>> print(X)

# In[ ]:


NI
iNeuron


# 4. What output does this code produce? Why?
# 
# 
# >>> X = 'iNeuron'
# >>> def func():
# global X
# X = 'NI'
# 
# 
# >>> func()
# >>> print(X)

# The output of the code will be "NI".
# 
# The function func() uses the global keyword to indicate that it will be using the global variable X. Then, when the function is called, it changes the value of the global variable X to "NI". Therefore, when print(X) is called outside the function, it refers to the updated value of the global variable X, which is "NI".

# 5. What about this code—what’s the output, and why?
# 
# 
# >>> X = 'iNeuron'
# >>> def func():
# X = 'NI'
# def nested():
# print(X)
# nested()
# 
# 
# >>> func()
# >>> X
# 

# The output of the code will be:
# 
# NI
# 'iNeuron'
# 
# The function func() defines a local variable X which is assigned the string value "NI". Then, it defines another function nested() which prints the value of X within the scope of func(). When func() is called, it also calls nested() which prints "NI". However, when print(X) is called outside of the function, it refers to the global variable X which still holds the value "iNeuron". Therefore, the output is "NI" followed by "iNeuron".

# 6. How about this code: what is its output in Python 3, and explain?
# 
# 
# >>> def func():
# X = 'NI'
# def nested():
# nonlocal X
# X = 'Spam'
# nested()
# print(X)
# 
# 
# >>> func()

# In[ ]:


The output of the code will be "Spam".

