from leetcode.src.problem125.solution1 import Solution

solution = Solution()


def test_example1():
    s = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s) == True


def test_example2():
    s = "race a car"
    assert solution.isPalindrome(s) == False


def test_example3():
    s = " "
    assert solution.isPalindrome(s) == True


def test_example4():
    s = "0P"
    assert solution.isPalindrome(s) == False
