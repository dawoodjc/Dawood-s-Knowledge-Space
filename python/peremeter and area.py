while(True):
    x="1 find area"
    y="2 find peremeter"

    print(x)
    print(y)

    z=input("enter 1 or 2: ")
    u=input("enter num:")
    t=input("enter num:")  
    if(int(z)==1):
        print(int(u)*int(t))
    if(int(z)==2):    
        print(int(u)*2+int(t)*2)