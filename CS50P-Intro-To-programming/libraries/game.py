import random
while True:
    try:
        level=int(input('Enter the level: '))
        if level<=0:
            continue
        break
    except ValueError:
        print('enter a numeric value')
        continue
    except EOFError:
        continue
secret = random.randint(1, level)
while True:
    try:
        guess = int(input(f"Guess: "))
        if guess<1:
            continue
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("too large!")
        else:
            print("Just right! ")
            break
    except ValueError:
        print("Please enter a numeric guess.")






