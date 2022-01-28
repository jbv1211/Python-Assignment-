# ID-->20CE008
# Name-->Jay Bhimani
# GitHub Link--> https://github.com/jbv1211/Python-Assignment-.git

#-----------------------------QUESTION-----------------------------------------

# Given the participants
# ' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
#
# Input Format: The first line contains.The second line containsan array A[] of n integers each separated by a space.
#
# Constraints:
# Output
# Format: Print the runner - up score.
#
# Sample Input
# 5
# 23665
#
# Sample Output
# 5
# Explanation: Given list is [2, 3, 6, 6, 5].The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner - up score.

n = int(input())
arr =list(map(int, input().split()))
arr.sort()
print(arr[(arr.index(max(arr)))-1])