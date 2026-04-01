def add(a,b):
    return a+b


def sub(a,b):
    return a-b

def multi(a,b):
   return a*b


def divide(a,b):
   return a/b

def divide2(a,b):
   return a//b
def mod(a,b):
    return a%b

def main():
    a=int(input("Enter a number: "))
    b= int(input("Enter a number: "))
    print(a,"+",b,"=",add(a,b))
    print(a, "-", b, "=", sub(a, b))
    print(a,"*",b,"=",multi(a,b))
    print(a, "/", b, "=", divide(a, b))
    print(a, "//", b, "=", divide2(a,b))
    print(a, "%", b, "=", mod(a,b))
if __name__ == '__main__':
    main()






