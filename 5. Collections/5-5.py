'''Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

alien_color = "green"

if alien_color == "green":  
    print("The player just earned 5 points for shooting the alien.")
elif alien_color == "yellow":  
    print("The player just earned 10 points for shooting the alien.")
else:  
    print("The player just earned 15 points for shooting the alien.")
