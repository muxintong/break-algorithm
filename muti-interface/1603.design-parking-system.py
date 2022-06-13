class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        if carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        if carType == 3 and self.small > 0:
            self.small -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)

# 返回 true ，因为有 1 个空的大车位
print(obj.addCar(1))

# 返回 true ，因为有 1 个空的中车位
print(obj.addCar(2))

# 返回 false ，因为没有空的小车位
print(obj.addCar(3))

# 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了
print(obj.addCar(1))
