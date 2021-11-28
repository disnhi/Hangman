# Hangman - terminal version

## After cloning the repository, the game can be ran by typing this into the terminal: 

``` 
python3 hangman.py 
```


The code is divided into several functions with the main function acting as a driver.

First _**levelTheme**_ is called; this function gives the player a choice of five themes (Dogs, Animals, Computers...) from which they can choose. The player is also asked what level of difficulty they want to play for each theme has a set of easy, medium, and hard words. The player selections are returned in a string formatted: ‘level theme.’ 

This string is then sent to _**word**_. The correct file is opened based on the players selection and a random word is pulled out. The word is returned. The next function to be called is _**setUp**_ which takes the word from _**word**_ as a parameter. This function shows the player the length of the word they need to guess with a ‘_’ printed for each letter. There is a space between each for readability. The list of ‘_’s is returned and will be used to keep track of the letters the player has guessed correctly. This happens in guesses.

_**Guesses**_ interprets the guess that the player makes. It first determines if the guess is more than one letter long. If it is the following happens; first _**longGuess**_ is called which looks at the guess and sees if it is a substring ( or potentially the same string) as the word. If the guess is in the word it returns the list of guessed letters in the correct place in the word and ‘_' s, but if the guess is wrong it returns False. Back in guesses, the count of wrong letters is increased by 1 if the long guess was wrong and the guessed letters are added to a list of all letters guessed (wrong or right). 

This is done so that if the player tries to guess the same letter twice the program can inform them of this and not count it against them. An updated display of the guessed letters and missing letters is printed for the player’s next turn. If the guess is only one letter long it is first checked to see if it is in the word list. It is then checked against already guessed correct letters to see if the letter has been guessed already. The players progress is updated and printed for their next turn. If the letter is not in the word the player is informed and their number of wrong guesses is increased by one. 

Also, the function _**draw**_ is called with the number of wrong guesses sent to it as a parameter. Draw takes in the count and determines how much of the hangman to draw. When it is first called it draws the gallows and the head and then when the count is two(i.e it is called the second time) it draws the body, and then the left leg when the count is 3, then the right, and so on. Once either the count reaches 6 or there are no more ‘_’s in the guess list _**winner**_ is called. 

It requires the wrong guess count and the word as parameters. If the count is less than 6 it inform the player that they have won and, using a global variable, adds one to the players win count. If the number of wrong guesses is 6 it tells the player they have lost, tells them what the word was, and using a different global variable adds 1 to the loss count. It then asks the player if they would like to play again. If the player chooses yes then the wrong guess count is reset to 0, the drawn hangman is cleared, and True is returned. This will restart the loop in the main function, thus beginning the driver again. If the player does not wish to play again the final score is printed (number of wins and losses) and the program is ended.


The website ​https://www.enchantedlearning.com/wordlist/​ was used to compile the lists of words. 
