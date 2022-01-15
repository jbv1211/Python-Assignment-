#ID-->20CE008
#Name-->Jay Bhimani
# (A) Write a Python program to add member(s) in a set and clear a set
print("---------------------Set(A)---------------------")
st1={39,8,12,13,14,52,39}
print("The set is -",st1)
st1.add(78)
print("The set after adding 78 is -",st1)
st1.clear()
print("The set is after clear -",st1)


# (B) Write a Python program to remove an item from a set if it is present in the set.
print("---------------------Set(B)---------------------")
st2={39,8,12,13,14,52,39}
print("Before Removing SET is -->",st2)
item=int(input("Enter remove element:"))
if(item in st2):
    st2.remove(item)
    print("After Removing element set is -",st2)
else:
    print("Elemnt is not found...\nSet is- ",st2)


# (C) Write a Python program to create an intersection, Union, difference of sets.
print("---------------------Set(C)---------------------")
# sets are define
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print("Set A is ",A)
print("Set B is ",B)

# union
print("Union :", A | B)

print('A Union B using funtion =', A.union(B))

# intersection
print("Intersection :", A & B)
print('A intersection B using funtion=', A.intersection(B))

# difference
print("A Difference B :", A - B)
print("B Difference A :", B - A)

# Equivalent to A-B
print('A Difference B using funtion =', A.difference(B))

# Equivalent to B-A
print('B Difference A using funtion =', B.difference(A))


# (D) Write a Python program to find maximum and the minimum value in a set.
print("---------------------Set(D)---------------------")
st3={39,8,12,13,24,14,31,39}
print("The set is ",st3)
print("Maximum value in set ",max(st3))
print("Minimum value in set ",min(st3))


# (E) Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
print("---------------------Set(E)---------------------")
#********** Frequncy count in List ***************
List = [2, 1, 2, 2, 1, 3]
counter = 0
num = List[0]
for i in List:
    # The count() method returns the number of occurrences of a number in the given List.
    curr_frequency = List.count(i)
    if (curr_frequency > counter):
         counter = curr_frequency
         num = i

print("(1) List = ",List)
print("   -->Most common elements is : ",num)
print("   -->Most repeted number is: ", counter)

#********** Frequncy count in Tuple ***************
tuple=(1,2,4,5,6,6,3,6,8,3,6)
L=list(tuple)
counter1 = 0
num1 = L[0]
for i in L:
#The count() method returns the number of occurrences of a number in the given Tuple.
    curr_frequency = L.count(i)
    if(curr_frequency> counter1):
        counter1 = curr_frequency
        num1 = i
print("(2) Tuple-",tuple)
print("   -->Number which is repeted most: ",num1)
print("   -->Most repeted number is: ",counter1)


# ********** Frequncy count in Dictionary ***************
dic={1:'meet',2:'harmi',3:'hinal',4:'aniket',5:'jay',6:'hinal',7:'harmi',8:'hinal',9:'bhavdeep'}
#values() method returns list of all values which are in dictionary
value=dic.values()
#convert values in list to count frequncy
l1=list(value)
counter1 = 0
name= list(l1[0])
for i in l1:
    curr_frequency = l1.count(i)
    if(curr_frequency> counter1):
        counter1 = curr_frequency
        name = i
print("(3)Dictionary-",dic)
print("   -->Name which is repeted most: ",name)
print("   -->Most repeted name is: ",counter1)


