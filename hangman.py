import random
# library that we use in order to choose 
# on random words from a list of words
 
name = input("What is your name? ")
# Here the user is asked to enter the name first
 
print(" Good Luck !", name)

print("Guess this word associated with Harry Potter")
 
words = ['HARRY', 'HERMIONE', 'RON', 'DRACO', 
         'DUMBLEDORE', 'HAGRID', 'SNAPE', 'VOLDEMORT', 
         'SIRIUS', 'BELLATRIX','MCGONAGALL'] 
 
# Function will choose one random
# word from this list of words
word = random.choice(words)
if word=='HARRY':
    print("Clue: Easiest to guess,the whole plot revolves around him.")
    
elif word=='HERMIONE':
    print("Clue: A smart girl with Ron and Harry as best friends.")
    
elif word=='RON':
    print("Clue: Harry's Roommate.") 
    
elif word=='DRACO':
    print("Clue: A sylethrin boy who could not get along with Harry's trio.") 
    
elif word=='DUMBLEDORE':
    print("Clue: headmaster of Hogwards.")    
    
elif word=='HAGRID':
    print("Clue: A halfgiant, favourite of golden trio.")    
    
elif word=='SNAPE':
    print("Clue: Secret Hero and head of Slytherin.")
    
elif word=='VOLDEMORT':
    print("Clue: A Slytherin tried to kill Harry,also known by the name The Dark Lord .") 
    
elif word=='SIRIUS':
    print("Clue: Harry's Godfather.")  
    
elif word=='BELLATRIX':
    print("Clue: A sound supporter of Voldemort.The escaped the prison of Azkaban.") 
    
elif word=='MCGONAGALL':
    print("Clue:Head of Gryffindor House. ")     
    
def display_hangman(turns):
    stages=[ 
            """" 
            |-------|
            |       (O)
            |      \\\\|//
            |        |
            |      // \\\\
            |
                 
                 
            """,
            """ 
            |-------|
            |      (O)
            |      \\\\|//
            |        |
            |       //
            |          
             
                 
            """,
            """
             |-------|
            |       (O)
            |      \\\\|//
            |        |
            |       
            |        
            
            """,
                 
            """
            |-------|
            |       (O)
            |      \\\\|
            |        |
            |       
            |        
            
                 
                 
            """,
            """
            |-------|
            |       (O)
            |        |
            |        |
            |       
            |
                
             
                 
            """,
                 
           """
            |-------|
            |       (O)
            |      
            |        
            |       
            |        
                 
          
            """,
            """
            |-------|
            |       
            |      
            |        
            |       
            |  
            
                
            
            """
           ]
      
    return stages[turns]

# any number of turns can be used here
turns = 6

print("Here is you Hangman!!")
print(display_hangman(turns))
 
print("Guess the characters")
 
guesses = ''
 
while turns > 0:
     
    # counts the number of times a user fails
    failed = 0
     
    # all characters from the input
    # word taking one at a time.
    for char in word: 
         
        # comparing that character with
        # the character in guesses
        if char in guesses: 
            print(char)
             
        else: 
            print("_")
             
            # for every failure 1 will be
            # incremented in failure
            failed += 1
             
 
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win") 
         
        # this print the correct word
        print("The character is: ", word) 
        break
     
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("Guess a character:").upper()
    # every input character will be stored in guesses 
    guesses += guess 
     
    # check input with the character in word
    if guess not in word:
         
        turns -= 1
         
        # if the character doesn’t match the word
        # then “Wrong” will be given as output 
        print("Wrong")
        print(display_hangman(turns))
         
        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("You Loose")