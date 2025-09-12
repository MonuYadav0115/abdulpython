l=[12, 0, 23, 0, 43]
for i in range(len(l)):
    if l[i]==0:
        l.remove(l[i])
        l.append(i)
print(l)
