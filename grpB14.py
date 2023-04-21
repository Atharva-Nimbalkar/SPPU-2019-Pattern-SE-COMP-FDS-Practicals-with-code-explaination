"""PS : Write a pythonprogram to store first year percentage of students in array. Write function 
for sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort and display top five scores. """

percentage = []
n = int(input("Enter no of students :"))
for i in range(n):
    p = float(input("Enter Percentage of first year :"))
    percentage.append(p)
print(percentage)


def selection(percentage):
    """
    This function performs selection sort on a list of percentages and prints the sorted list.
    
    :parameter percentage: The input parameter "percentage" is a list of numbers representing the percentage
    values to be sorted in ascending order using the selection sort algorithm
    """

    # This code block is implementing the selection sort algorithm to sort the list of percentages in
    # ascending order. It iterates through the list and finds the minimum value in the unsorted
    # portion of the list and swaps it with the first element of the unsorted portion. This process is
    # repeated until the entire list is sorted.
    for i in range(len(percentage)):
        min = i
        for j in range(i+1, len(percentage)):
            if percentage[min] > percentage[j]:
                min = j
        percentage[i], percentage[min] = percentage[min], percentage[i]

    print_Array(percentage,5)



def bubble(percentage):
    """
    The function implements the bubble sort algorithm to sort a list of percentages in ascending order
    and prints the sorted list.
    
    :parameter percentage: The input list of percentages that needs to be sorted using the bubble sort
    algorithm
    """

    # This code block is implementing the bubble sort algorithm to sort the list of percentages in
    # ascending order. The variable `n` is assigned the length of the input list `percentage`. The
    # outer loop iterates `n` times, and the inner loop iterates from 0 to `n-i-1`. In each iteration
    # of the inner loop, the adjacent elements are compared and swapped if they are in the wrong
    # order. This process is repeated until the entire list is sorted.
    n = len(percentage)

    for i in range(n):

        for j in range(0, n - i - 1):

            if percentage[j] > percentage[j + 1]:
                percentage[j], percentage[j +
                                          1] = percentage[j + 1], percentage[j]

    print_Array(percentage, 5)



def print_Array(array, limit=None):
    """
    The function prints either the entire sorted array or the top 5 scores of an array.
    
    :parameter array: The array parameter is a list of numbers that we want to print
    :parameter limit: The limit parameter is an optional parameter that specifies the number of elements to
    be printed from the array. If the limit is not specified, the entire array is printed. If the limit
    is specified, only the top 'limit' elements are printed
    """
    if limit == None:
        print("Sorted array")
        for i in range(len(array)):
            print(array[i])

    else:
        print(" top 5 scores are: ")
        if len(array) > 5:
            for i in range(len(array) - 1, len(array) - 6, -1):
                print(array[i])
        else:
            for i in range(len(array) - 1, -1, -1):
                print(array[i])


while True:
    print("""
    Operation
    1. Selection Sort
    2. Bubble Sort
    3. Exit
    """)
    choice = int(input("Enter Choice : "))
    if choice == 1:
        selection(percentage)
    elif choice == 2:
        bubble(percentage)
    elif choice == 3:
        break
    else:
        print("Invalid Choice")
