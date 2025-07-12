print("Welcome to calculator")
print ("what do you want to do add,substract,multipli,divide")
t=input()
z=int(input("Enter First Number: "))
x=int(input("Enter Second Number: "))
if(t=="add"):
    print("add")
    print("your answer is")
    print(int(z)+int(x))
if(t=="substract"):
    print("substract")
    print("your answer is")
    print(int(z)-int(x))
if(t== "multiply"):
    print("multipli")
    print("your answer is")
    print(int(z)*int(x))
if(t=="divide"):
    print("divide")
    print("your answer is")
    print(int(z)/int(x))
