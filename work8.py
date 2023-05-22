#s = "ajldjlajfdljfddd",去重并从小到大排序输出"adfjl"
#set去重，去重后转为list，利用sort方法排序，reeverse=False是从小到大排
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
res = "".join(s)
print(res)