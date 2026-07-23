def sum (list, target):
    seen={}

  
    for index,num in enumerate(list):
        complement= target-num

      
        if complement in seen:
            return [seen[complement],index]
          
        seen[num]=index 
print(sum([2,7,11,15],9))
