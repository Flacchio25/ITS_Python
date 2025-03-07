'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

def make_shirt(taglia:str="large", message:str="I love python"):

    print(f"la maglietta sarà una taglia {taglia} con su scritto \"{message}\"")

make_shirt()
make_shirt("medium")
make_shirt("S","i love java")