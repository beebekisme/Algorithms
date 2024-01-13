

class Sorting_Algorithms: 
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def insertion_sort(self) -> list[int]:
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j > -1 and self.arr[j] > key:
                self.arr[j+1] = self.arr [j]
                j = j-1
            self.arr[j+1] = key
        return self.arr
    
    def selection_sort(self) -> list[int]:
        for i in range(len(self.arr)):
            min_idx = i
            for j in range(i+1, len(self.arr)):
                if self.arr[min_idx] > self.arr[j]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
        return self.arr





print(Sorting_Algorithms([-2, 1, 3,5, 4]).insertion_sort())