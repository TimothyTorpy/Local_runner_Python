import random
##List of Random Words
w = ["apple", "banana", "cherry", "dog", "elephant", "flamingo", "giraffe", "hamburger", "iguana", "jacket"]

def a():
    """Function Returns a Random Word from the list of words made globally.
    """
    return random.choice(w)

def b():
    """Function sets 3 variables to the return values.
    1. x = Random Word.
    2. y = Empty List.
    3. z = a set number for something. 
    """
    x = a()
    y = []
    z = 6
    return x, y, z

def c(x, y):
    """Function Takes in two arguements. 
    X Is the generated Word passed in from Function F. 
    d starts as a empty string then adds each piece of E to it.
    If E is in Y then it adds E to D. if not it replaces a place holder with a "_".
    """
    d = ""
    for e in x:
        if e in y:
            d += e
        else:
            d += "_"
    return d

def f():
    """Function takes a input and makes sure that it is a single letter."""
    while True:
        g = input("Guess a letter: ").lower() ##convers a letter to lowercase
        if len(g) != 1 or not g.isalpha():
            print("Please enter a single letter.")##if the input is not equal to a lenght of 1
        else:
            return g

def h():
    x, y, z = b()###Unpacks the function of B into the variables.
    ## X = Unpackes the random word. 
    ## Y = The Empty list for the guessing game.
    ## Z = 6

    while z > 0:
        print("\nAttempts left:", z)
        print("Current word:", c(x, y))##Prints the current word with the letters from the game hangman. 

        g = f()##Calls the function F, will loop until a single letter is imputted.

        if g in y:
            print("You've already guessed that letter.")
        elif g in x:
            y.append(g)
            if c(x, y) == x:
                print("Congratulations! You guessed the word:", x)
                break
        else:
            y.append(g)
            z -= 1

    if z == 0:##End of the game if the attempts are 0.
        print("\nYou ran out of attempts. The word was:", x)
