class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_number = x
        copy_number = original_number
        reversed_number = 0
        while original_number > 0:
            remainder = original_number % 10
            reversed_number = reversed_number * 10 + remainder
            original_number = original_number // 10
        if copy_number ==reversed_number:
            return True
        else:
            return False
