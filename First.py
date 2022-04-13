# ID-->20CE008
# Name-->Jay Bhimani 
# GitHub Link--> https://github.com/jbv1211/Python-Assignment-.git

#-----------------------------QUESTION-----------------------------------------
'''
You  are  given  a  string. 
Your  task  is to  count  the  frequency  of  letters  of  the  string  and print the letters in  descending  order  of frequency.
If the  following  string is given  as input to the  program: aabbbccde Then, the  out put  of the  program  should  be: 
b  3
a  2
c  2
d  1
e  1
'''
from collections import Counter

string = input()

count = Counter(string)

for letter,value in count.items():
    print(letter,value)
