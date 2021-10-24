
#How is memory managed in Python?
'''
ans:- Memory management is a process of allocating and
de-allocating memory and it also involves cleaning memory
which no reference is pointing to an object and that obj
no longer being accessed or used,that obj removes from heap memory.
this process is done by automatically through the barbage collector.

EXAMPLE:
x = 15  #x is known or allocated and 15 is int obj.
print(x)
output-15
----------
del x
print(x)       #x is de-allocated.
output- name 'x' is not defined.

'''

'''
#MEMORY MANAGEMENT IN PYTHON.

In python, Memory management is the process of efficiently
allocating, de-allocating memory so that all the different
processs run smoothly and can optimally access different
system resouces.
Memory management also involves cleaning memory of objects
that are no longer being used or accessed,that process is done
through the garbage collector.

example:
x = 15  #x is known or allocated and 15 is int obj.
print(x)
output-15
----------
del x
print(x)       #x is de-allocated.
output- name 'x' is not defined.

#GARBAGE COLLECTION.

It is a process in which the interpreter frees up
the memory when object not in use to make it availabe
for other objects.
Assume a case where no reference is pointing to an object in memory
i.e it is not in use so, the virtual machine has a garbage collector
that automatically deletes that object from the heap memory.

HEAP MEMORY: it holds all objects and other data structures, that will
be used in the program.
'''
