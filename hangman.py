
import random
word_list = ["python", "code","app","website"]

def display_word(word , guessed):
    display =""
    for letter in word:
        if letter in guessed :
            display += letter
        else:
            display +="_"
    return  display

def hangman():
    word = random.choice(word_list)
    guessed_letters = set()
    attempts= 6

    while attempts >0:
        print("Welcom to hangman!")
        print(f"Word :{ display_word(word= word,guessed =guessed_letters)}")
        print(f"Guessed Letters :{" ".join(guessed_letters)}")
        print(f"Remaining Attempts :{attempts}")

        guess = input("Enter the letter :").lower()
        guessed_letters.add(guess)

        if guess in word:
            print("Good Guess!")
        else:
            print("Wrong Guess!")
            attempts -=1
        
        if "_" not in display_word(word,guessed_letters):
            print("Congratulation's,You Won ")
            print(f"The word was :{word}")
            break
    else :
        print("You failed")

if __name__ == "__main__":
   hangman() 