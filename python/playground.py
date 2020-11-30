import statistics

def partition(left, right, array):
    pivot = array[right]
    i, j = left, left
    while j < right:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    array[i], array[right] = array[right], array[i]
    return i

def find_median(array):
    N = len(array)
    start = 0
    end = N-1
    expected_pivot = (N-1)//2
    pivot = partition(start, end, array)
    while expected_pivot != pivot:
        if pivot > expected_pivot:
            pivot = partition(start, pivot-1, array)
        else:
            pivot = partition(pivot + 1, end, array)
    if N % 2 == 1:
        return array[pivot]
    else:
        return (array[pivot] + min(array[pivot+1:]))/2

array = [6,8,2,9,3,1,10,34,12,8,4]
print(find_median(array))
print(statistics.median(array))
