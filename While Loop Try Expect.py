while True:
    try:
        num = int(input("Enter a number: "))
        if (num % 2) == 0:
            print("{0} is Even".format(num))
        else:
            print("{0} is Odd".format(num))
    
        b = int(input("enter a value: "))
    except:
            print("Value is not valid Please try Again")
    