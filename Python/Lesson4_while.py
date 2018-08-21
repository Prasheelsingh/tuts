spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1


#the break statement will end the loop
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')



#the continue statement causes the program execution to jump back to the start of the loop
while True:
  print('Who are you?')
  name2 = input()
  if name2 != 'A':
    continue
  else:
    break
print('Hello, A. How are you') 



#if name is blank, it will restart loop
name3 = ''
while not name3:
    print('Enter your name:')   
    name3 = input()
print('Hello, ' + name3) 
