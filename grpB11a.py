"""PS : a) Write a python program to store roll numbers of student in array who attended
training program in random order. Write function for searching whether particular
student attended training program or not, using Linear search and Sentinel search. """


"""This below code is taking input from the user for the total number of students who attended the training
 program and their roll numbers. It is storing the roll numbers in an array called `students_attend`.
 It is also taking input from the user for the roll number that needs to be searched, which is stored
 in the variable `search_element`."""

students_attend = []
n = int(input("Enter the total no. of students who attended the training program. "))
print("Enter the roll no. of students who attended the training program. ")
for i in range(n):
    students_attend.append(int(input()))

search_element = int(input("Enter the roll no. that you want to search : "))

# ----------------------------------------------------------------------------------------------------->

def linear_search(students_attend, search_element):
    """
    The function performs a linear search on a list of students attending a class to find a specific
    element and returns 1 if found, -1 otherwise.
    
    :parameter students_attend: a list of students who attended a class or event
    :parameter search_element: The element that we are searching for in the list of students_attend
    :return: 1 if the search element is found in the list of students' attendance, and -1 if it is not
    found.
    """

    for i in students_attend:
        if i == search_element:
            return 1

    return -1

# -------------------------------------------------------------------------------------->

def sentinel_search(students_attend, search_element, n):
    # Last element of the array
    last = students_attend[n - 1]

    # Element to be searched is placed at the last index
    students_attend[n - 1] = search_element
    i = 0

    while (students_attend[i] != search_element):
        i += 1

    # Put the last element back
    students_attend[n - 1] = last

    if ((i < n - 1) or (search_element == students_attend[n - 1])):
        return 1
    else:
        return -1

# -------------------------------------------------------------------------------------->

print("1) Linear search")
print("2) Sentinal search")
ch = int(input("Enter your choice "))

if ch == 1:
    result = linear_search(students_attend, search_element)
    if result == -1:
        print("The entered roll no. did not attend the training program.")
    else:
        print("The entered roll no. has attended the training program.")

elif ch == 2:
    result = sentinel_search(students_attend, search_element, n)
    if result == -1:
        print("The entered roll no. did not attend the training program.")
    else:
        print("The entered roll no. has attended the training program.")

else:
    print("Sorry wrong choice")