#Secret word game
Secret_word = input("Please enter a 5 letter word: ")
Secret_word_desc = input("Please input a description of your word (50 characters limit): ")
Secret_word_desc_length = len(Secret_word_desc)
Secret_word_length = len(Secret_word)
Guess = ""
Guess_limit = 6
Guess_count = 0
Guess_Limit_Reached = False
#Variables all stored above

while Guess != Secret_word and Guess_Limit_Reached != True:
    if Secret_word_length > 5:
            print("Word character limit exceeded, please try again!")
            Secret_word = input("Please enter a 5 letter word: ")
            Secret_word_length = len(Secret_word)
    else:
        if Secret_word_desc_length > 50:
            print("Description character limit exceeded, please try again!")
            Secret_word_desc = input("Please input a description of your word (50 characters limit): ")
            Secret_word_desc_length = len(Secret_word_desc)
        else:
            if Guess_count < Guess_limit:
                print(Secret_word_desc)
                Guess=input("Please enter a guess: ")
                Guess_count +=1
                if Guess[0] == Secret_word[0]:
                    print("First letter correct!")
                if Guess[1] == Secret_word[1]:
                    print("Second letter correct!")
                if Guess[2] == Secret_word[2]:
                    print("Third letter correct!")
                if Guess[3] == Secret_word[3]:
                    print("Fourth letter correct!")
                if Guess[4] == Secret_word[4]:
                    print("Fifth letter correct!")
                print("You have had "+ str(Guess_count) + "/6 attempts")        
            else:
                Guess_Limit_Reached = True
if Guess_Limit_Reached:
    print("You lose!")
else: print("You win!")