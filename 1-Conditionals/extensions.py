file = input('Name of file? ').strip().lower()
if file == ('.gif'):
    print('image/gif')
elif file == ('.jpg') or ('.jpeg'):
    print('image/jpeg')
elif file == ('.png'):
    print('image/png')
elif file == ('.pdf'):
    print('application/pdf')
elif file == ('.txt'):
    print('text/plain')
elif file == ('.zip'):
    print('application/zip')
else:
    print('N/A')