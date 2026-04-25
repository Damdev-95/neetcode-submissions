class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for num in nums:
            result[num] = result.get(num,0) + 1
            if result[num] > 1:
                return True
        return False

        