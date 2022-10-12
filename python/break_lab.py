secret_word = "chupacabra"
counter = 0

while True:
    guess_word = input("Enter the secret word: ")
    if guess_word == secret_word:
        break
    counter += 1

if guess_word == secret_word:
    print("You've successfully left the loop.")