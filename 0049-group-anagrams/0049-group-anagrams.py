class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #O(nlogN*m solution)
        
        string_dict={}
        
        for idx in range(len(strs)):
            s = tuple(sorted(strs[idx]))
            if string_dict.get(s,0):
                string_dict[s].append(strs[idx])
                # print("true", string_dict[s])
                
            else:
                string_dict[s]=[strs[idx]]
                # print("false", string_dict[s])
        
        return string_dict.values()
                
        


        
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            #simplest - nlog(n) *m
        # my_dict={}
        # for i in range(len(strs)):
        #     sorted_word = ''.join(sorted(strs[i]))
        #     if my_dict.get(sorted_word,0) == 0:
        #         my_dict[sorted_word] = [strs[i]]
        #     else:
        #         my_dict[sorted_word].append(strs[i])
        # return my_dict.values()

  #O(m*n*26) solution

#         result=defaultdict(list)

#         #for each word in str array
#         for s in strs:

#             #create a list count of 26 vals for each alph a-z
#             count=[0]*26
        
#             #create that list for each string in strs
#             for ch in s:
#                 count[ord(ch)-ord('a')] += 1
#             #make a hash where you use that list(tuple) as key and store string as value - same as before

#             result[tuple(count)].append(s)
#         #return hash vals
#         return result.values()
            
