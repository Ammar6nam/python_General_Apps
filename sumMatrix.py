numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]

def mean (lists):
    array=[]
    index1=0
    while index1 < len(lists):
        lists[index1]
        #print(numbers[index1])
        sum=0
        for i in lists[index1]:
            sum+=i
            range1=len(lists[index1])
            #print('Range',range1)
        #print('Sum',sum)
        avarage1=sum/range1
        array.append(avarage1)
        #x=list(avarage1)
        #print(avarage1)
        #print(x)
        index1+=1
    print(array)

mean(numbers)