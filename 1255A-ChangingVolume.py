for x in range(int(input())): 
               a, b = map(int, input().split()) 
               d = abs(a-b)
               count=0
               while (d>0):
                              if(d>=5):
                                                            count = count + d//5
                                                            d = d%5
                              elif(d>=2):
                                                            count = count + d//2
                                                            d = d%2
                              elif(d==1):
                                                            d = d-1
                                                            count = count+1
               if d==0: 
                              print(count)
