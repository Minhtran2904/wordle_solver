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
