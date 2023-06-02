def get_word(filename: str):
    with open(filename) as f:
        for line in f:
            guess_list.append(line.strip())
            
def wordle_solver():
    for guesses in range(6):
        guess = input("\nword: ").lower()
        print("g - green, y - yellow, w - wrong / grey")
        feedback = input("Feedback: ").lower()
        if feedback == "ggggg":
            print("Well Done! Guess",guesses+1)
            break
            
    mytuple = tuple(guess_list)
        for letter in mytuple:
            for i in range(5):
                if feedback[i] == "w" and guess[i] in letter:
                    guess_list.remove(letter)
                    break
                elif feedback[i] == "g" and guess[i] != letter[i]:
                    guess_list.remove(letter)
                    break
                elif feedback[i] == "y" and guess[i] not in letter:
                    guess_list.remove(letter)
                    break
                elif feedback[i] == "y" and guess[i] == letter[i]:
                    guess_list.remove(letter)
                    break
