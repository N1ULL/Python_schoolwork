import random
while True:
    play=eval(input('输入你的选择，石头1 剪刀2 布3'))
    computer=random.randint(1,3)
    if play-computer == -1 or play-computer == 2:
        print('你赢啦！')
        break
    elif computer-play == -1 or computer-play == 2:
        print('你输啦！')
    else:
        print('平局！')
    print('电脑输出',computer)