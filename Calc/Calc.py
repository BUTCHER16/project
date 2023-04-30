#defining the calc function
def add(a,b):
    print(a + b)

def sub(a,b):
    print(a - b)

def mul(a,b):
    print(a * b)

def div(a,b):
    try:
        div=a/b
        print(div)
    except Exception:
        print("Invalid Entry")

while True:
    print("""A.  Addition
        B.  Subraction
        C.  Multiplication
        D.  Division
        E.  Exit""")
    
    choice=input("Input Your Choice : ")

    if choice == "a" or choice == "A":
        print("Addition")
        a=int(input("Enter the a "))
        b=int(input("Enter the b "))
        add(a,b)
    
    elif choice == "b" or choice == "B":
        print("Subraction")
        a=int(input("Enter the a "))
        b=int(input("Enter the b "))
        sub(a,b)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a=int(input("Enter the a "))
        b=int(input("Enter the b "))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a=int(input("Enter the a "))
        b=int(input("Enter the b "))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("Exited")
        quit()

    

    
    