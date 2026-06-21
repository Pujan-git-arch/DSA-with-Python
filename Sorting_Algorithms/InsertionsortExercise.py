def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1

        elements[j + 1] = anchor

    return elements


def find_median(elements):
    n = len(elements)

    if n % 2 == 1:
        return elements[n // 2]
    else:
        return (elements[n // 2 - 1] + elements[n // 2]) / 2


def running_median(stream):
    temp = []

    for num in stream:
        temp.append(num)              # add new element
        insertion_sort(temp)          # keep sorted
        print(find_median(temp))      # print median


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    running_median(elements)