#Secret word game
import os
os.system("")
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\33[33m'
    YELLOWBG = '\33[43m'
    RESET = '\033[0m'
Secret_word = input("Please enter a 5 letter word: ")
Secret_word_desc = input("Please input a description of your word (50 characters limit): ")
Secret_word_desc_length = len(Secret_word_desc)
Secret_word_length = len(Secret_word)
Guess = ""
Guess_Length = len(Guess)
Guess_limit = 6
Guess_count = 0
Guess_Limit_Reached = False
os.system('cls')

while Secret_word_length !=5:
    print("Word character limit exceeded, please try again!")
    Secret_word = input("Please enter a 5 letter word: ")
    Secret_word_length = len(Secret_word)
    os.system('cls')
while Secret_word_desc_length > 50:
    print("Description character limit exceeded, please try again!")
    Secret_word_desc = input("Please input a description of your word (50 characters limit): ")
    Secret_word_desc_length = len(Secret_word_desc)
    os.system('cls')
print (style.GREEN + "{0}".format("right letter, right place ") + 
       style.YELLOW + "{0}".format("in word twice, in wrong place ") + 
       style.YELLOWBG + "{0}".format("in word once only ") + style.RESET,
       style.BLUE + "{0}".format("right letter, wrong place ") + 
       style.RED + "{0}".format("not in this word") + style.RESET)

while Guess != Secret_word and Guess_Limit_Reached != True:
    if Guess_count < Guess_limit:
        print(Secret_word_desc)
        Guess=input("Please enter a guess: ")
        Guess_Length = len(Guess)
        if Guess_Length != 5:
            print("Your guess is the incorrect length, please try again!")
            Guess=input("Please enter a guess: ")
            Guess_Length = len(Guess)
        else:  
            Guess_count += 1
            c = 0
            for i in Guess:
                if Guess[c] == Secret_word [c]: 
                    print (style.GREEN + "{0}".format(str(i)) + style.RESET, end = " ")
                elif Guess[c] != Secret_word [c]:
                    if Secret_word.count(i) > 1 and Guess.count(i) == 1 and Guess[c] in Secret_word:
                        print (style.YELLOW + "{0}".format(str(i)) + style.RESET, end = " ")
                    elif Secret_word.count(i) == 1 and Guess.count(i) > 1 and Guess[c] in Secret_word:
                        print (style.YELLOWBG + "{0}".format(str(i)) + style.RESET, end = " ")
                    elif Guess[c] in Secret_word:
                        print (style.BLUE + "{0}".format(str(i)) + style.RESET, end = " ")
                    else:
                        print (style.RED + "{0}".format(str(i)) + style.RESET, end = " ")
                c += 1
            c = 0
        print("You have had "+ str(Guess_count) + "/6 attempts")       
    else:
        Guess_Limit_Reached = True
if Guess_Limit_Reached:
    print("You lose! The word was " + str(Secret_word))
else: print("You win!")