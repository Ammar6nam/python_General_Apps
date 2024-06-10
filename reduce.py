list1=[1,2,3,4,5]
bytwo=lambda x:x*2
map1=map(bytwo,list1)
result=list[map1]
#print(list(map1))
#for i in map1:
    #print(i)
isodd1=lambda x:(x%2)!=0
filter1=filter(isodd1,list1)
map2=map(isodd1,list1)
print(list(map2))
print (list(filter1)) 

from functools import reduce

result2=reduce(lambda x,y:x*y,list1)
print(result2)
