def find_min(data:list[int])->int:
   
   s=0
   i=0
   for i in data:
       if i%2==0:
        s+=i

   return s  
  
print(find_min([1,2,8,9,5]))