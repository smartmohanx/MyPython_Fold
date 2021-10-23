#How can you generate random numbers in Python?
'''
There is a need to generate random numbers by using the random module.

Generating a Single Random Number:
The random() method in random module generates a float number between 0 and 1.

Example
import random
n = random.random()
print(n)  #0.2112200


Generating Number in a Range:
The randint() method generates a integer between a given range of numbers.

Example
import random
n = random.randint(0,22)
print(n)  #2



Generating a List of numbers Using For Loop:

We can use the above randint() method along
with a for loop to generate a list of numbers.
We first create an empty list and then append
the random numbers generated to the empty list one by one.

Example

import random
lis = []
for i in range(0,5):
    x = random.randint(0, 100)
    lis.append(x)
print(lis)



Using random.sample()
We can also use the sample() method available
 in random module to directly generate a list of random numbers.
 Here we specify a range and give how many random numbers we need to generate.

Example
import random
#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30), 5)
print(randomlist)
Output
Running the above code gives us the following result −

[16, 19, 13, 18, 15]
'''