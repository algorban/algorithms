def _mergesort(array, start, end):
    if start<end:
        mid = (start+end)//2
        _mergesort(array, start, mid)
        _mergesort(array, mid+1, end)
        _merge(array, start, mid, end)


def _merge(array, start, mid, end):
    i = start
    j = mid+1
    aux = array[:]
    k = start
    while i <= mid and j <= end:
        if aux[i] < aux[j]:
            array[k] = aux[i]
            i += 1
            k += 1
        else:
            array[k] = aux[j]
            j += 1
            k += 1

    while i <= mid:
        array[k] = aux[i]
        k += 1
        i += 1

    while j <= mid:
        array[k] = aux[j]
        k += 1
        j += 1


def mergesort(array):
    _mergesort(array, 0, len(array)-1)


def _quicksort(array, lo, hi):
    if lo < hi:
        pivot = _pivot(array, lo, hi)
        _quicksort(array, lo, pivot-1)
        _quicksort(array, pivot+1, hi)


def _pivot(array, lo, hi):
    pivot = array[hi]
    i = lo-1
    for j in range(lo, hi):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[hi] = array[hi], array[i+1]
    return i+1


def quicksort(array):
    _quicksort(array, 0, len(array)-1)

if __name__ == '__main__':
    array = [3, 8, 1, 5, 4, 1, 6, 9, 7]
    mergesort(array)
    print(array)
    array = [8, 3, 1, 5, 4, 1, 6, 9, 7]
    quicksort(array)
    print(array)