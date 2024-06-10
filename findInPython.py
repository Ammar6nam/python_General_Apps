text=str(input('Enter your text please: '))
word=str(input('Which word you want to search for it? '))
#index=text.index(word)
find1=text.find(word)
#print(find1)
#print(bool(find1))
#print(index)
#print (text,word)
if word in text:
    print(f'I found {word} at [{find1}]!')
else:
    print(f"I can't find {word} :( ")


# index=0
# z1=0
# find1=text.find(word)
# length=len(text)
# for x in text:
#     char = text[index]
#     if find1 :
#         y=[index]
#         z1 +=1
#     index += 1
# if z1 !=0 :
#     print(f'I found {word} at index[{y}]!')
# else:
#     print(f"I can't find {word} :( ")
# print (length)
# for i in text:
#     char=text[index]
#     index+=1
#     if word in text:
#         x=index
#print(x)
# find1=text.find(word)
# if find1 :
#     print(f'I found {word} at [index]!')
# else:
#     print(f"I can't find {word} :( ")