list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
commenList=[]
fCommenList=[]
index1=0
index2=0
for i in list_1:
    for j in list_2:
        if i == j:
            commenList.append(i)
        index2 +=1
    index1 +=1
for x in commenList:
    if x not in fCommenList:
        fCommenList.append(x)
print(fCommenList)
    #print('M1: ',elm1)

# for j in list_2:
#     elm2=list_2[index2]
#     index2 +=1
#     #print('M2: ',j)

# if elm1 == elm2:
#     # commenList.append[elm1]
#     print(elm1)