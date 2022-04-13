# ID-->20CE008
# Name-->Jay Bhimani 
# GitHub Link--> https://github.com/jbv1211/Python-Assignment-.git


def maxArea(A, Len):
    area = 0
    for i in range(Len):
        for j in range(i + 1, Len):\
            area = max(area, min(A[j], A[i]) * (j - i))
    return area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height,len(height)))

height = [1,1]
print(maxArea(height,len(height)))