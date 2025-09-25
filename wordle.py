# word guessing game (wordle)

import pandas as pd
import random

def load_words(filename="wordlist.txt"):
    try:
        with open(filename, 'r') as file:
            words = [line.strip().lower() for line in file if len(line.strip()) == 5]
        if words:
            return words
    except FileNotFoundError:
        print("⚠️ NO custom words found. Falling back to default \"WORDLE\" word lists.")
    return None

def feedback(answer, guess):
    result = []
    for a, g in zip(answer, guess):
        if a == g:
            result.append("🟩")
        elif g in answer:
            result.append("🟨")
        else:
            result.append("⬜")
    return "".join(result)

def main():
    global valid_answers, valid_guesses

    valid_guesses = pd.read_csv('valid_guesses.csv', header=None)[0].str.lower().tolist()
    valid_answers = pd.read_csv('valid_solutions.csv', header=None)[0].str.lower().tolist()

    dictionary = set(valid_guesses + valid_answers)

    custom_words = load_words("wordlist.txt")
    if custom_words:
        print("✅ Using words from custom word list.")
        valid_answers = custom_words
        dictionary.update(valid_answers)

    answer = random.choice(valid_answers)
    attempts = 6
    print("Welcome to Wordle! Guess the 5-letter word.")

    while attempts > 0:
        guess = input(f"Attempt {7 - attempts}/6: ").lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if guess not in dictionary:
            print("Not a valid word.")
            continue
        result = feedback(answer, guess)
        print(result)
        if guess == answer:
            print("🎉 Congratulations! You guessed it right!")
            break
        attempts -= 1
    else:
        print(f"❌ Sorry, the word was: {answer}")

if __name__ == "__main__":
    main()