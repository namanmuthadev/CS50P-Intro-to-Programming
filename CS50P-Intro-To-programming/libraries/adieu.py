names = []
n=0
while True:
    try:
        if n<=0:
             #for the first name inputed
             lines=input('Name: ')
             n+=1
             names.append(lines)
        else:
             #for the subsequent name inputed
             line = input("")
             names.append(line)
        if len(names)==1:
            #to print when there is only one name
            print(f'Adieu, adieu, to {names[0]}')
        elif len(names)==2:
            #to print when there are two names
            print(f'Adieu, adieu, to {names[0]} and {names[-1]}')
        else:
            #to print when there are more than two names
            print(f'Adieu, adieu, to {", ".join(names[:-1])}, and {names[-1]}')




    except EOFError:
        #to break the loop when EOF is reached
        break

