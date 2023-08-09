from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_s = s.strip()
        if not strip_s:
            return True
        phrase = deque(char.lower() for char in strip_s if char.isalnum())

        while len(phrase) > 1:
            if phrase.popleft() != phrase.pop():
                return False
        return True
