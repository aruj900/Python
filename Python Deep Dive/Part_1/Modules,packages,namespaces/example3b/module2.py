print('Running module2.py')


import module1

def hello():
    print('module2 says Hello!\n and ...')
    module1.hello()