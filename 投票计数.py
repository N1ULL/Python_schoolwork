votes = input('请输入列表：')
votes = votes.split(',')
result = {}
for name in votes:
    result[name] = result.get(name, 0)+1
print(result)
