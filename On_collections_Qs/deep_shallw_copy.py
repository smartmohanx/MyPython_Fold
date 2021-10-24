# '''
# SHALLOW AND DEEP COPPY:

# In Python, we use '=' operator to create a copy of an object.
# a = 10
# b = a
# You may think that this creates a new object; it doesn't.
# It only creates a new variable that shares the reference of the
# original object.

# sometimes we want to change new modified values
# not original values,or vice versa.
# In Python, there are two ways to create copies:

# 1. Shallow Copy
# 2. Deep Copy

# 'To make these copy work, we use the copy module.
# import copy --------------------- copy Module'

# SHALLOW COPY:
# A shallow copy creates a new object which stores the reference of
# the original elements.
# '''
# #EXAMPLE:
# import copy as cp
# x = [1,2,3,4,5,6]
# y = cp.copy(x)
# print(x)
# print(y)
# x[2] = 9
# print(x)
# print(y)

# print("==============================")
# ''''
# NOTE: Shallow copy is not applicable for nested objects.

# DEEPCOPY:
# A deep copy creates a new object and recursively adds the copies of
# nested objects present in the original elements.
# '''
# #EXAMPLE:
# import copy as cp
# x = [11,22,33,[11,22],44,55]
# y = cp.deepcopy(x)
# print(x)
# print(y)
# x[3][0] = 99
# print(x)
# print(y)
