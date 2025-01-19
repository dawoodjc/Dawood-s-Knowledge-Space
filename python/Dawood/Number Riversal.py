x=int(input("Enter a number: "))
y=0
while(x>0):
    y = x%10 + y*10
    x=x//10
print("reverstd number",y)