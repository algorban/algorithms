class Node:

    __slots__ = ['data', 'next']

    def __init__(self, data):
        self.data = data
        self.next = None


class List:

    __slots__ = ['size', 'head', 'iter']

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def peak(self):
        if self.size > 0:
            return self.head.data
        else:
            return None

    def reverse(self):
        prev_node = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def lastnth(self, n):
        if n > self.size:
            return None
        else:
            last = self.head
            for i in range(0,n):
                last = last.next
            first = self.head
            while last:
                first = first.next
                last = last.next
        return first.data

    def __len__(self):
        return self.size

    def __iter__(self):
        self.iter = self.head
        return self

    def __next__(self):
        if self.iter is None:
            raise StopIteration
        element = self.iter.data
        self.iter = self.iter.next
        return element

if __name__ == '__main__':

    llist = List()

    for i in range(10,0,-1):
        llist.add(i)

    print(llist.peak())

    assert 6 == llist.lastnth(5)
    llist.reverse()
    assert 5 == llist.lastnth(5)
