"""Chardle."""


new_word: str = input("Enter a 5-character word: ")


if len(new_word) > 5:
    print("Error: Word must contain 5 characters.")
    quit()
else:
    if len(new_word) < 5:
        print("Error: Word must contain 5 characters.")
        quit()
        

character_search: str = input("Enter a single character: ")
counter: int = 0


print(f"Searching for {character_search} in {new_word}")
if len(character_search) > 1:
    print("Error: Character must be a single character")
    quit()
else:
    if character_search == new_word[0]:
        print(f"{character_search} found at index 0.")
        counter += 1
    
    if character_search == new_word[1]:
        print(f"{character_search} found at index 1.")
        counter += 1
    
    if character_search == new_word[2]:
        print(f"{character_search} found at index 2.")
        counter += 1

    if character_search == new_word[3]:
        print(f"{character_search} found at index 3.")
        counter += 1
    
    if character_search == new_word[4]:
        print(f"{character_search} found at index 4.")
        counter += 1
   
print(f"{counter} instances of {character_search} found in {new_word}.")
quit()  # this is not a necessary thing but it makes my life easier.
                    
