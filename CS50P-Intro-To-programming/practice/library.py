names = []
n=0
while True:
    try:
        if n<=0:
             book_name=input('book Name: ').upper().strip()
             n+=1
             names.append(book_name)
        else:
             the_rest = input("").upper().strip()
             names.append(the_rest)
        if len(names)==1:
            print(f'book name is, {names[0]}')
        elif len(names)==2:
            print(f'book names are, {names[0]} and {names[-1]}')
        else:
            print(f'book names are, {", ".join(names[:-1])}, and {names[-1]}')




    except EOFError:
        break

