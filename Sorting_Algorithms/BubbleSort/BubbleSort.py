# Function to swap two elements in a list
def swap(arr, i, j):
    # Store first element in a temporary variable
    temp = arr[i]

    # Put second element at the position of first element
    arr[i] = arr[j]

    # Put the temporary value at the position of second element
    arr[j] = temp


# Function to sort the list using Bubble Sort
def bubble_sort(elements):
    # Find total number of elements in the list
    size = len(elements)

    # Outer loop controls the number of passes
    # After each pass, the largest unsorted element
    # moves to its correct position at the end
    for i in range(size - 1):

        # Assume no swapping will happen in this pass
        swapped = False

        # Inner loop compares adjacent elements
        # size-1-i because the last i elements are already sorted
        for j in range(size - 1 - i):

            # If current element is greater than the next element
            # swap them
            if elements[j] > elements[j + 1]:
                swap(elements, j, j + 1)

                # Mark that a swap has occurred
                swapped = True

        # If no swapping occurred in the entire pass,
        # the list is already sorted, so stop early
        if not swapped:
            break


# Program execution starts here
if __name__ == '__main__':

    # Unsorted list
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    # Call Bubble Sort function
    bubble_sort(elements)

    # Print the sorted list
    print("Sorted List:", elements)