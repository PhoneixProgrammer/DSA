class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}

        for x in s:
            if x in s_dic:
                s_dic[x] += 1
            else:
                s_dic[x] = 1

        #print(s_dic)
        
        for y in t:
            if y in t_dic:
                t_dic[y] += 1
            else : 
                t_dic[y]=1
        
        #print(t_dic)
        
        if s_dic == t_dic :
            return True
        else :
            return False