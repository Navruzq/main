def find_max(data:list[int])->int:
    s=data[0]
   
 
    for i in data:
       if i>s:
          s=i
    for a in range(len(data)):
       if  data[a]==s:
            data[a]=0
    return data
print(find_max([1,2,3,4,5]))