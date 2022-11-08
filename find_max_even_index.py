def find_max_odd(data:list[int])->int:
   
   m=0
   for i in data:
       if  i>m and i%2==0:
          m=i
   return data.index(m)
print(find_max_odd([10,2,9,4,5]))