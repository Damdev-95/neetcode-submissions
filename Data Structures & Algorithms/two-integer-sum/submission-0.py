class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,num in enumerate(nums):
            remain = target - num 
            if remain in result.keys():
                return [result[remain], i]
            result[num] = i
        return None
            
        