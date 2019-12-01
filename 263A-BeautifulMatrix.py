for x in range(1,6):
               r = map(int, input().split())
               s = list(r)
               if 1 in s:
                              i = s.index(1)
                              print(abs(3-(i+1)) + abs(3-x))
               else:
                              continue
