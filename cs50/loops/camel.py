i=input('CamelCase : ')
snake=''
for index, s in enumerate(i):
    if index==0:
        snake+=s.lower()
    elif s.isupper():
        snake+='_'+s.lower()
    else:
        snake+=s
print('snake_case is : ',snake)