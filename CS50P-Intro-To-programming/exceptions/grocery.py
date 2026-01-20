b={}
while True:
    try:
        item=input().upper().strip()
        if item in b:
            b[item]+=1
        else:
            b[item]=1
    except EOFError:
        break
for item in sorted(b):
    print(b[item], item)

