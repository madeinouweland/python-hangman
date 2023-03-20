import data
import random

mystery_words = ["ANGEL", "CLOUDY", "SUNSHINE"]
mystery_word = random.choice(mystery_words)

wrong_guesses = []
partial_solution = "_" * len(mystery_word)

print(data.gallows[len(wrong_guesses)])
print(f"Word: {partial_solution}")

while len(wrong_guesses) < len(data.gallows) - 1 and partial_solution != mystery_word:
    c = input("Your guess: ").upper()
    if c in mystery_word:
        for i, x in enumerate(mystery_word):
            if x == c:
                partial_solution = partial_solution[:i] + c + partial_solution[i+1:]
    else:
        if c not in wrong_guesses:
            wrong_guesses.append(c)
    print(data.gallows[len(wrong_guesses)])
    print(f"Word: {partial_solution}, Wrong guesses: {', '.join(wrong_guesses)}")
    
if mystery_word == partial_solution:
    print("You have won.")
else:
    print(f"You have lost. The word was: {mystery_word}")