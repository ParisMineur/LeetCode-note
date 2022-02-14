class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        
        for num in nums:
            if len(self.heap)<k:
                heapq.heappush(self.heap, num)
            else:
                if num > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, num)
        
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]
