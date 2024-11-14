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
        print("enter value in yard")
        u=input()
        print("yard converted into inches is")
        print(int(u)*36)
    elif(i=="2"):
        print("enter value in feet")
        u=input()
        print("feet converted into iches is")
        print(int(u)*12)
    elif(i=="3"):
        print("enter value in feet")
        u=input()
        print("feet converted into yard is")
        print(int(u)/3)
    elif(i=="4"):
        print("enter value in inches")
        u=input()
        print("inches converted into feet is")
        print(int(u)/12)
    elif(i=="5"):
        print("enter value in inches ")
        u=input()   
        print("inches converted into yard is")
        print(int(u)/36)
    elif(i=="6"):
        print("enter value in yard ")
        u=input()
        print("yard converted into feet is")
        print(int(u)*3)

    print("thank you")
