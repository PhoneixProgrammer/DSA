class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort greed factors
        s.sort()  # Sort cookie sizes
        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # Cookie satisfies child
                child += 1
            # Move to next cookie regardless
            cookie += 1

        return child  # Number of content children