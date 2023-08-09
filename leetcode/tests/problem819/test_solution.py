from leetcode.src.problem819.solution import Solution

solution = Solution()


def test_example1():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    assert solution.mostCommonWord(paragraph, banned) == "ball"


def test_example2():
    paragraph = "a."
    banned = []

    assert solution.mostCommonWord(paragraph, banned) == "a"


def test_example3():
    paragraph = "Bob. hIt, baLl"
    banned = ["bob", "hit"]

    assert solution.mostCommonWord(paragraph, banned) == "ball"


def test_example4():
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]

    assert solution.mostCommonWord(paragraph, banned) == "b"


def test_example5():
    paragraph = "..Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    assert solution.mostCommonWord(paragraph, banned) == "ball"
