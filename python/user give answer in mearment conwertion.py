while(True):
    x="1 yd into in"
    z="2 ft into in"
    y="3 ft into yd"
    q="4 in into ft"
    s="5 in into yd"
    d="6 yd into ft"
    
    print(x)
    print(z)
    print(y)
    print(q)
    print(s)
    print(d)

    i=input()
    
    if(i=="1"):
        u=input("enter value in yard: ")
        l=input("enter yard conwerted into inches:") 
        p=(int(u)*36)
        if(int(l)==p):    
            print("corect")
        else:
            print("incorect")
    elif(i=="2"):
        u=input("enter value in feet:")
        l=input("enter feet converted into iches: ")
        p=(int(u)*12)
        if(int(l)==p):
            print("corect")
        else:
            print("incorect")
    elif(i=="3"):
        u=input("enter value in feet: ")
        l=input("enter feet converted into yard: ")
        p=(int(u)/3)
        if(int(l)==p):   
            print("corect")
        else:
            print("incorect")
    elif(i=="4"):
        u=input("enter value in inches: ")
        l=input("enter inches converted into feet: ")
        p=(int(u)/12)
        if(int(l)==p):   
            print("corect")
        else:
            print("incorect")
    elif(i=="5"):
        u=input("enter value in inches: ")   
        l=input("enter inches converted into yard: ")
        p=(int(u)/36)
        if(int(l)==p):    
            print("corect")
        else:
            print("incorect")
    elif(i=="6"):
        u=input("enter value in yard: ")
        p=input("enter yard converted into feet: ")
        l=int(u)*3
        if(int(p)==l):
           print("corect") 
        else:    
            print("incorect")
            
