secret_number = 777

print(
"""
+==================================+
| Welcome to my game, Muggle!      |
| Enter an integer number          |
| picked for you.                  |
| and guess what number I've       |
| So, What is the secret number?   | 
+==================================+
"""
)
guess_number = int(input("Type the secret number: "))
while guess_number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        guess_number = int(input("Type the secret number: "))
        if guess_number == secret_number:
            print("Well done, muggle! You are free now.")