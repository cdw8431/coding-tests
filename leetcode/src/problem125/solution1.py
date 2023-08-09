class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_s = s.strip()
        if not strip_s:
            return True
        phrase = [char.lower() for char in strip_s if char.isalnum()]
        return phrase == phrase[::-1]
