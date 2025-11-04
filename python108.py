# Calculate the average of numbers in a list

l = [ 10,20,30,40,50,60,70,80,90]
total = 0
count = 0
for i in l:
    total = total + i
    count = count + 1

average = total / count

print("average of number :", average )