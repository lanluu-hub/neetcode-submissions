class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for  count, num in freq.items():
            heapq.heappush(heap, (num, count))

        while len(heap) > k:
            heapq.heappop(heap)

        new_heap = []

        for count, num in heap:
            heapq.heappush(new_heap,num)

        return new_heap