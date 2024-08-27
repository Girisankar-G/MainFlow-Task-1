"""
Python variables
    *There is no need of specifying the type of variables in python
    *Python automatically takes the type of value
    *Variables have to be defined with restriction like no specialcharacters
     or keywords and some other rules
"""

#These are some of the most used datatypes
Integer=12
Float=12.00
String="Hello World"
Boolean=True

"""
How to print?
    print("COntent")
    In python for printing is done by giving strings,numbers,variables as it is
"""
print("Hello World")
print(Integer)
print(10)

"""
Python Arithmetics
    *Python supports various operations like addition,subraction etc
    *Python also has inbuilt library for many mathematical operations
     that is under math library
"""
#Arithmetic operations
a=10
b=12
print(a+b,b-a,b/2,b%3)

"""
String Manipulation
    Strings can be manipulated using slicing and inbuilt function
"""
print(String[::-1])#Reversing using slicing
print(String+" printing")#Concatenation
print(len(String))#To find length using inbuilt function

"""
Conditional Statements
    if
    if...else
    if...elif...else
"""
if(a>10):#If false then only goes for elif
    print("a is greater than 10")
elif(a>15):
    print("a is grater than 15")
else:
    print("value of a is ",a)


"""
Data Structures
    1.List(Group of differentelements)
    2.Dictionary(Key Value based)
    3.Tuples(Imutable)
"""
#List
List=[1,2,"abc",3,4,5]
print(List[2])

#Dictionary
Dict={
    1:"Abc",
    2:"Def",
    3:345
    }
print(Dict[2])
#Tuple
a=(1,3,2)
print(a)
a[1]=4



