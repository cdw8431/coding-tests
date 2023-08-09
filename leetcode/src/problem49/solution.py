from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            anagram = "".join(sorted(s))
            group = anagrams.get(anagram)
            if group:
                group.append(s)
                anagrams[anagram] = group
            else:
                anagrams[anagram] = [s]

        return list(anagrams.values())
