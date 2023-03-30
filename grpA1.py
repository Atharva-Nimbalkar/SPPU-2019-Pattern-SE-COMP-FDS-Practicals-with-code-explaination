""" 
Promblem Statement :

 In second year computer engineering class, group A student’s play cricket, group B 
students play badminton and group C students play football. 
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton 
b) List of students who play either cricket or badminton but not both 
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET 
built-in functions) 

"""
SEComp =[]
# //cricket

# Taking input from user and storing it in a list.
n = int(input("\nEnter number of students in SE COMP: ")) 
print("Enter the names of",n,"students :")
for i in range(0, n):
    x = input()
    SEComp.append(x)
print("Original list of students in SEComp : ",SEComp)

# <--------------------------------------------------------------------------------------------------------->

Cricket =[]
n = int(input("\n\nEnter number of students who play cricket : "))
print("Enter the names of",n,"students who play cricket : ")
for i in range(0, n):               # A for loop that will run n times.
    y = input()
    Cricket.append(y)               # Adding the value of y to the list Cricket.
print("Original list of students playing cricket is :" ,Cricket)

# <--------------------------------------------------------------------------------------------------------->

badminton =[]
n = int(input("\n\nEnter number of students who play badminton : "))
print("Enter the names of",n,"students who play badminton : ")
for i in range(0, n):               #same explaination as for cricket list
    y = input()
    badminton.append(y)
print("Original list of students playing badminton is :" ,badminton)

# <--------------------------------------------------------------------------------------------------------->

football =[]
n = int(input("\n\nEnter number of students who play football : "))
print("Enter the names of",n,"students who play football : ")
for i in range(0, n):               #same explaination as for cricket list
    y = input()
    football.append(y)
print("Original list of students playing football is :" ,football)

# <--------------------------------------------------------------------------------------------------------->

#List of students who play both cricket and badminton

c_b=[]

for i in Cricket:               #line 54-59 Checking if the name in the list Cricket is also in the list badminton. If it is, it adds it to the  list c_b.
    for j in badminton:
        if i ==j:
            c_b.append(i)
        else:
            pass
print("List of students who play both cricket and badminton:",c_b)

# <--------------------------------------------------------------------------------------------------------->

#List of students who play either cricket or badminton but not both

only_cb=[]

for i in Cricket:               # Checking if the name in the list Cricket is also in the list badminton. If it is, it adds it to the  list only_cb.
    if i not in badminton:
        only_cb.append(i)
for i in badminton:
    if i not in Cricket:
        only_cb.append(i)

print(" List of students who play either cricket or badminton but not both:",only_cb)

# <--------------------------------------------------------------------------------------------------------->

#Number of students who play neither cricket nor badminton

nc_nb=[]
for i in football:
    nc_nb.append(i)             # Adding all the names in the list football to the list nc_nb.


for i in Cricket:               # Checking if the name in the list Cricket is also in the list nc_nb. If it is, it removes it from the  list nc_nb.
    for j in nc_nb:
        if i==j:
            nc_nb.remove(i)

for i in badminton:
    for j in nc_nb:
        if i==j:
            nc_nb.remove(i)

print("Number of students who play neither cricket nor badminton",nc_nb)

# <--------------------------------------------------------------------------------------------------------->

#Number of students who play cricket and football but not badminton.

fc_f_nb=[]
for i in Cricket:               # Checking if the name in the list Cricket is also in the list football. If it is, it adds it to the list fc_f_nb.
    for j in football:
        if i==j:
            fc_f_nb.append(i)


for i in fc_f_nb:               # Checking if the name in the list fc_f_nb is also in the list badminton. If it is, it removes it from the list fc_f_nb.
    for j in badminton:
        if i==j:
            fc_f_nb.remove(i)

print("Number of students who play cricket and football but not badminton:", fc_f_nb)

# <------------------------------------------------------------------The End------------------------------------->







