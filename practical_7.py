# ID-->20CE008
# Name-->Jay Bhimani
# GitHub Link--> https://github.com/jbv1211/Python-Assignment-.git

#-----------------------------QUESTION-----------------------------------------
'''
Lapindrome is defined as a string which when split in the middle,
gives two halves having the same characters and same frequency of each character.
 If there are odd number of characters in the string, we ignore the middle character and check for lapindrome.
 For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency.
 Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
 The two halves contain the same characters but their frequencies do not match. Your task is simple.
 Given a string, you need to tell if it is a lapindrome.
'''

from tokenize import String


def Lapindrome(str):

    strlen = len(str)
    print(strlen)
    if(strlen%2==0):
        a = str[:(strlen//2)]
        b = str[(strlen//2):]
    else:

        a = str[:(strlen//2)]
        b = str[(strlen//2)+1:]
        print(b)
    list_a = list(a)

    list_a.sort()
    print(list_a)
    list_b = list(b)

    list_b.sort()
    print(list_b)
    if (list_a==list_b):
        print("YES")
    else:
        print("NO")

a = int(input())

for i in range(a):
    String =  input()
    Lapindrome(String)