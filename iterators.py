# myString='This is an example'
# print(len(myString)) 
# for x in myList:
#     print(x)
# myList={1,2,3,4,False,'case','7',True}
# myList2 = {'key1':'s','key2':'a','key3':'d'}
# # myKey='key1'
# counter=0
# print(len(myList))
# rang1=range(len(myList))
# print (rang1)
# for y in rang1:
#     print(f'in the index {y+1} the value is: {myList[y]}')
# for x in myList:
#     print(f'in the index {counter+1} the value is: {x}')
#     counter+=1
# for i,j in myList2.items():
#     print(f'index number {i} value is: {j}')
# myList3=[[1,2,3],[4,5,6]]
# print(myList2[myKey])
#print(len(myList3[1]))

# myTuples=myList2.items()
# print(myTuples)

# myList4={'Value1','Value2','Value3','Value4','Value5','Value6','Value7','Value8'}
# for x,y in enumerate(myList2.values()):
#     print(x,y)
#     print(type(x),type(y))

# p=enumerate(myString)
# print(p)
 
# a=[1,2,3]
# b=['one','Two','Three']
# c=zip(myList,myList2.items(),a)
# for i in c:
#     print(i)
# print(c)

books = {
  'Harry Potter And The Sorcerers Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}
sales = []
book = []
for key,value in books.items():
    sales.append(value)
    book.append(key)
print(sales)
print(book)
booksList = zip(book,sales)
print(booksList)
for q in booksList:
    print(q)