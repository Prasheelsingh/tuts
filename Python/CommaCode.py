def comma(tab):
    count = len(tab)
    j = 0
    string = ''
    for i in tab:
        j += 1
        if j == count:
            string = string  + ', and ' + i
        elif j == 1:
            string = i
        else:
            string = string  + ', ' + i
    print(string)

spam = ['aaples', 'bananas', 'tofu', 'cats']
comma(spam)

