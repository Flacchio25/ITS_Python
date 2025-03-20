def countdown(n:int) -> None:
    if n >=0 :
        while n:
            print(n)
            n = n - 1

    else:
        print("Error! Inserted number is negative!")

countdown(-5)

countdown(5)