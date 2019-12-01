x = 0
for i in range(int(input())): 
               st= input() 
               if st == "++X" or st == "X++": 
                              x = x+1
               elif st == "--X" or st == "X--": 
                              x = x-1
print(x)
