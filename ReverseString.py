import re
str1 = list('asdf@re#tyu$oi!')
tmp = []
res = []
for i in str1:
    if i.isalpha():
        tmp.append(i)
    else:
        res.append(tmp[::-1])
        res.append(i)
        tmp.clear()
        
outlst = [' '.join([str(c) for c in lst]) for lst in res]
outlst = ''.join([str(elem) for elem in outlst]) 
print(outlst)
