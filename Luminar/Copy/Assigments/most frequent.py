words="AAABBCCDDCCAA"
dict={}
lst=[]
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
for k,v in dict.items():
    lst.append(v)
for j in dict:
    if(int(max(lst))==dict[j]):
        print("most frequent:",j)



