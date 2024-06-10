text=input('Enter the number: ')
alphapet='abcdefghijklmnopqrstuvwxyzäöüß '
for i in text:
    if i in alphapet:
        x=1
    else:
        x=2
if x==1:
    print(text)
if x==2:
    num=complex(text)
    print(num.real)
        
# str1=str(text)
# int1=int(text)
# float1=float(text)
# complex1=complex(text)
# print(x)
# print(int1)
# print(float1)
# x=complex(text)

# print(x.real)