from hash_map_repeated.hash_map_repeated import repeated_word,find_first_repeated_word,count_word_frequency,tokenize_string
import pytest
def test_repeated_word():
    
    input_string1 = "This is a test string with a repeated word."
    assert repeated_word(input_string1) == "a"

   
    input_string3 = "hello my name is eman, dad name is mohammad and mum name kholod"
    assert repeated_word(input_string3) == "name"

    print("All test cases passed!")



test_repeated_word()