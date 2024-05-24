while(True):
    x="1 add"
    f="2 substract"
    r="3 multipli"
    u="4 divide"
    
    print(x)
    print(f)
    print(r)
    print(u)
    
    x=input()
    
    if(x=="1"):
        print("add")
        x=input()
        y=input()
        z=input()
        l=int(x)+int(y)
        if(int(z)==(l)):
            print("corect")
        else: 
            print("in corect")
    if(x=="2"): 
        print("substract")
        x=input()
        y=input()
        z=input()
        l=int(x)-int(y)
        if(int(z)==(l)):
            print("corect")
        else: 
            print("in corect")
    if(x=="3"):
        print("multipli")
        x=input()
        y=input()
        z=input()
        l=int(x)*int(y)
        if(int(z)==(l)):
            print("corect")
        else: 
            print("in corect")
    if(x=="4"):
        print("divide")
        x=input()
        y=input()
        z=input()
        l=int(x)/int(y)
        if(int(z)==(l)):
            print("corect")
        else: 
            print("in corect")
