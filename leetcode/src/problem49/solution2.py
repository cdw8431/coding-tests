from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict를 활용하면 기본값을 넣어주기 때문에 깔끔하게 구현할 수 있음
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return list(anagrams.values())
