def get_sum(lists):

    list2=[]

    total=0
    for i in range(len(lists)):

        total+=lists[i]
        
        list2.append(total)

    return list2

print(get_sum([1,2,3,4]))
