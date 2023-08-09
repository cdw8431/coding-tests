import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # re.split을 사용하면 패턴으로 split 할 수 있음, \W+ 의미는 문자가 아닌 경우
        words = re.split(r"\W+", paragraph.lower())
        count_of_words = Counter(
            [word for word in words if word and word not in banned]
        )
        return count_of_words.most_common(1)[0][0]
