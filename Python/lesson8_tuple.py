# A tuple
eggs = ('hello', 42, 0.5)

# It uses () instead of [] unlike list
# Tuple is immutable just like string

eggs[1]         #42
type(('hello',))        #<class 'tuple'>
type(('hello'))         #<class 'str'>

#Conversion from list to tuple and vice versa
tuple(['cat', 'dog', 5])        #('cat', 'dog', 5)
list(('cat', 'dog', 5))         #['cat', 'dog', 5]
list('hello')                   #['h', 'e', 'l', 'l', 'o']
