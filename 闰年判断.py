a=eval(input('请输入年份：'))
if a%400==0 or (a%4==0 and a%100!=0):
    print('True')
else:
    print('False')