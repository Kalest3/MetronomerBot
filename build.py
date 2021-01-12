import os.path
usernamexists = os.path.exists('username.txt')
passwordexists = os.path.exists('password.txt')
if usernamexists == False:
    print('Creating username.txt file...')
    open('username.txt', 'w+')
    print('username.txt has been created!')
else:
    print('username.txt exists. Nothing happens...')
if passwordexists == False:
    print('Creating password.txt file...')
    open('password.txt', 'w+')
    print('password.txt has been created!')
else:
    print('password.txt exists. Nothing happens...')