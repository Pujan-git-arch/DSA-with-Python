def bubble_sort(elements):
  size = len(elements)
  
  for i in range(size-1): 
    swapped = False           # to eliminate  already sorted array we fist flag it as unswapped.. such that after the 1st iteration the list is still unswapped and it breaks from the outer loop
    for j in range(size-1-i):  # size-1-i is in the sense that after each ith iteration in outer loop the last two elements will be sorted already
         if  elements[j] > elements[j+1]:
            tmp = elements[j]
            elements[j] = elements[j+1]
            elements[j+1] = tmp  
            swapped = True
    if not swapped:
        break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    
    bubble_sort(elements)
    print(elements)