# def getAllValues(*values):
#     a,b,*c=values
#     print(f'Values',values)

# functionValues: list=['a','b','c','d']
# getAllValues(*functionValues)

# shopingList: list=['shoes','shirt','cap']
# def func1 (*items):
#     print (items)
#     #print(item2)
#     #print(item3)

# func1(shopingList)

# def func2(**items):
#     print(items)

# shopingList2:dict={'item1':'shoes','item2':'shirt','item3':'cap'}
# # func2(**shopingList2)

# def func3 (item1=None,**item2):
#     print(item1)
#     print(item2)

# # func3(**shopingList2)

# def func4 (item1,item2=90,**items):
#     print(item1)
#     print(item2)
#     print(items)
    
# func4(**shopingList2)

#def func5(*var)

# def greet_person(age, location="Berlin", name="Ammar", favorite_meal=None):
#     if age < 10:
#         print("You are not allowed to have a favorite meal.")
#     else:
#         if favorite_meal:
#             print(f"{name}'s favorite meal is {favorite_meal}.")
#         else:
#             print(f"{name} has no favorite meal.")
    
#     if location != "Berlin":
#         print("Welcome to Berlin")
#     else:
#         print("You are already in Berlin.")

# greet_person(28, location="Leipzig", name="Max", favorite_meal="Pasta")
# greet_person(35, location="Berlin", name="Sami",favorite_meal='rice')


# closures:
# def firstFunction():
#     x=900
#     def givCapitaliyedValues():
#         print(x)
#         print('I changed smthg')
#     return givCapitaliyedValues

# capitalize=firstFunction()
# print(capitalize())

# def decorator(func):
#     def addFunctionality(name):
#         result=func(name)
#         return result.upper()
#     return addFunctionality
# @decorator
# def getMyName(name):
#     return name

# # newFunction=decorator(getMyName)
# # print(newFunction('Ammar'))
# print(getMyName('Ammar'))

# def capitalizeDecorator():
#     def doSmthg():
#         pass
#     return doSmthg

# newFunc=capitalizeDecorator()
# newFunc()

def readTxt(fileName:str):
    file=open(fileName,'r')
    result=file.read().split('\n')
    return result
def readTxtAgn(filename:str):
    for item in open(filename,'r'):
                     yield item
result1=readTxt('lar')