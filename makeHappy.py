text =str(input('enter your text: '))
sadFace1=':('
happyFace1=':)'
sadFace2='8('
happyFace2='8)'
sadFace3='x('
happyFace3='x)'
sadFace4=';('
happyFace4=';)'
if sadFace1 in text:
    replace1=text.replace(sadFace1,happyFace1)
    print(replace1)
if sadFace2 in text:
    replace2=text.replace(sadFace2,happyFace2)
    print(replace2)
if sadFace3 in text:
    replace3=text.replace(sadFace3,happyFace3)
    print(replace3)
if sadFace4 in text:
    replace4=text.replace(sadFace4,happyFace4)
    print(replace4)

