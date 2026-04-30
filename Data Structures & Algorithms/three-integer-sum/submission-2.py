class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the input array in ascending order
        nums.sort()
        
        # Create an empty array to store the unique triplets
        result = []
        
        # Store the length of the array in a variable
        n = len(nums)

        # Iterate over the array till n - 2
        for i in range(n - 2):
            # If the current number is greater than 0, break the loop
            if nums[i] > 0:
                break
            
            # The current number is either the first element or not a duplicate of the previous element
            if i == 0 or nums[i] != nums[i - 1]:
                # Initialize two pointers
                low, high = i + 1, n - 1
                
                # Run a loop as long as low is less than high
                while low < high:
                    # Calculate the sum of the triplet
                    sum = nums[i] + nums[low] + nums[high]
                    
                    # If the sum is less than 0, move the low pointer forward
                    if sum < 0:
                        low += 1
                    
                    # If the sum is greater than 0, move the high pointer backward
                    elif sum > 0:
                        high -= 1
                    else:
                        # Add the triplet to result as this triplet sums to 0
                        result.append([nums[i], nums[low], nums[high]])
                        
                        # Move both pointers to the next distinct values to avoid duplicate triplets
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
        
        # Return result, which contains all unique triplets that sum to zero
        return result
      