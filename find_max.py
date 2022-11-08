def find_max(data:list[int])->int:\
   
   m=0
   for i in data:
       if  i>m:
          m=i
   return m
print(find_max([1,6,3,4,5]))