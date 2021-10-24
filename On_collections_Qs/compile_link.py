#What is the process of compilation and linking in python?
'''
Compilation:
The source code in python is saved as a .py file which is then compiled into
a format known as byte code, byte code is then converted to machine code.
After the compilation, the code is stored in .pyc files and is regenerated
when the source is updated. This process is known as compilation.

.py>byteCode>>machineCode>.pyc

Linking:
Linking is the final phase where all the functions are linked with their
definitions as the linker knows where all these functions are implemented.
This process is known as linking.

.py>byteCode>>machineCode>.pyc>>linker
'''

import dis
def recursive_sum(n):
    """Function to return the sum of recursive numbers"""
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)

# change this value for a different result
number = 16
if number < 0:
    print("The sum is",recursive_sum(number))
# by using dis module ,the bytecode is loaded into machine code ,and a piece of code that reads each instruction in the bytecode and executes whatever operation is indicated.
dis.dis(recursive_sum)