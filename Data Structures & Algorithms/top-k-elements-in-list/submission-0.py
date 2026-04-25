class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        for num in nums:
            fre[num] = fre.get(num, 0) + 1
        output = sorted(fre.items(), key = lambda x : x[1], reverse=True)
        output = output[:k]
        return [num for num, count in output]

        