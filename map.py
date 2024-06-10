a_list=[1,2,3,4,5]
# byTwo=lambda num:num*2
# listByTwo=map(byTwo,a_list) #it s´dosnt work!
# print(a_list)
# print(list(a_list))
# def by_two(el):
#     return el **6

# def isOdd (el):
#     return el%2 != 0
#result=map(by_two,a_list)
#result2=filter(isOdd,a_list)
#print(result)
#print(result2)
#print(list(result))
#print(list(result2))

from functools import reduce
result3=reduce(lambda x,y :x ** y , a_list)
print (result3)