#functions

# def all_aboard(a,*args,**kw):
#     print(a,args,kw)
# all_aboard(4,7,3,0,x=10,y=64)

l=[10,20,30,1,3,5,7]
result = [int(i)  for i in l if i%2==0 ]
print(type(result))
print(result)