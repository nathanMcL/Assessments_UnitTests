# PokemonArray_ListManipulation.py
import re
import os 

# Read array data from the test files
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
    # Test file input paths
    base_dir = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the script
    pokemon_filepath = os.path.join(base_dir, "../DSA_Test_files/array_Pokemon_input.txt")

    # Regex pattern to exclude lines that are not character names
    pokemon_exclusion_pattern = r"^Generation|^Pokemon"

    # Load the Pokémon array from the file
    pokemon_array = read_array_file(pokemon_filepath, pokemon_exclusion_pattern)

    # Save the original array for restoration if needed
    original_pokemon_array = pokemon_array.copy()

    # Introduction
    print("Welcome to the Pokémon Array Manipulator!")
    print("Available Commands: insert i e, remove e, append e, sort, pop, reverse, print, reset, quit")
    print("Type your commands below:\n")

    # Process commands
    while True:
        # Display the current state of the Pokémon array
        print(f"Current Pokémon Array: {pokemon_array}")
        
        # Read the command
        command = input("Enter a command: ").strip().split()
        if not command:
            print("Invalid command. Please try again.")
            continue

        operation = command[0]

        try:
            if operation == "insert":
                index = int(command[1])
                element = command[2]
                pokemon_array.insert(index, element)
                print(f"Inserted '{element}' at index {index}.")
            elif operation == "remove":
                element = command[1]
                pokemon_array.remove(element)
                print(f"Removed first occurrence of '{element}'.")
            elif operation == "append":
                element = command[1]
                pokemon_array.append(element)
                print(f"Appended '{element}' to the array.")
            elif operation == "sort":
                pokemon_array.sort()
                print("Sorted the Pokémon array alphabetically.")
            elif operation == "pop":
                popped_element = pokemon_array.pop()
                print(f"Popped last element: {popped_element}.")
            elif operation == "reverse":
                pokemon_array.reverse()
                print("Reversed the Pokémon array.")
            elif operation == "print":
                print(f"Pokémon Array: {pokemon_array}")
            elif operation == "reset":
                pokemon_array = original_pokemon_array.copy()
                print("Restored the Pokémon array to its original order.")
            elif operation == "quit":
                print("Exiting the Pokémon Array Manipulator. Goodbye!")
                break
            else:
                print("Unknown command. Please try again.")
        except (IndexError, ValueError):
            print("Error processing command. Please check your inputs.")

    # Optional: Write the restored original array back to the file after quitting
    with open(pokemon_filepath, 'w') as file:
        file.write('\n'.join(original_pokemon_array))
    print(f"Original order saved back to the file: {pokemon_filepath}")

if __name__ == "__main__":
    main()
