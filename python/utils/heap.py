class Empty(Exception):
    pass

class _Heap:
    __slots__ = ['_size', '_heap']

    def __init__(self):
        self._heap = []
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def clone(self):
        heap = self._heap[:]
        return heap

    def _parent(self, idx):
        index = (idx-1)//2
        if index < 0:
            return None
        else:
            return index

    def _leftchild(self, idx):
        index = idx*2+1
        if index < self._size:
            return index
        else:
            return None

    def _rightchild(self, idx):
        index = idx*2+2
        if index < self._size:
            return index
        else:
            return None

    def pull(self):
        if self._size == 0:
            raise Empty("Heap is empty")
        else:
            return self._heap[0]

    def pop(self):
        if self._size == 0:
            raise Empty("Heap is empty")
        else:
            element = self._heap[0]
            self._heap[0] = self._heap[self._size - 1]
            self._size -= 1
            self._sinkdown(0)
            return element

    def add(self, element):
        self._heap.append(element)
        self._size += 1
        self._bubbleup(self._size-1)

    def _sinkdown(self, index):
        pass

    def _bubbleup(self, index):
        pass


class MinHeap(_Heap):

    def _bubbleup(self, index):
        parent = self._parent(index)
        if parent is not None and self._heap[index] < self._heap[parent]:
            self._heap[parent], self._heap[index] = self._heap[index], self._heap[parent]
            self._bubbleup(parent)

    def _sinkdown(self, index):
        largest = index
        left = self._leftchild(index)
        right = self._rightchild(index)
        if left is not None and self._heap[left] < self._heap[largest]:
            largest = left
        if right is not None and self._heap[right] < self._heap[largest]:
            largest = right
        if largest != index:
            self._heap[largest], self._heap[index] = self._heap[index], self._heap[largest]
            self._sinkdown(largest)


class MaxHeap(_Heap):
    def _bubbleup(self, index):
        parent = self._parent(index)
        if parent is not None and self._heap[index] > self._heap[parent]:
            self._heap[parent], self._heap[index] = self._heap[index], self._heap[parent]
            self._bubbleup(parent)

    def _sinkdown(self, index):
        largest = index
        left = self._leftchild(index)
        right = self._rightchild(index)
        if left is not None and self._heap[left] > self._heap[largest]:
            largest = left
        if right is not None and self._heap[right] > self._heap[largest]:
            largest = right
        if largest != index:
            self._heap[largest], self._heap[index] = self._heap[index], self._heap[largest]
            self._sinkdown(largest)


if __name__ == '__main__':
    minheap = MinHeap()
    maxheap = MaxHeap()
    for i in [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]:
        minheap.add(i)
        maxheap.add(i)

    while not minheap.isEmpty():
        print(minheap.pop(), end=" ")

    print("")

    while not maxheap.isEmpty():
        print(maxheap.pop(), end=" ")


