def sum (n: int) -> int:
    if n < 0 :
        print("Error! Inserted number is negative!")
        return None
    else:
        sum:int = 0 
        while n:
            sum = sum + n
            n = n-1
        return int(sum)