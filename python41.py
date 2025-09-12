l=list(map(int,input().split()))
i=0
j=len(l)-1
while i<j:
  l[i],l[j]=l[j],l[i]
  i=i+1
  j=j-1
print(l)
