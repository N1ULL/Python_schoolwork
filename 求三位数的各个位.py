a=eval(input('请输入一个三位数字：'))
b=a//100
c=a//10%10
d=a%10
print('百位是{}，十位是{}，个位是{}。'.format(b,c,d))