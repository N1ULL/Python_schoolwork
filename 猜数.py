import random
a = random.randint(0, 101)
print('现在进行猜数游戏')
while True:
    b = eval(input('请输入数字:'))
    if a > b:
        print('小了')
    elif a < b:
        print('大了')
    else:
        print('猜数正确！')
        break