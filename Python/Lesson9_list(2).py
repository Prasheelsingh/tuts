spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)           #[0, 'Hello!', 2, 3, 4, 5]
print(spam)             #[0, 'Hello!', 2, 3, 4, 5]

spam.append('6')
print(spam)             #[0, 'Hello!', 2, 3, 4, 5, 6]
print(cheese)           #[0, 'Hello!', 2, 3, 4, 5, 6]

#When you assign a list to a variable, you are actually assigning a list reference to the variable.

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)                #['A', 'B', 'C', 'D']
print(cheese)              #['A', 42, 'C', 'D']
# The copy module allows you to pass a difference list reference than before

#cheese = copy.deepcopy(spam)           Used when my list contains another list

spam = ['1', '2', '3', 30, '5']
var = spam[int(int('3' * 2) // 11)]
print(var)

bar = ('A', 'B', 'C', 'D')
print(bar.index('C'))


