#ID-->20CE008
#Name-->Jay Bhimani
# (A) Write a Python program to create a tuple with different data types.
print("---------------------Tuple(A)---------------------")
tp1=('Jay bhimani',800,2.58,True,"CSPIT")
print(tp1)
print(type(tp1))

# (B) Write a Python program to create a tuple with numbers and print one item.
print("---------------------Tuple(B)---------------------")
tp2=(39,8,6,4,42,52,57,58)
print(tp2)
print("0 index Element:",tp2[0])

# (C) Write a Python program to add an item in a tuple.
print("---------------------Tuple(C)---------------------")
print("Quesion: Write a Python program to add an item in a tuple.")
print("Answer : Tuple is unchangeable.")
tp3=(39,8,6,4,42)
print("Tuple:",tp3)
tp3=tp3+(52,)
print("Tuple:",tp3)
tp3=tp3+(57,)
print("Tuple:",tp3)
tp3=tp3+(58,)
print("Tuple:",tp3)

# (D) Write a Python program to convert a tuple to a string.
print("---------------------Tuple(D)---------------------")
tp4=("hello","Jay.","Welcome","to","Charusat","Univercity.")
joint=" ".join(tp4)
print(joint)
print(type(joint))
   #-->convert data type tuple to string
TtoS=str(tp4)
print(type(TtoS))


# (E) Write a Python program to find the length of a tuple.
print("---------------------Tuple(E)---------------------")
tp5=(39,8,6,4,42,52,57,58)
print(tp5)
print("Length:",len(tp5))