import json
from difflib import get_close_matches

# Load dictionary data from JSON file
def load_dictionary():
    with open("dictionary.json") as f:
        data = json.load(f)
    return data

# Function to get definition of a word
def get_definition(word, data):
    # Convert word to lowercase for case-insensitive matching
    word = word.lower()
    if word in data:
        return data[word]
    # Check for similar words using difflib if exact match not found
    elif len(get_close_matches(word, data.keys())) > 0:
        suggested_word = get_close_matches(word, data.keys())[0]
        confirm = input("Did you mean '{}' instead? Enter 'Y' for yes, 'N' for no: ".format(suggested_word)).lower()
        if confirm == 'y':
            return data[suggested_word]
    return "Word not found in dictionary."

def main():
    dictionary_data = load_dictionary()
    word = input("Enter a word to get its definition: ")
    definition = get_definition(word, dictionary_data)
    print(definition)

if __name__ == "__main__":
    main()
