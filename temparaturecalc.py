
while True :
    str =input('Whats the temparature?numF/C  or \' q \' to quit ')
    if str[0].lower()=='q':
        break
    if str[len(str)-1].lower()=='f':
        print((float(str[:-1])-32)/1.8)
    elif str[-1].lower()=='c':
        print((float(str[:-1])*1.8)+32)
    else:
        print("Please enter f/c after the temparature")
    
print('good bye!') 

