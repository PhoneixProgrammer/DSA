class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t :
            return ""

        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)

        res = ""
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0) +1

            if char in need and window[char] == need[char] :
                have += 1
            
            while have == need_count:
                #Update Result
                if (right - left + 1) < res_len :
                    res = s[left:right + 1]
                    res_len = right - left + 1 

                #Pop from the left of the window
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        return res

        #Time complexity : O(m+n)
        # Space Complexity : O(n) for the hashmaps