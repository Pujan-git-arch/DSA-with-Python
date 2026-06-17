# When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

# numbers = [1,4,6,9,10,5,7]

# answer----> Because the list is not in sorted order


# Find index of all the occurances of a number from sorted list

# numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
# number_to_find = 15  
# This should return 5,6,7 as indices containing number 15 in the array

def binary_search(arr, number_to_find, left_index, right_index):
    
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = arr[mid_index]

    if mid_number == number_to_find:
        return mid_index

    elif mid_number < number_to_find:
        return binary_search(arr, number_to_find, mid_index + 1, right_index)

    else:
        return binary_search(arr, number_to_find, left_index, mid_index - 1)


def find_all_occurrences(numbers, number_to_find, left_index, right_index):

    index = binary_search(numbers, number_to_find, left_index, right_index)

    if index == -1:
        return []

    indices = [index]

    # left side
    i = index - 1
    while i >= 0 and numbers[i] == number_to_find:
        indices.append(i)
        i -= 1

    # right side
    i = index + 1
    while i < len(numbers) and numbers[i] == number_to_find:
        indices.append(i)
        i += 1

    return sorted(indices)


if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 17

    left_index = 0
    right_index = len(numbers) - 1

    indices = find_all_occurrences(numbers, number_to_find, left_index, right_index)
    if len(indices)>1:
        print(f"Indices of occurrences of {number_to_find} are {indices}")
    else:
        print(f"Indices of occurrences of {number_to_find} is {indices}")
