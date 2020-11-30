class FlatternList:

    def __init__(self, llist):
        self.current_list = [e for e in llist if not self.isEmpty(e)]
        self.idx = 0
        self.stack = []

    def isEmpty(self, e):
        return type(e) is list and len(e) == 0

    def next(self):
        if self.hasNext():
            while self.stack and self.idx >= len(self.current_list):
                self.idx, self.current_list = self.stack.pop()
            while type(self.current_list[self.idx]) is list:
                if self.idx + 1 < len(self.current_list):
                    self.stack.append((self.idx + 1, self.current_list))
                self.current_list = [e for e in self.current_list[self.idx] if not self.isEmpty(e)]
                self.idx = 0
            r = self.current_list[self.idx]
            self.idx += 1
            return r

    def hasNext(self):
        return self.stack or self.idx < len(self.current_list)


if __name__ == '__main__':

    llist = [[1,1],2,[1,2],[],2,[2,3]]
    fl = FlatternList(llist)
    while fl.hasNext():
        print(fl.next())