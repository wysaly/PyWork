#python实现列表去重的方法
#先通过集合去重，再转列表
lis = [11,12,13,12,15,16,13]

a = set(lis)#集合去重

print(a)

a = [x for x in a]#转列表

print(a)