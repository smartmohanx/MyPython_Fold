#What is monkey patching in Python?
'''
MONKEY PATCHING:
In python, the term monkey patch refers to dynamic (or run time)
modifications of a class or module.
In python, we can actually change the behavior of code at run-time.

'''
#EXAMPLE;
#--------------------------------------------------------
# #monk.py  #create a .py file and put this code into it.
# class A:
#     def func(self):
#         print("func() is being called.")
#--------------------------------------------------------
# import monk
# def monkey_func(self):
#     print("monkey() is being called.")

# obj = monk.A()
# obj.normal_func()
# #-------------------------------
# monk.A.normal_func = monkey_func #monkey_func is replacing
# obj = monk.A()
# obj.normal_func()
