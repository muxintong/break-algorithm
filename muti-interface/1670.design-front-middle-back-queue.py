class FrontMiddleBackQueue:

    def __init__(self):
        self.list = []

    def pushFront(self, val: int) -> None:
        self.list.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.list.insert(len(self.list) // 2, val)

    def pushBack(self, val: int) -> None:
        self.list.append(val)

    def popFront(self) -> int:
        # self.list.try_pop(0)
        return self.try_pop(0)

    def popMiddle(self) -> int:
        return self.try_pop((len(self.list) - 1) // 2)

    def popBack(self) -> int:
        return self.try_pop(-1)

    def try_pop(self, index):
        try:
            return self.list.pop(index)
        except:
            return -1

    def print(self):
        print(self.list)


# Your FrontMiddleBackQueue object will be instantiated and called as such:
q = FrontMiddleBackQueue()

# [1]
q.pushFront(1)
q.print()
print('---')

# [1, 2]
q.pushBack(2)
q.print()
print('---')

# [1, 3, 2]
q.pushMiddle(3)
q.print()
print('---')

# [1, 4, 3, 2]
q.pushMiddle(4)
q.print()
print('---')

# return 1 -> [4, 3, 2]
q.popFront()
q.print()
print('---')

# return 3 -> [4, 2]
q.popMiddle()
q.print()
print('---')

# return 4 -> [2]
q.popMiddle()
q.print()
print('---')

# return 2 -> []
q.popBack()
q.print()
print('---')

# return -1 -> [] (The queue is empty)
q.popFront()
q.print()
print('---')
