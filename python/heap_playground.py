import heapq as hq


class Item:

    def __init__(self, key, value, frequency=1):
        self.key = key
        self.value = value
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency


if __name__ == '__main__':

    h = []
    kvm = {1: Item(1,2,3), 2:Item(2,3,2), 3: Item(3,3,1), 4:Item(4,8,2)}
    hq.heappush(h, kvm[1])
    hq.heappush(h, kvm[2])
    hq.heappush(h, kvm[3])
    hq.heappush(h, kvm[4])

