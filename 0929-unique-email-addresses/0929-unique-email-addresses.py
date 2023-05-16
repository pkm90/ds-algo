class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        
        
        
        
#         testemail@leetcode.com
        
#         testemail@leetcode.com
        
        
        
#         test.email + alex    @leetcode.com
                             
#         test.email @leetcode.com
        
        
#         keep track of unique values/count
        
#         go through each element in input
#         grab string before @
#         remove everything after the first plus
#         remove all periods
        
    
#         def find@(mail):
#             for i in range(len(mail)):
#                 if mail[i] == "@":
#                     return i
            
        uniqueEmails = set()
        for email in emails:
            # find position of @
            for i in range(len(email)):
                if email[i] == "@":
                    locationOfAt = i
            local = email[:locationOfAt]
            domain = email[locationOfAt:]
            
            
            temp = ""
            for char in local:
                if char == "+":
                    break
                if char == ".":
                    continue
                temp = temp + char
            
            temp = temp + domain
            uniqueEmails.add(temp)
            
#             print(local)
#             print(domain)
        
        
        print(uniqueEmails)
        return len(uniqueEmails)

        