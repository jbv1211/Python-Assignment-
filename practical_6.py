# ID-->20CE008
# Name-->Jay Bhimani
# GitHub Link--> https://github.com/jbv1211/Python-Assignment-.git

#-----------------------------QUESTION-----------------------------------------
'''AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.
'''

n = int(input())
word_list = []
for i in range(n):
    word_list.append(input())

New_word_list = []
for element in word_list:
    if element in New_word_list:
        New_word_list = New_word_list
    else:
        New_word_list.append(element)

print(len(New_word_list))
for element in New_word_list:
    print(word_list.count(element), end=" ")