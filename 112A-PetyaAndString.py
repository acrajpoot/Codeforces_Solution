i = 0
s1 = input().lower()
s2 = input().lower()
if len(s1) > len(s2): 
               print('-1') 
elif len(s1) < len(s2):
               print('1')
elif len(s1) == len(s2): 
               for x in range(len(s1)):
                              if s1[x] == s2[x]: 
                                             i= i+1
                              elif s1[x] != s2[x]: 
                                             if ord(s1[x]) > ord(s2[x]): 
                                                            print("1")
                                                            break
                                             elif ord(s1[x]) < ord(s2[x]): 
                                                            print("-1")
                                                            break
if i == len(s1):
                 print('0')
               
