import re

def tokenize_string(input_string):
    # Use regular expression to tokenize the string and remove special characters
    words = re.findall(r'\b\w+\b', input_string.lower())
    return words


def count_word_frequency(word_list):
    # Count the frequency of each word using a dictionary
    word_freq = {}
    for word in word_list:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


def find_first_repeated_word(word_list, word_freq):
    # Find the first word that occurs more than once
    for word in word_list:
        if word_freq[word] > 1:
            return word
    return None


def repeated_word(input_string):
    # Tokenize the input string
    words = tokenize_string(input_string)
    print("Tokenized words:", words)

    # Count word frequency
    word_freq = count_word_frequency(words)
    print("Word frequency:", word_freq)

    # Find the first repeated word
    repeated_word = find_first_repeated_word(words, word_freq)
    print("First repeated word:", repeated_word)

    return repeated_word


# Test case
input_string = "This is a test string with a repeated word. Test it."
result = repeated_word(input_string)
print("Result:", result)