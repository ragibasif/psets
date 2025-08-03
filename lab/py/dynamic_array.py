# url: https://neetcode.io/problems/dynamicArray


class DynamicArray:

    def __init__(self, capacity: int):
        self.buffer = []
        self.capacity = capacity if capacity > 0 else 8

    def get(self, i: int) -> int:
        return self.buffer[i]

    def set(self, i: int, n: int) -> None:
        self.buffer[i] = n

    def pushback(self, n: int) -> None:
        if len(self.buffer) >= self.capacity:
            self.resize()
        self.buffer.append(n)

    def popback(self) -> int:
        temp: int = self.buffer[-1]
        self.buffer.pop()
        return temp

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.buffer)

    def getCapacity(self) -> int:
        return self.capacity
