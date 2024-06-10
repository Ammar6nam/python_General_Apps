def removeLeadingAndTrailingZeros (text):
    numbers='0123456789.'
    for i in text:
        if i in numbers:
            x= True
        else:
            x= False
    if x == True:
        number= complex(text)
        print(number.real)
    if x==False:
        print (text)
text=input('Enter your number pleas: ')
removeLeadingAndTrailingZeros(text)










#     com1=complex(text)
#     number=int(com1)
#     if number.isnumeric():
#         print(number)
#     else:
#         print(text)
# text1=input('Enter your operation: ')
# func=removeLeadingAndTrailingZeros(text1)


  # if text.isalpha():
    #     print (text)
    # if text.isnumeric():
    #     number=int(text)
    #     print(number)
