names = []
n=0
while True:
    try:
        if n<=0:
             lines=input('Name: ')
             n+=1
             names.append(lines)
        else:
             line = input("")
             names.append(line)
        if len(names)==1:
            print(f'Adieu, adieu, to {names[0]}')
        elif len(names)==2:
            print(f'Adieu, adieu, to {names[0]} and {names[-1]}')
        else:
            print(f'Adieu, adieu, to {", ".join(names[:-1])}, and {names[-1]}')




    except EOFError:
        break

