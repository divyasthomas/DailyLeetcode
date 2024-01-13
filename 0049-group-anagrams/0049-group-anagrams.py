class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

    #O(m*n*26) solution
        anagrams=defaultdict(list)
    
    
         #make a dict
        for idx in range(len(strs)):
            arr=[0]*26

            for c in strs[idx]:
                arr[ord(c)-ord('a')]+=1
            
            
            anagrams[tuple(arr)].append(strs[idx])

        
        return anagrams.values()
            
            
            
            

    
    
    
    
                
        


        
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        #O(nlogN*m solution)

#         string_dict={}
        
#         for idx in range(len(strs)):
#             s = tuple(sorted(strs[idx]))
#             if string_dict.get(s,0):
#                 string_dict[s].append(strs[idx])
#                 # print("true", string_dict[s])
                
#             else:
#                 string_dict[s]=[strs[idx]]
#                 # print("false", string_dict[s])  
#         return string_dict.values()
    
    
    
    
    
    

#   #O(m*n*26) solution

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
            
