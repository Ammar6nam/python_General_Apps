def mathExpression(stext):
    text=stext.lower()
    A='abcdefghijklmnopqrstuvwxyzäüßµ@€'
    B='+-/*%'
    index1=1
    index2=1

    for i in text:
        if i in A: # it means that it is letter ==> 0
            x= 0
        else:
            x=1 # it means it is number or space ==> 1
        index1*=x
        c1=bool(index1)
#print(c1)
    #print (x)
#print(x)

#print(' ----------------------------------- ')
    for j in text:
        if j in B: # it is  complete the condition
            y=0
        else:
            y=1
        index2*=y
    c2=not bool(index2)
#print(c2)

    if c1 and c2:
        return (True)
    else:
        return (False)
text=input('Enter your text: ')
e=mathExpression(text)
print(f'{text} -->  {e}')


#     else:
#         x=1
#     index+=1
# if x ==0:
#     print(False)
# if x ==1:
#     print(True)


# x=text.isnumeric()
# y=text.isspace()
# z=text.isdigit()
# i=text.isalpha()
# p=text.isalnum()

# print(x)
# print(y)
# print(z)
# print(i)
# print(p)



# if x or y :
#     print(True)
# else:
#     print(False)
# if '+' or '-' or '*' or '/' or '%' in text() and not x:
# if (alphabet1.split()in text) and '+' or '-' or '*' or '/' or '%' in text():
#     print (True)
# else:
#     print (False)
# x=text.isspace()
# text=input('Enter your text: ')
# text.is

#     print (True)
# else:
#     print (False)