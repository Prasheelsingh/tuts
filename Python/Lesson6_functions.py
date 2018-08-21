def name():
    print('Hello!')
name()

def name(Jim):
    print('Hello, ' + Jim + '!')

name('Jim')


def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()              # Prints 99


def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)         # Prints spam

