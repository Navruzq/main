def find_max(data:list[int])->int:\
   
   m=0
   for i in data:
       if  i>m:
          m=i
   return data.count(m)
print(find_max([1,2,5,4,5]))