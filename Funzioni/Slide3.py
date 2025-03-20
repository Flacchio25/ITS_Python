def countdown(n:int) -> None:
# n is negative
    if n < 0 :
        print("Error! Inserted number is negative!")
#n = 0 most stop recursive process
    elif n == 0:
        print(0)
# other cases
    else:
        print(n)
        countdown(n-1)

