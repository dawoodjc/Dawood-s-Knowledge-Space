while(True):
    print("convert celsius to fahrenheit=1")
    print("convert fahrenheit to celsius=2")
    print("exit=3")

    x=input()

    if(int(x)==1):
        print("enter your celsius")
        y=input()
        print("celsius convert to fahrenheit")
        print(int(y)*9/5+32)
    if(int(x)==2):
        print("enter your fahrenheit ")
        z=input()
        print("fahrenheit  convert to celsius")
        print(int(z)-32*5/9)
    if(int(x)==3):
        break
    else:
        print("invalied choice")