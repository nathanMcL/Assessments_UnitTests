# Array
import re
import time # This is for the countdown timer

# Countdown Timer
def countdown_timer(seconds, message="Next section: List Manipulation starts in"):
    for i in range(seconds, 0, -1):
        print(f"{message} {i}...")
        time.sleep(1) # Pause for 1 second
    print("Starting Now!\n")

### Read the array data from the test files 
def read_array_file(file_path, pattern_to_exclude):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Use regex to exclude lines that are not character names (Section headers)
            return [line.strip() for line in lines if not re.match(pattern_to_exclude, line.strip())]    
    except FileNotFoundError:
        print(f"Error: File at {file_path} not found.")
        return []
    
def main():
    ### Test file input paths
    pokemon_filepath = r"DSA_Test_files/array_Pokemon_input.txt"
    emoji_filepath = r"DSA_Test_files/array_Emoji_input.txt"

    # Regex pattern to exclude lines that are not character names or emoji icons (Section Headers)
    pokemon_exclusion_pattern = r"^Generation|^Pokemon"
    emoji_exclusion_pattern = r"^Emoji|^Face Expressions|^Expressions|^Weather|^Sports|^Entertainment|^Miscellaneous"

    ### Read the array data from the test files
    pokemon_array = read_array_file(pokemon_filepath, pokemon_exclusion_pattern)
    emoji_array = read_array_file(emoji_filepath, emoji_exclusion_pattern)

    # Save the original order of the Pokemon array test file.
    original_pokemon_array = pokemon_array.copy()

    # Display the arrays
    #print("Filtered Pokémon Array:", pokemon_array)
    #print("Filtered Emoji Array:", emoji_array)

    ## In this section, We want to allow the user to implement their own array access methods...
    ##... Access specific elements in the test files and display them to the user...

    # Access specific elements
    # There are 59 Pokémon in the file.
    # Access
    try:
        index = int(input("Enter an index to access a Pokémon: (0-based index): "))
        if 0 <= index < len(pokemon_array):
            print(f"Pokémon at index {index}: {pokemon_array[index]} ")
        else:
            print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer index.")

    # There are 88 emojis in the file
    try:
        index = int(input("Enter an index to access an Emoji: (0-based index): "))
        if 0 <= index < len(emoji_array):
            print(f"Emoji at index {index}: {emoji_array[index]}")
        else:
            print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer index.")

    # Countdown Timer for the List Manipulation Section
    countdown_timer(5)

    # List Manipulation...
    print("List Manipulation starts now...")

    # In this section, we have to know what it is that we are wanting to do with the array...
    # For starters we might want to:
    # 1. insert Charmander into the first index position 0 of the array_Pokemon_input test file. 
    # 2. remove Charmander: Delete the first occurrence of Charmander.
    # 3. append Charmander: Insert Charmander at the Top of the Pokemon OGs list.
    # 4. sort: Sort the Pokemon OGs list alphabetically.
    # 5. pop: Pop the last element from the new sorted Pokemon OGs list and print the character name that was popped.
    # 6. reverse: Reverse the list order.

    # 1. insert Charmander into the first index position 0 of the array_Pokemon_input test file.
    pokemon_array.insert(0, "Charmander")
    print(f"After inserting 'Charmander' at index 0: {pokemon_array}\n")

    countdown_timer(1)

    # 2. Remove the first occurrence of 'Charmander'.
    if "Charmander" in pokemon_array:
        pokemon_array.remove("Charmander")
        print(f"After removing 'Charmander': {pokemon_array}\n")
    else:
        print("'Charmander' not found in the array.")

    countdown_timer(1)

    # 3. Append 'Charmander' to the array.
    pokemon_array.append("Charmander")
    print(f"After appending 'Charmander': {pokemon_array}\n")

    countdown_timer(1)

    # 4. Sort the Pokemon array alphabetically.
    pokemon_array.sort()
    print(f"After sorting alphabetically: {pokemon_array}\n")

    countdown_timer(1)

    # 5. Pop the last element from the sorted array.
    popped_element = pokemon_array.pop()
    print(f"Popped Element: {popped_element}")
    print(f"Array after popping the last element: {pokemon_array}\n")

    countdown_timer(1)

    # 6. Reverse the array.
    pokemon_array.reverse()
    print(f"After reversing: {pokemon_array}\n")
    print(f"\n")

    # End of the List Manipulation Section

    # 7. Restore the original order of the Pokemon array
    pokemon_array = original_pokemon_array
    print(f"Restored to original order: {pokemon_array}\n")

    # Optional: Write the original array back to the file after all manipulatuions are done.
    # This can be commented out. Purely Optional.
    with open(pokemon_filepath, 'w') as file:
        file.write('\n'.join(original_pokemon_array))
    print(f"Original order saved back to the file: {pokemon_filepath}")


# Main
if __name__ == "__main__":
    main()

# Notes:
# - Filter the array to exclude non-character entries such as section headers