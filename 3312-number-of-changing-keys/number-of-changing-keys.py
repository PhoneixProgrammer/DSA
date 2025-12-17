class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s or len(s) <=1 :
            return 0

        key_changes = 0

        #Initialize with the first character 
        current_key = s[0].lower()

        for i in s[1:]:
            next_key = i.lower()

            if next_key != current_key :
                key_changes += 1
                current_key = next_key
        return key_changes