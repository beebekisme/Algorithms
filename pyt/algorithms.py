

class Sorting_Algorithms: 
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def insertion_sort(self) -> list[int]:
        for i in range(2, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j > 0 and self.arr[j] > key:
                self.arr[j+1] = self.arr [j]
                j = j-1
            self.arr[j+1] = key
        return self.arr


