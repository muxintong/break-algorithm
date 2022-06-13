import heapq


class SeatManager_TimeLimitError:

    def __init__(self, n: int):
        self.seats = [i + 1 for i in range(n)]

    def reserve(self) -> int:
        mini = min(self.seats)
        self.seats.remove(mini)
        return mini

    def unreserve(self, seatNumber: int) -> None:
        self.seats.append(seatNumber)


class SeatManager:

    def __init__(self, n: int):
        self.seats = [i + 1 for i in range(n)]
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        mini = heapq.heappop(self.seats)
        return mini

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# [[3],[],[],[1],[2],[],[1],[],[1]]
seatManager = SeatManager(3)
print(seatManager.reserve())
print(seatManager.reserve())
print(seatManager.unreserve(1))
print(seatManager.unreserve(2))
print(seatManager.reserve())
print(seatManager.unreserve(1))
print(seatManager.reserve())
print(seatManager.unreserve(1))

print('---')
# [null, 1, 2, null, 2, 3, 4, 5, null]
# 初始化 SeatManager ，有 5 个座位
seatManager = SeatManager(5)
# 所有座位都可以预约，所以返回最小编号的座位，也就是 1
print(seatManager.reserve())
# 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2
print(seatManager.reserve())
# 将座位 2 变为可以预约，现在可预约的座位为 [2,3,4,5]
print(seatManager.unreserve(2))
print(seatManager.reserve())
print(seatManager.reserve())
print(seatManager.reserve())
print(seatManager.reserve())
print(seatManager.unreserve(5))
