class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        Logic : 
        loop 1 : tracking key alternatily untill equal length n1==n2
        loop2 and 3 : dor trackinf remaining values
        join() fun to return list without space
        
        """
      
        res = []
        n1 = len(word1)
        n2 = len(word2)
        i , j = 0 , 0

        while i < n1 and j < n2 :
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1

        while i < n1 :
            res.append(word1[i])
            i+=1
            
        while  j < n2 :
            res.append(word2[j])
            j+=1
        
        return "".join(res)
            
        
