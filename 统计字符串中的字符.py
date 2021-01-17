num,word,space,other=0,0,0,0
a=input('请输入字符串：')
for i in a:
    if i.isdigit():
        num+=1
    elif i.isalpha():
        word+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print('数字=%d，字母=%d，空格=%d，其他=%d'%(num,word,space,other))