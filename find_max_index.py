def find_max_index(data:list[int])->int:\
   
   m=0
   for i in data:
       if  i>m:
          m=i
    
   return data.index(m)
print(find_max_index([1,6,3,56,5]))