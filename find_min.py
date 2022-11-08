def find_min(data:list[int])->int:\
   
   m=data[0]
   for i in data:
       if  i<m:
          m=i
   return m
print(find_min([1,2,3,-9,5]))