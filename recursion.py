#this file is simple example of recursion

def printingVal(a):
    if a==0:
        return
    print(a)
    printingVal(a-1)


printingVal(10)    
