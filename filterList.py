l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
def digit_filter (inputs):
    filterdList=[]
    for i in inputs:
        if i.isalpha():
            filterdList.append(i)
    print(filterdList)

digit_filter(l33t)