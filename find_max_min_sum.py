def find_max_min_sum(data:list[int])->int:\
   
   max=data[0]
   min=data[0]
   for i in data:
       if  i>max:
          max=i
   for i in data:
       if  i<min:
          min=i     
   return min+max
print(find_max_min_sum([1,2,3,4,5]))


