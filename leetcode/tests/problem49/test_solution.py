from leetcode.src.problem49.solution import Solution

solution = Solution()


def test_example1():
    strs = ["bat", "nat", "ate", "tan", "eat", "tea"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    assert solution.groupAnagrams(strs) == expected


def test_example2():
    strs = [""]
    expected = [[""]]

    assert solution.groupAnagrams(strs) == expected


def test_example3():
    strs = ["a"]
    expected = [["a"]]

    assert solution.groupAnagrams(strs) == expected
