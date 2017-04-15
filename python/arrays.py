from random import random, randrange


def arrayrotationpoint(array, l, h):
    """
    :param array: shifted sorted array
    :return: index of rotation point, i.e. index of minimal element in the array
    """
    if array[l] <= array[h]:
        return l
    length = h-l
    mid = (l+h)//2
    next = (mid+1)%length
    prev = (mid+length-1)%length
    if array[mid] <= array[next] and array[mid] <= array[prev]:
        return mid
    if array[mid] <= array[h]:
        return arrayrotationpoint(array, l, mid-1)
    else:
        return arrayrotationpoint(array, mid+1, h)


def shiftarray(array, n):
    """
    Shifts array circully to the right for n position
    :param array: array
    :param n: number of shifts
    :return: shifted array
    """
    start = 0
    end = len(array)-1
    #reverse array
    while end > start:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    #reverse each part before and after index
    start = 0
    end = n-1
    while end > start:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    start = n
    end = len(array)-1
    while end > start:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    return array

def shufflearray(array):
    """
    Shuffles array inplace
    :param array: array
    :return: shuffled array
    """
    for index in range(len(array)-1, 0, -1):
        ri = randrange(0, index)
        array[index], array[ri] = array[ri], array[index]
    return array

def maxprofit(array):
    """
    Finds max profit in sequence of stock prices in linear time
    :param array: array of stock price
    :return: max profit
    """
    profit = array[1] - array[0]
    mmin = array[0]
    for idx in range(1, len(array)):
        current_profit = array[idx] - mmin
        profit = max(profit, current_profit)
        mmin = min(array[idx], mmin)

    return profit

def maxsumsubarray(array):
    """
    :param array: array of int
    :return: continuous subarray with maximum sum
    """
    maxglobal = array[0]
    startidx = 0
    endidx = 0
    for idx in range(1, len(array)):
        if maxglobal + array[idx] < array[idx]:
            maxglobal = array[idx]
            startidx = idx
            endidx = idx
        else:
            maxglobal = maxglobal + array[idx]
            endidx = idx

    return array[startidx:endidx+1]

if __name__ == '__main__':
    array = [6,7,8,9,10,0, 1,2,3,4,5]
    print("Index of minimal element is", end=" ")
    print(arrayrotationpoint(array, 0, len(array)-1))
    print("Shifting array to the right for 6 positions", end=" ")
    print(shiftarray(array,6))
    print("Shuffling array", end=" ")
    print(shufflearray(array))
    print("Max profit", end=" ")
    print(maxprofit(array))
    print("Max subarray with biggest sum", end=" ")
    print(maxsumsubarray(array))