def longprefix(strs):
    if not strs:
        return""
    
    for i in range(len(strs[0])):

        for j in range(len(strs)):

            if i==len(strs[j]) or strs[0][i]!= strs[j][i]:


                return strs[0] [:i]
            
    return strs[0]
print(longprefix(["flower","flow","flight"]))