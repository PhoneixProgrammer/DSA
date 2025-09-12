from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordset = set(wordDict)
        if not wordset:
            return []

        # max word length to limit inner loop
        max_len = max(len(w) for w in wordset)

        # possible[i] = True if s[i:] can be segmented into words from wordset
        possible = [False] * (n + 1)
        possible[n] = True  # empty suffix is segmentable

        # fill possible by DP from right to left
        for i in range(n - 1, -1, -1):
            # only try j up to i+max_len
            end_limit = min(n, i + max_len)
            for j in range(i + 1, end_limit + 1):
                if s[i:j] in wordset and possible[j]:
                    possible[i] = True
                    break

        # If whole string can't be segmented, early return
        if not possible[0]:
            return []

        # memoization for dfs: start_index -> list of sentences from s[start_index:]
        memo = {}

        def dfs(start: int) -> List[str]:
            if start in memo:
                return memo[start]
            if start == n:
                return ['']  # one way: empty sentence

            res = []
            end_limit = min(n, start + max_len)
            for end in range(start + 1, end_limit + 1):
                # prune if remainder can't be segmented
                if not possible[end]:
                    continue
                word = s[start:end]
                if word in wordset:
                    tails = dfs(end)  # all sentences for the suffix
                    for tail in tails:
                        # if tail is empty, don't add an extra space
                        res.append(word + (' ' + tail if tail else ''))
            memo[start] = res
            return res

        return dfs(0)
