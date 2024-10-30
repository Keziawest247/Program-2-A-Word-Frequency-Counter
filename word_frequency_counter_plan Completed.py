"""Word Frequency Counter"""

filename = "zen_of_python.txt"

### Read Text File Function ###
def read_text_file(filename: str) -> str:
    """Read text file and return contents.

        Args:
           filename: This is the name of the file to be read.

       Returns:
          A string of characters.

    """
    with open(filename, mode="r") as text_file:
        return text_file.read()


### File Contents Parser Function ###
def file_content_parser(text: str) -> list:
    """Parse raw file contents to leave only alphanumeric chars and spaces.

        This function parses the contents of the file by iterating over all
        characters in the file, and when an alphanumeric character or space
        is detected, it is concatenated to a new string. This new string
        is then split and returned as a list of lower-case words.


        Args:
            text: This is the raw string which comes from the text file.

        Returns:
           A parsed list of words.
    """
    desired_character = ""

    for char in text:
        if char.isalnum() or char.isspace():
            desired_character += char.lower()


    return desired_character.split()


### Frequency Dictionary Builder Function ###
def frequency_dict_builder(parsed_words: list) -> dict:
    """This function creates a blank dictionary, and then iterates 
    over the list of parsed words.
    
    This function accepts the list of parsed words, and iterates over them.
    If the word does not appear in the dict. it is added with a value of 1,
    if the word already appears then its value is incremented. The dictionary
    is then passed to the sorted function where it is sorted by value and returned.


    Args:
        parsed_words: This is the parsed list of words.

    Returns:
       A sorted dictionary.
    """
    word_dict = {}
# iterate over the list parsed words.
    for word in parsed_words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return dict(sorted(word_dict.items(), key=lambda item : item[1], reverse=True))


# Step 1: Define the name of the text file.
filename = "zen_of_python.txt"

# Step 2: filename is passed to read_text_file which returns contents to 'raw_contents'
raw_contents = read_text_file(filename)

# Step 3: the string is passed to 'file_content_parser' which cleans the string and returns a list of parsed words
parsed_words = file_content_parser(raw_contents)

# Step 4: the list is passed to 'frequency_dict_builder' which returns frequency dictionary.
word_dict = frequency_dict_builder(parsed_words)

# Step 5: Use dictionary to print the words in text_file.
for word, freq in word_dict.items():
    out_string = f"The Word '{word}' appears {freq} times" if freq > 1 else f"The Word '{word}' appears once."
    print(out_string)






