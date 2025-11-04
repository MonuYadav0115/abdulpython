# Find the maximum and minimum numbers in a list.

numbers = [ 12,13,14,15,16,17,18,19]
max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    if n>max_num:
        max_num = n
    if n<min_num:
        min_num = n

# print("maximum nuber:",max_num)
# print("minimum number",min_num)


l = [1,2,3,4,5,6,7,8,9]

print("maximum number",max(l))
print("minimum number:",min(l))
