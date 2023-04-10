"""
PS: "Write a Python program to store marks scored in subject “Fundamental of Data 
Structure” by N students in the class. Write functions to compute following:
a) The average score of class 
b) Highest score and lowest score of class 
c) Count of students who were absent for the test
d) Display mark with highest frequency"
"""

#Assignment 2
n=int(input("enter no. of students in class "))
mks=[]
m=int(input("enter no. of students who present in class "))

# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

def enter_mks():
    for i in range(m):              
        #It takes the number of students in a class as input and then asks for the marks of each student and stores it in a list
        num=int(input("enter marks of students in class "))
        mks.append(num)
    print(f"marks of students are {mks}")

# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

def average():              
    #It calculates the average of the marks in the list `mks` and prints it"""
    sum=0
    for i in mks:
        if i!=-1:
            sum=sum+i
    avg=sum/len(mks)
    print(f"Average of marks is {avg}")

# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

def highest():              
    """It takes the first element of the list and compares it to the rest of the elements in the list. If any of the elements are greater
    than the first element, it replaces the first element with the greater element. It then prints the highest score of the class"""
    max=mks[0]
    for i in mks:
        if i>max:
            max=i
    print(f"highest score of class is {max} ")

# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

def lowest():               
    """It loops through the list of marks, and if the mark is not -1, it checks if it is less than the current minimum. If it is, it sets 
    the minimum to that value"""
    min=mks[0]
    for i in mks:
        if i != -1:
          if i<min:
            min = i
    print(f"lowest score of class is {min} ")

# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

def frequency():
    """In this function we  creates two lists, one for the values and one for the frequencies. It then iterates through the list of marks, and if the mark is 
    already in the list of values, it increments the frequency of that value by 1. If the mark is not in the list of values, it adds the mark to the list of 
    values and adds 1 to the list of frequencies"""
    freq=[]
    value=[]
    for i in mks:
        if i in value:
            freq[value.index(i)]+=1
        else:
            value.append(i)
            freq.append(1)

    frequ=max(freq)
    vvalue=freq.index(frequ)
    print(f"marks with highest frequency is {value[vvalue]}" )
    print(f"number of times high no has occured is {frequ} ")

# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

def absent():
    """
    The function counts the number of absent students for a test.
    """
    count=0
    for j in range(n):
        if j not in range(m):
            count+=1
    print(f"number of students who where absent for the test is {count}")

enter_mks()
average()
highest()
lowest()
absent()
frequency()

# suggestion: you can give choice also to call the functions