class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1
        s= s.lower()
        while left < right :
            while left < right and not s[left].isalnum():
                print(f"\tSkipping non-alphanumeric at left: '{s[left]}' (index {left})")
                left+=1
            while left < right and not s[right].isalnum():
                print(f"\tSkipping non-alphanumeric at right: '{s[right]}' (index {right})")
                right-=1

            print(f"\tLeft -> '{s[left]}' (index {left}), Right -> '{s[right]}' (index {right})")    
            
            if s[left]!= s[right]:
                return False
            
            left+=1
            right-=1
        return True 