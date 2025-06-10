def fattoriale(n:int) -> int:
    
    fattoriale: int = 1 

    for i in range(n):
        fattoriale *= n - i

    return fattoriale 

print(fattoriale(8))