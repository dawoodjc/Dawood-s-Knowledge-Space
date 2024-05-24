while(True): 
    print("1=kg into g")
    print("2=g into Kg")
    x=input()


    if(int(x)==1):
        print("kg into g")
        y=input()
        print(int(y)*1000)
    else:
        if(int(x)==2):
            print("g into mg")
            y=input()
            print(int(y)/1000)