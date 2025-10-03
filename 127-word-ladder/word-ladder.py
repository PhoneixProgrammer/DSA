from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Step 1: If endWord not in wordList → impossible
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)

        # Step 2: Build dictionary of intermediate patterns
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                all_combo_dict[pattern].append(word)

        # Step 3: BFS setup
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        # Step 4: BFS traversal
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                for neighbor in all_combo_dict[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                # Clear the pattern to save reprocessing
                all_combo_dict[pattern] = []
        
        return 0
