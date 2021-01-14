import random                                      # 导入随机模块
sum=10                                             # 积分
print("基础积分为：10")                            # 显示基础积分
A=("剪刀","石头","布")
while True:
    a=input("请输入：（0 剪刀、1 石头、2 布）")   # 将输入的数据转化为整型
    c=random.randint(0,2)                         # 随机一个0到2的整数
    if a.isdigit() and a in ['0','1','2']:        # 是否为数字,且在出拳数字内
        a=int(a)                                  # 转换为整型
        if a==c:                                  # 平局条件
            print("\n平局\n")
        elif a-c==1 or c-a==2:                    # 赢局条件
            print("\n你赢了\n")
            sum+=1
        else:                                     # 输局
            print("\n你输了\n")
            sum-=1
        print("你出%s，电脑出%s" % (A[a], A[c]))          # 显示出双方出拳
    else:                                         # 输入错误
        print("你没正确出拳")
    print(("目前积分为：%d"%sum).rjust(60)) 