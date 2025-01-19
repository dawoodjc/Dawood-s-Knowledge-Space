while(True):
    v=input("enter any number: ")
    g=input("enter any num: ")
    print("enter what you want to do with the numbers")
    print("+,*,-,/ or exit")
    x=input()
    if (x=="+"):
        print("add")
        print("your answer is")
        print(int(g)+int(v))
    if(x=="/"):
        print("divide")
        print("your answer is")
        print(int(v)/int(g))
    if(x=="*"):
        print("multipli")
        print("your answer is")
        print(int(v)*int(g))
    if(x=="-"):    
        print("substractoin")
        print("your answer is")
        print(int(v)-int(g))
    if(x=="exit"):
        break