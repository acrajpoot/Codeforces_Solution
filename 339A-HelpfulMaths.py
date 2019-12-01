s = input()
lst = []
a  = "+"
for x in range(0,len(s),2):
               lst.append(s[x])
lst.sort()
print(a.join(lst))
