#python中生成随机整数、0-1之间小数的方法
import random
result = random.randint(10,20)#区间
ret = random.random()#不能传数值
print("正整数",result)
print("0-1随机小数",ret)
#numpy库不知道怎么导入（或下载）