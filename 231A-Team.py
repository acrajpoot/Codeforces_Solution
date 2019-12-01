n = int(input())
i=0
for x in range(n): 
               s1, s2, s3 = map(int, input().split()) 
               if (s1 + s2 + s3) == 2 or (s1 + s2 + s3) == 3: 
                              i = i+1
print(i)
