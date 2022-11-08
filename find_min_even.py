def find_max_odd(data:list[int])->int:\
   
   m=0
   for i in data:
       if  i<m and i%2==0:
          m=i
   return m
print(find_max_odd([1,2,3,4,5]))