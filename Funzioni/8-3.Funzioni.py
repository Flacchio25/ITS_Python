'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

def make_shirt(taglia:str, messaggio:str):
    print(f"La taglia è la {taglia} e il messaggio sopra è {messaggio}")

make_shirt("M", "New york")
make_shirt(messaggio = "mamma leo", taglia = "M" )