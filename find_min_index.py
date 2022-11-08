def find_min_index(data:list[int])->int:\
   
   m=data[0]
   for i in data:
       if  i<m:
          m=i
    
   return data.index(m)
print(find_min_index([1,-66,3,-7,5]))