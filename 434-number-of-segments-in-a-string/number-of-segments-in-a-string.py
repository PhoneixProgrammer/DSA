class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        in_segment = False
        
        for char in s:
            if char != ' ':          # non-space character
                if not in_segment:  # start of a new segment
                    segments += 1
                    in_segment = True
            else:
                in_segment = False   # space means outside segment
        
        return segments
