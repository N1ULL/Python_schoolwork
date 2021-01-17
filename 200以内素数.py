num = 0
for i in range(2, 201):
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    if j == i:
        print(i, end='\t')
        num = num+1
print()
print("1-200之间的素数个数是：%d" % num)
