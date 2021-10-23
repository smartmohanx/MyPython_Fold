import random
lis = [0, 1, 2, 3, 4, 5, 'mohan', 7, True, 9]
random.shuffle(lis)
print(lis)

'''
To randomly shuffle the elements of lists in Python, use the random module.
random provides shuffle() that shuffles the original list in place,
and sample() that returns a new list that is randomly shuffled.
sample() can also be used for strings and tuples.

random.shuffle() shuffles the original list
random.sample() returns a new shuffled list
Shuffle strings and tuples
Initialize the random number generator with random.seed()
'''