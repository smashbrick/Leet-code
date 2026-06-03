class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        for s in strs:
            response += str(len(s)) + "#" + s
        return response
        
        
        
        
    def decode(self, s: str) -> List[str]:
        recieved = []
        i = 0
        j = 0
        while i < len(s):
            j = i

            while s[i] != "#":
                i+=1
            
            length = int(s[j:i])
            i+=1
            recieved.append(s[i: i + length])
            i += length
        return recieved

    

                
        


            
               
    


        
