## _Main Purpose of the Program_ ##

  Upon carefule consideration of the programming style, it has been found that the instructor Bo Cen wanted to pull a fast one on some students by creating a devious plot of hide the game of HangMan, or word guess. With limited psycological training i can only assume it was a favorite game durring child hood.

## _Vairiable *W*_ ##

The Variable or List of words, is  globally spect'ed value of random words that will be drawn from down the road in latter function.

## Function f() ##

 This carefully crafted function intakes a persons input while the game is being played and preforms a poor coders regex to ensure that only a single char is in putted. If it is more then one Char, then the loop will not break and will re-ask for the guess. IF it is a single char then the function will return thus letter back too the game.

## Function h() ##

 Function H which oddly sounds like a ingredient in creating a evil power puff Girl/ villian most likely stands for function hangman, the function is the game. It brings in the other Function (B) and unpacks the tupple into the associated values. From there the other functions from above, take the word, and the parsed letter and checks to see if it is in the word (Function C) if it is then the count down does not go down and produces the opertunity to guess again. If the Guess is not in the word, then you subtract 1 from z (Remaining guesses). If the word is guessed then the games ends with a win. if z reaches 0 then the while loop is ended and you are informed politely that you have lost the game.
