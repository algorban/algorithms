from random import random, randrange


def max_sum_of_non_adjacent_elements(array):
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]
    maxar = [-1] * len(array)
    maxar[0] = array[0]
    maxar[1] = max(maxar[0], array[1])
    for i in range(2, len(array)):
        maxar[i] = max(array[i] + maxar[i - 2], maxar[i - 1])
    return maxar[-1]


def array_rotation_point(array, l, h):
    """
    :param array: shifted sorted array
    :return: index of rotation point, i.e. index of minimal element in the array
    """
    if array[l] <= array[h]:
        return l
    length = h - l
    mid = (l + h) // 2
    next = (mid + 1) % length
    prev = (mid + length - 1) % length
    if array[mid] <= array[next] and array[mid] <= array[prev]:
        return mid
    if array[mid] <= array[h]:
        return array_rotation_point(array, l, mid - 1)
    else:
        return array_rotation_point(array, mid + 1, h)


def shift_array(array, n):
    """
    Shifts array circully to the right for n position
    :param array: array
    :param n: number of shifts
    :return: shifted array
    """
    start = 0
    end = len(array) - 1
    # reverse array
    while end > start:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    # reverse each part before and after index
    start = 0
    end = n - 1
    while end > start:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    start = n
    end = len(array) - 1
    while end > start:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    return array


def shuffle_array(array):
    """
    Shuffles array inplace
    :param array: array
    :return: shuffled array
    """
    for index in range(len(array) - 1, 0, -1):
        ri = randrange(0, index)
        array[index], array[ri] = array[ri], array[index]
    return array


def max_profit(array):
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


def max_sum_subarray(array):
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

    return array[startidx:endidx + 1]


# recursive powerset
def powerset1(array):
    if len(array) == 0:
        return [[]]
    include = [[array[0]] + subset for subset in powerset1(array[1:])]
    exclude = powerset1(array[1:])
    return include + exclude


# iterative
def powerset2(array):
    result = [[]]
    for element in array:
        result = [[element] + subset for subset in result] + result
    return result


def is_hoppable(array):
    """
    Tower Hopper Problem
    Value at particular index represent max number of steps one can jump over
    Find if there is a way to ump from index 0 out of the array
    :param array: array of integers
    :return: True or False
    """
    index = 0
    while True:
        if index >= len(array):
            return True
        if array[index] == 0:
            return False
        index = next_step(index, array)


def next_step(index, array):
    """
    Helper function to find next optimal step
    :param index: start index
    :param array: array of integers
    :return: return next optimal index(step) in the array
    """
    next_index = 0
    mmax = 0
    for i in range(1, array[index]):
        if array[index+i] > mmax:
            mmax = array[index+i]
            next_index = index+i
    return next_index


if __name__ == '__main__':
    array = [6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5]
    print("Index of minimal element is", end=" ")
    print(array_rotation_point(array, 0, len(array) - 1))
    print("Shifting array to the right for 6 positions", end=" ")
    print(shift_array(array, 6))
    print("Shuffling array", end=" ")
    print(shuffle_array(array))
    print("Max profit", end=" ")
    print(max_profit(array))
    print("Max subarray with biggest sum", end=" ")
    print(max_sum_subarray(array))
    print("Maximum Sum of Non-adjacent Elements", end=" ")
    print(max_sum_of_non_adjacent_elements([1, 0, 3, 9, 2]))
    print("Powerset recursive: ", end = " ")
    print(powerset1([1,2,3]))
    print("Powerset iterative: ", end=" ")
    print(powerset2([1, 2, 3]))
    assert is_hoppable([4,2,0,0,2,0]) == True