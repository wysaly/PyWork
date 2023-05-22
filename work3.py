#字典如何删除键和合并两个字典
#del和update方法
dic = {"name": "张三","age":18}

del dic["name"]

print(dic)

dic2 = {"name":"李四"}

dic.update(dic2)

print(dic)


