class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}

        for x in s: 
            #s_dic[x] = s_dic.get(x, 0) + 1
            if x in s_dic:
                s_dic[x] += 1
            else:
                s_dic[x] = 1
     
        for y in t:
            #t_dic[y] = t_dic.get(y,0)+1
            if y in t_dic:
                t_dic[y] += 1
            else : 
                t_dic[y]=1
        
        #return s_dic == t_dic
        if s_dic == t_dic :
            return True
        else :
            return False

        #t.c :O(m+n) , s.c:O(m+n)

        # Alternatively we can use Counter for generating hashmaps automatically for s and t
        # and check both
        # from collections import Counter
        # return Counter(s) == Counter(t)