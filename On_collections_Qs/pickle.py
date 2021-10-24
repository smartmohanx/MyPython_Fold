#What is pickling and unpickling?
'''

Python pickle module is used for serializing
and de-serializing python object structures.
The process to converts any kind of python objects
(list, dict, etc.) into byte streams (0s and 1s) is called pickling
or serialization or flattening or marshalling.

We can converts the byte stream (generated through pickling)
back into python objects by a process called as unpickling.

Pickling: It is a process where a Python object hierarchy is converted into a byte stream. 
Unpickling: It is the inverse of Pickling process where a byte stream is converted into an object hierarchy. 
 
Why Pickle?: In real world sceanario, the use pickling and unpickling
are widespread as they allow us to easily transfer data from one server/system
to another and then store it in a file or database.


'''

# #pickling example
# lis = [1,2,3,0,4,9,5,6,8,7]
# import pickle
# file = open("employee_info.txt","wb")
# pickle.dump(lis,file)
# file.close()
# print("Data Written to File")

##unpickling example;
# import pickle
# file = open("employee_info.txt","rb")
# lis = pickle.load(file)
# print(lis)
# file.close()
