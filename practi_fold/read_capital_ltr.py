"""Write a one-liner that will count the number of capital letters in a
file. Your code should work even if the file is too big to fit in memory.
"""
# text = "hello MOHAn, I AM pytHON. HOw Can i helP YOU."
# count = 0
# for i in text:
#     if i.isupper():
#         count = count+1
# print(count) #it prints all Capital letters in a str.

# count = 0
# for i in text:
#     if i.isspace():
#         count = count+1
# print(count) #it prints all whitespaces in a str.
"""
#one line code here:

text = "helP2 YOU1."
print([char for letter in text for char in letter if char.isupper()]) 
print(len([char for letter in text for char in letter if char.isupper()])) 
'''
EXPLAIN:
char is gathering all letters:
char;
for letter in text,
for char in letter,
condition;
    if char.isupper() #find all upper chars.

'''
"""
# test:
# txt = "hello mohan i am python 2.9 version, ok na"
# print([letter for i in txt for letter in i if letter == 'm'])







file = open('demo1.txt','r')
text = file.read()
#print([letter for i in text for letter in i if letter.isupper()])
print(len([letter for i in text for letter in i if letter.isupper()]))