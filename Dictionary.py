#ID-->20CE008
#Name-->Jay Bhimani
# (A) Write a Python script to check whether a given key already exists in a dictionary.
print("-------------------Dictionary(A)---------------------")
dict1={'Jay':'19','Deep':'22','Hinal':'18','Meet':'19','Nilesh':'24','Sharad':'25','Harmi':'17','Aniket':'29'}
fname=input("Enter the Your Name:")

if fname in dict1:
    print("your name is exists in dictionary.")
else:
    print("Your name is not exists in distionary")


# (B) Write a Python script to merge two Python dictionaries.
print("-------------------Dictionary(B)---------------------")
dict2={'A':'100','B':'400','C':'20','D':'454'}
dict3={'F':'52.2','G':'587.10'}
combined_dict={**dict2,**dict3}
print("Merge Dictionary:")
print(combined_dict)

# (C) Write a Python program to sum all the items in a dictionary.
print("-------------------Dictionary(C)---------------------")
dict4={'A':100,'B':400,'C':20,'D':454}
sum=0
for x in dict4.values():
    sum=sum+x
print("Sum of All items:",sum)

# (D) Write a Python script to add a key to a dictionary.
#     Sample Dictionary : {0: 10, 1: 20}
#     Expected Result : {0: 10, 1: 20, 2: 30}
print("-------------------Dictionary(D)---------------------")
dict5={0: 10, 1: 20}
print("Old Dictionary")
print(dict5)
  #UPDATE Syntax
dict5.update({2:30})
dict5[2]=30
print("After add key :")
print(dict5)


# (E) Write a Python script to concatenate following dictionaries to create a new one.
#     Sample Dictionary : dic1={1:10, 2:20}
#                         dic2={3:30, 4:40}
#                         dic3={5:50,6:60}
#     Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("-------------------Dictionary(E)---------------------")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

combined_dict1={**dic1,**dic2,**dic3}
print(combined_dict1)