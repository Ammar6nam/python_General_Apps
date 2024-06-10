def swap (list,element1,element2):
    temp=list[element1]
    list[element1]=list[element2]
    list[element2]=temp
    print(list)
n=int(input('Enter the number of numbers: '))
index=0
a=[]
while(index<n):
    x=int(input(f'Enter the number of number {index+1}: '))
    a.append(x)
    index+=1
case1=input('do you want to make any exchange between 2 elmements? "yes or no" ')
if case1=='no':
    print(a)
else:
    el1=int(input(f'Enter the index of 1st element you want to exchange it? "the number of index should be less than {n-1}": '))
    el2=int(input(f'Enter the second index for the second element "the number of index should be less than {n-1}": '))
    swap(a,el1,el2)

    # el=int(input(f'Enter the index of 1st element you want to exchange it? "the number of index should be less than {n-1}": '))
    # el2=int(input(f'Enter the second index for the second element "the number of index should be less than {n-1}": '))
    # temp=a[el]
    # a[el]=a[el2]
    # a[el2]=temp
    # print(a)
#def swap (a,element1,element2):
    # n=int(input('Enter the number of numbers: '))
    # index=0
    # list=[]
    # while(index<n):
    #     x=int(input(f'Enter the number of number {index+1}: '))
    #     a.append(x)
    #     index+=1
    # case1=input('do you want to make any exchange between 2 elmements? "yes or no" ')
    # if case1=='no':
    #     print(a)
    # else:
        # element1=int(input(f'Enter the index of 1st element you want to exchange it? "the number of index should be less than {n-1}": '))
        # element2=int(input(f'Enter the second index for the second element "the number of index should be less than {n-1}": '))
        # temp=a[el]
        # a[el]=a[el2]
        # a[el2]=temp
        # print(a)