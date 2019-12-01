v = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
str1 = "."
s = list(input()) 
s2= s.copy() 
for x in s: 
               for y in v:
                              if x==y: 
                                             s2.remove(x) 
lst = [x.lower() for x in s2]
print("." + str1.join(lst))
