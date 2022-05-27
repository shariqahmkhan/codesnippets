def operations():
    print("Enter your 1st Variable")
    a = int(input())
    print("Enter your 2nd Variable")
    b = int(input())
    p = input("Choose sum/difference/multiply/division/modulus")
    if p == 'sum':
        print(a+b)
    elif p=='difference':
        print(abs(a-b))
    elif p=='multiply':
        print(a*b)
    elif p=='division':
        print(a/b)
    elif p=='modulus':
        print(a%b)
    
operations()  

