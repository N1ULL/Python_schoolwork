print('计算n！')
n=eval(input('n的值是：'))
sum=1
for i in range(1,n+1):
    sum=sum*i
    i+=1
print('n!=',sum)