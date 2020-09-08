for i in range(101):

    if (i%3==0 and i%5!=0):
        print ("fizz",i)   
    elif (i%5==0 and i%3!=0):
        print ("buzz",i)  
    elif (i%5==0 and i%3==0 ):
        print ("fizzbuzz",i)  
    else :
        print(i)