"""PS : Write a python program to store first year percentage of students in array. Write function 
for sorting array of floating point numbers in ascending order using quick sort and display 
top five scores."""

def swap(arr, i, j):
    """
    The function swaps the elements at two given indices in an array.
    
    :parameter arr: an array that contains elements to be swapped
    :parameter i: The index of the first element to be swapped in the array
    :parameter j: The index of the second element to be swapped in the array
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# --------------------------------------------------------------------------------------------------------->

def partition(arr, start, end):
    """
    The function partitions an array by selecting a pivot element and rearranging the elements such that
    all elements smaller than the pivot are on the left and all elements greater than the pivot are on
    the right.
    
    :parameter arr: an array of elements to be partitioned
    :parameter start: The starting index of the subarray to be partitioned
    :parameter end: The index of the last element in the subarray being partitioned
    :return: the index of the pivot element after partitioning the array.
    """
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if (arr[j] < pivot):
            i = i + 1
            swap(arr, i, j)
    swap(arr, (i + 1), end)
    return (i + 1)

# --------------------------------------------------------------------------------------------------------->

def quick_sort(arr, start, end):
    """
    This is a recursive implementation of the quick sort algorithm in Python.
    
    :parameter arr: The array to be sorted using quick sort algorithm
    :parameter start: The starting index of the subarray to be sorted
    :parameter end: The index of the last element in the array to be sorted
    """
    if (start < end):
        pivot = partition(arr, start, end)

        print("Quick Sort: ", arr)
        quick_sort(arr, start, (pivot - 1))
        quick_sort(arr, (pivot + 1), end)

# --------------------------------------------------------------------------------------------------------->


# This code is taking input from the user for the number of students and checking if the number is
# less than 5. If the number is less than 5, it will keep asking the user to enter the number of
# students until the number is greater than or equal to 5. It then initializes an empty list `a` to
# store the percentage of students.
cont = 'y'
while (cont == 'y'):
    n = int(input("Enter the no. of students: "))
    if (n < 5):
        while (n < 5):
            print("Sorry, Number of students can not be less than 5")
            n = int(input("Enter the no. of students again: "))
    a = []
    # This code is taking input from the user for the percentage of each student and storing it in a
    # list `a`. It first asks the user to enter the number of students and then uses a for loop to
    # iterate over the range of `n` and ask the user to enter the percentage of each student. It then
    # checks if the entered percentage is between 0 and 100, and if it is, it appends it to the list
    # `a`. If the entered percentage is not between 0 and 100, it keeps asking the user to enter the
    # percentage until a valid percentage is entered. Finally, it prints the list of percentages
    # entered by the user.
    for i in range(1,n+1):
        print("Enter percentage student", i, ": ", end="")
        elem = float(input())
        if ((elem <= 100) and (elem >= 0)):
            a.append(elem)
        else:
            while ((elem > 100) or (elem < 0)):
                print("Percentage can not be greater than 100 or negative")
                print("Enter percentage studnet", i, " again: ", end="")
                elem = float(input())
            a.append(elem)
   # This code is taking input from the user for the percentage of each student and storing it in a
   # list `a`. It then sorts the list using the quick sort algorithm and displays the top 5 scores. It
   # also asks the user if they want to continue and if the user enters 'n', it prints "Thank you!!!"
   # and exits the program.
    print("List of percentage of students is: ", a, "\n")
    quick_sort(a, 0, (n - 1))
    print("The sorted list of percentages (by Quick Sort) is: ", a)
    print("The Top 5 scores are:")
    for i in range(n - 1, n - 6, -1):
        print(n - i, "th: ", a[i])
    cont = input("Do you want to continue? (y/n): ")
if (cont == 'n'):
    print("Thank you!!!")



