sum = 0
count = 0
for num in range(1,500):
    if num %6 == 0 and num %7 == 0:
        sum += num
        count += 1
print("能同时被6和7整除的数一共有%d个，他们的和为%d" %(count,sum))
