"""PS: Write a python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix """

# This code is initializing an empty list `a` and then taking input from the user for the number of
# rows and columns of a matrix and storing them in variables `a_r` and `a_c` respectively.
a=[]
print("enter the order of the matrix")
a_r = int(input("enter number of rows"))
a_c = int(input("enter number of col"))

# It is then printing the matrix in a readable format by iterating over the rows
# and columns of the matrix and printing each element with a space in between.
print("enter the matrix")
for i in range(a_r):
    print("\n")
    b=[]
    for j in range(a_c):
        print("\n")
        num=int(input("enter a value"))
        b.append(num)
    a.append(b)

for i in range(a_r):
    for j in range(a_c):
        print(a[i][j], end=" ")
    print()

#------------------------------------------------------------------------------------------>

# Same explaination like above for another matrix
c=[]
print("enter the order of the matrix")
c_r = int(input("enter number of rows"))
c_c = int(input("enter number of col"))

print("enter the matrix")
# This code is taking input from the user for the number of rows and columns of another matrix and
# storing them in variables `c_r` and `c_c` respectively. It is then initializing an empty list `c`
# and taking input from the user for the values of the matrix and storing them in the list `c`.
for i in range(c_r):
    print("\n")
    d = []
    for j in range(c_c):
        print("\n")
        num = int(input("enter a value"))
        d.append(num)
    c.append(d)

for i in range(c_r):
    for j in range(c_c):
        print(c[i][j], end = " ")
    print()

#------------------------------------------------------------------------------------------>

res=[[0,0,0,0],[0,0,0,0]]
    
"""The function performs matrix addition and stores the result in a new matrix."""
def matrix_add():
    for i in range(c_r):
        for j in range(c_c):
            res[i][j]=a[i][j] + c[i][j]
            print(res[i][j],end=" ")
        print()

"""The function performs matrix subtraction and prints the resulting matrix."""
def matrix_sub():
    
    for i in range(c_r):
        for j in range(c_c):
            res[i][j]=a[i][j]-c[i][j]
            print(res[i][j],end=" ")
        print()

"""This function performs matrix multiplication between two matrices."""
def matrix_mult():
    
    res = []
    if (a_r == c_c):
        for i in range(a_r):
            temp = []
            for j in range(c_r):
                temp.append(0)
            res.append(temp)

        for i in range(len(a)):
            for j in range(len(c[0])):
                for k in range(len(c)):
                    res[i][j] += a[i][k] * c[k][j]

        for i in range(a_r):
            for j in range(c_c):
                print(res[i][j], end=" ")
            print()

"""This function transposes a matrix by printing its columns as rows."""
def matrix_trans():
    print("first matrix")
    for i in range(a_r):
        for j in range(a_c):
            print(a[j][i],end=" ")
        print()

    print("\nsecond matrix")
    for i in range(c_r):
        for j in range(c_c):
            print(c[j][i],end=" ")
        print()

print("addition of ")
matrix_add()

print("subtraction of matrix is")
matrix_sub()

print("multiplication of matrix is")
matrix_mult()

print("transpose of ")
matrix_trans()
