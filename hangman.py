import random
import turtle
numWin = 0
numLos = 0

def setUp(word):
    guessList = ['_'] *len(word)

    printing = ''
    for term in guessList:
        printing = printing + term + ' '

    print('Your word is: ', printing)

    return guessList

def levelTheme():
    
    print('THEMES \n--------')
    print('Animals \nComputers \nSports \nDogs \nElements \n--------')
    userTheme = input('Pick a theme: ')

    userTheme = userTheme.lower()
    themes = ['animals','computers','sports','dogs','elements']
    
    while userTheme not in themes:
        print('You have entered an INVALID theme!')
        userTheme = input('Try again by picking another theme: ')
        
    try:   
        userLevel = int(input('Pick a difficulty level from 1-3, with 3 being the hardest: '))
    except:
        userLevel = int(input('That was an INVALID level. Please chose 1, 2, or 3: ' ))
                        
    level = [1,2,3]

    while int(userLevel) not in level:
        print('You have entered an INVALID difficulty level!')
        userLevel = input('Try again. Pick a difficulty level from 1-3, with 3 being the hardest: ')

    choice = str(userLevel) + ' ' + userTheme

    return choice

def word(choice):
    choice = choice.split()
    
    #finding file for theme and level
    if choice[0] == '1':
        fin = open('easy'+str(choice[1])+'.txt','r')
    if choice[0] == '2':
        fin = open('medium'+str(choice[1])+'.txt','r')
    if choice[0] == '3':
        fin = open('hard'+str(choice[1])+'.txt','r')
        
    #makes a list of words in the file
    alist = []
    for line in fin:
       alist.append(line[:-1])
       
    #pulls word from list
    num = random.randint(0,len(alist)-1)
    word = alist[num]
        
    return word

def longGuess(guessList, wordList, guess):
     guessed = list(guess)
     comp = ''
     ch = 0
     for i in range(len(wordList)):
         while wordList[i] == guessed[ch]:
             comp = comp + guessed[ch]
             ch += 1
             i += 1
             
             if list(comp) == guessed:
                 stl = wordList.index(guess[0])
                 stg = 0
                 for g in range(len(guess)):
                     guessList[stl] = guessed[stg]
                     stl += 1
                     stg += 1
                 return guessList
                            
         ch = 0
         comaprison = ''

     return False

def guesses(guessList, word):
    wordList = list(word)
    count = 0
    guessed = []
    
    #interprets guess
    while '_' in guessList and count !=6:
        guess = input('Your guess? ')

        #if guessing more than one letter at a time
        if len(guess) != 1:
            result = longGuess(guessList,wordList, guess)
            
            #long guess was wrong
            if result == False:
                print('Sorry that was an incorrect guess. Don\'t worry, we\'ll only count that as one guess. \nYou have',5-count,'guesses left.')

                #adds guesses to guessed
                for i in range(len(guess)):
                    guessed.append(guess[i])

                #progress report
                guessPrint = ''
                for term in guessList:
                    guessPrint = guessPrint + term + ' '
                print('Your progress: ',guessPrint)
                count += 1
                draw(count)
                
            else:
                #long guess was correct
                guessed.append(guess)
                guessPrint = ''
                for term in guessList:
                    guessPrint = guessPrint + term + ' '
                print('Your progress: ',guessPrint)
                    
        #only guessing one letter         
        elif guess in wordList:
            
            #already guessed it
            if guess in guessList:
                print('You\'ve already guessed that letter. Try another')
                guessed.append(guess)
                
            else:
                #guessed letter in the word
                guessed.append(guess)
                for i in range(len(wordList)):
                    if wordList[i] == guess:
                        guessList[i] = guess
                        
                    guessPrint = ''
                    for term in guessList:
                        guessPrint = guessPrint + term + ' '
                        
                print('Your progress: ',guessPrint)
            
        else: #guess not in word
            #already guessed letter
            if guess in guessed:
                print('You\'ve already guessed that letter. Try another.')
            else:
                #wrong guess
                print('Sorry, that letter is not in the word. You have', 5 - count, 'more guesses.')
                count += 1
                guessed.append(guess)
                draw(count)
            
            
            guessPrint = ''
            for term in guessList:
                guessPrint = guessPrint + term + ' '
            print('Your progress:', guessPrint)
           

    return count

def winner(count, word):
    if count != 6:
        print('--------')
        print('Congrats you won!')
        global numWin
        numWin += 1
    else:
        print('--------')
        print('Sorry, you lost.')
        print('Your word was', word)
        global numLos
        numLos += 1

    replay = input('Would you like to play again? y/n ')
    
    while replay != 'y' and replay != 'n':
        replay = input('Please type "y" for yes or "n" for no ')
    
    if replay == 'y':
        turtle.clearscreen()
        turtle.bgcolor('black')
        return True
    else:
        print("-----------------")
        print('Final Score:')
        print('Wins:', numWin, 'Loses:', numLos)
        print("-----------------")
        return False
    

def draw(count):
    turtle.bgcolor('black')
    turtle.setworldcoordinates(-180,-105,50,100)
    t = turtle.Turtle()
    t.speed(5)
    t.pencolor('lavender')
    t.pensize(7)
    t.hideturtle()
    
    if count == 1:
        #draws gallows
        t.up
        t.setposition(0, -100)
        t.down()
        t.goto(25,-100)
        t.goto(-25,-100)
        t.goto(0,-100)
        t.goto(0,100)
        t.goto(-100,100)
        t.goto(-100,80)
        t.goto(-100,100)
        t.goto(-50,100)
        t.goto(0,50)
        
        #draws the head
        t.pencolor('mediumspringgreen')
        t.up()
        t.setposition(-100,30)
        t.down()
        t.circle(25)
        return

    elif count == 2:
        t.pencolor('mediumpurple')
        t.up()
        t.setposition(-100,30)
        t.down()
        t.goto(-100,-40)
        t.up()
        return 

    elif count == 3:
        t.pencolor('deeppink')
        t.up()
        t.setposition(-100,-40)
        t.down()
        t.goto(-115,-80)
        return

    elif count == 4:
        t.pencolor('deepskyblue')
        t.up()
        t.setposition(-100,-40)
        t.down()
        t.goto(-85,-80)
        return

    elif count == 5:
        t.pencolor('yellow')
        t.up()
        t.goto(-100,0)
        t.down()
        t.goto(-115,20)
        
        return 
        
    elif count == 6:
        t.pencolor('orangered')
        t.up()
        t.goto(-100,0)
        t.down()
        t.goto(-85,20)

def main():
    replay = True
    while replay == True:
        choice = levelTheme()
        guessWord = word(choice)
        guessList = setUp(guessWord)
        game = guesses(guessList,guessWord)
        replay = winner(game, guessWord)

main()
