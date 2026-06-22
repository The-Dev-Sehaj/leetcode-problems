class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_items[:k]]


        