
secret_word: str = "knoll"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(secret_word) != len(guess_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

index: int = 0
result: str = ""


while index < len(secret_word):
    match_found: bool = False
    if guess_word[index] == secret_word[index]:
        result += GREEN_BOX
    else:
        i: int = 0
        while i < len(secret_word):
            if guess_word[index] == secret_word[i]:
                match_found = True
            i += 1
    
        if match_found is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
            
    index += 1

print(result)

if secret_word == guess_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")