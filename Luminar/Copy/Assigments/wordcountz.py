w="hai hello hello hai hai"
dict={}
words=w.split(" ")
print(words)
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)

