from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.stream = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey < 0 or idKey > self.n:
            return []

        self.stream.setdefault(idKey, value)
        res = []
        if self.stream.get(self.ptr):
            while idKey < self.n + 1:
                if self.stream.get(idKey):
                    res.append(self.stream.get(idKey))
                    idKey += 1
                    self.ptr = idKey
                else:
                    break
        # print(res)
        return res


# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)

# 插入 (3, "ccccc")，返回 []
obj.insert(3, "ccccc")

# 插入 (1, "aaaaa")，返回 ["aaaaa"]
obj.insert(1, "aaaaa")

# 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
obj.insert(2, "bbbbb")

# 插入 (5, "eeeee")，返回 []
obj.insert(5, "eeeee")

# 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]
obj.insert(4, "ddddd")
