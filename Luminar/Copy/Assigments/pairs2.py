lst=[2,3,4]
lst1=()
for i in range(0,len(lst)-1):
    rs=lst[i],lst[i+1]
    print(rs)
    print(type(rs))
    if (rs not in lst1):
        lst1.append(rs)
        last=lst[0],lst[len(lst)-1]
        print("last",last)
        print(type(last))
    if(last not in lst1):
        lst1.append(last)
print(lst1)
