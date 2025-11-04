prices = [ 10,20,30,40,50,60,70,80,90]

quantity = [1,2,3,4,5,6,7,8,9]

total= 0
for i in range(len(prices)):
    total = total + prices[i] * quantity[i]

print("total prices: ", total)
