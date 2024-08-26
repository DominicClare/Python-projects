#Secret word game
import os
Secret_word = input("Please enter a 5 letter word: ")
Secret_word_desc = input("Please input a description of your word (50 characters limit): ")
Secret_word_desc_length = len(Secret_word_desc)
Secret_word_length = len(Secret_word)
Guess = ""
Guess_limit = 6
Guess_count = 0
Guess_Limit_Reached = False
os.system('cls')

while Guess != Secret_word and Guess_Limit_Reached != True:
    if Secret_word_length > 5:
            print("Word character limit exceeded, please try again!")
            Secret_word = input("Please enter a 5 letter word: ")
            Secret_word_length = len(Secret_word)
            os.system('cls')
    else:
        if Secret_word_desc_length > 50:
            print("Description character limit exceeded, please try again!")
            Secret_word_desc = input("Please input a description of your word (50 characters limit): ")
            Secret_word_desc_length = len(Secret_word_desc)
            os.system('cls')
        else:
            if Guess_count < Guess_limit:
                print(Secret_word_desc)
                Guess=input("Please enter a guess: ")
                Guess_count +=1
                c = 0
                for i in Guess:
                    if Guess[c] == Secret_word [c]: 
                        print (str(i) + " Is in this word and is in the right position")
                    elif Guess[c] != Secret_word [c]:
                        if Secret_word.count(i) > 1 and Guess.count(i) == 1 and Guess[c] in Secret_word:
                            print (str(i) + " Is in this word twice and is in the wrong position")
                        elif Secret_word.count(i) == 1 and Guess.count(i) > 1 and Guess[c] in Secret_word:
                            print (str(i) + " Is only in this word once and is in the wrong position")
                        elif Guess[c] in Secret_word:
                            print (str(i) + " Is in this word and is in the wrong position")
                        elif Guess[c] != Secret_word [c]:
                                if Guess[c] not in Secret_word:
                                    print (str(i) + " Is not in this word")
                    c += 1
                c = 0
                print("You have had "+ str(Guess_count) + "/6 attempts")          
            else:
                Guess_Limit_Reached = True
if Guess_Limit_Reached:
    print("You lose! The word was" + str(Secret_word))
else: print("You win!")