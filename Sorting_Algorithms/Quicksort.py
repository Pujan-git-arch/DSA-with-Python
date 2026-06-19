# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(start,end,elements):
    p_index = start
    pivot = elements[p_index]
    while start< end:
        
        while start <= end and elements[start] <= pivot:
            start+=1
        
        while elements[end] > pivot:
            end-=1
            
        if start < end:
            swap(start,end, elements)
            
    swap(p_index, end, elements)
    
    return end

def quicksort(start,end, elements):
    if start < end:
        pi = partition(start, end, elements)
        quicksort(start,pi-1, elements)
        quicksort(pi+1,end,elements)
        
        
    
    



if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quicksort(0,len(elements)-1,elements)
    print(elements)
