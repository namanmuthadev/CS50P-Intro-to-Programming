n=input('enter file name : ').strip().lower()
if n.endswith('.gif'):
    print('image/gif')
elif n.endswith('.jpg'):
    print('image/jpeg')
elif n.endswith('.jpeg'):
    print('image/jpeg')
elif n.endswith('.png'):
    print('image/png')
elif n.endswith('.pdf'):
    print('application/pdf')
elif n.endswith('.zip'):
    print('application/zip')
elif n.endswith('.txt'):
    print('text/plain')
else:
    print('application/octet-stream')
