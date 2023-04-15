"""PS: b) Write a python program to store roll numbers of student array who attended training 
program in sorted order. Write function for searching whether particular student 
attended training program or not, using Binary search and Fibonacci search."""

students_attend = []
n=int(input("Enter the total no. of students who attended the training program :"))
print("Enter the roll no. of students who attended the training program :")
for i in range(n):
    students_attend.append(int(input()))

search_element = int(input("Enter the roll no. that you want to search : "))

students_attend.sort()
start = 0

# ----------------------------------------------------------------------------------------------------------->

def bins(students_attend,search_element,start,n):
    """
    This is a recursive binary search function that searches for a given element in a sorted list of
    student attendance records.
    
    :paramter students_attend: a sorted list of integers representing the attendance of students in a class
    :parameter search_element: The element that we are searching for in the list of students_attend
    :parameter start: The starting index of the sub-array being searched
    :parameter n: The total number of elements in the list of students_attend
    :return: the index of the search element in the given list of students' attendance using binary
    search. If the search element is not found in the list, it returns -1.
    """

    if start > n:
        return -1

    mid = (start+n)//2

    if search_element == students_attend[mid]:
        return mid

    if search_element < students_attend[mid]:
        return bins(students_attend,search_element,start,mid-1)
    else:
        return bins(students_attend,search_element,mid+1,n)

# ----------------------------------------------------------------------------------------------------------->

def fibonacci_search(students_attend, search_element, n):
    """
    The function implements the Fibonacci search algorithm to find a specific element in a sorted list
    of students' attendance.
    
    :paramter students_attend: a sorted list of integers representing the number of students attending a
    class on each day
    :parameter search_element: The element that we are searching for in the list of students_attend
    :parameter n: The number of elements in the array "students_attend"
    :return: the index of the search element in the given list of students' attendance using Fibonacci
    search algorithm. If the search element is not found in the list, it returns -1.
    """
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1

    while (fib > 1):

        i = min(offset+fib2, n-1)

        if (students_attend[i] < search_element):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif (students_attend[i] > search_element):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if(fib1 and students_attend[offset+1] == search_element):
        return offset+1

    else:
        return -1

print("1) Binary search")
print("2) Fibonacci search")
ch = int(input("Enter your choice "))

if ch == 1:
    result = bins(students_attend,search_element,start,n-1)
    if result == -1 :
        print("The entered roll no. did not attend the training program.")
    else:
        print("The entered roll no. has attended the training program.")

elif ch == 2:
    result = fibonacci_search(students_attend, search_element, n)
    if result == -1 :
        print("The entered roll no. did not attend the training program.")
    else:
        print("The entered roll no. has attended the training program.")

else:
    print("Sorry wrong choice")