import random
# store secret word
secret_word = 'water'
# store user's guesses
guess = ""
# how many times did the user guess?
guess_count = 0
guess_limit = 5
out_of_guesses = False

# keep looping while the guess is NOT = to secret word and NOT out of guesses
while guess != secret_word and not(out_of_guesses):
# if guess count is less than the limit, let the user guess
    if guess_count < guess_limit:
        guess = input("Enter a 5 letter word: ")
# Once the user guesses, add 1 to the guess count
# that way we can track that the user doesn't go outside the guess limit
        guess_count += 1
    else:
# When user is out of guesses, break out of while loop
        out_of_guesses = True
# when out of while loop, if user is out of guesses they lose
if out_of_guesses:
    print("Out of guesses, you lose!")
# If the guess = the secret word
else:
	print (guess + " is correct. You win!")
