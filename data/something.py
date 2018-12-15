import this

#enumerate. 설명
a = [4,5,1,6,7,3,8,1,0,3]

for k,v in enumerate(a):
     print(k, v)

# #__missing__
#
#
class SubDict(dict):
     def __missing__(self, key):
         print('__missing__')

d = SubDict()
d['hello']

# class SubDict(dict):
#     pass
#
# d = SubDict()
# d['hello']
