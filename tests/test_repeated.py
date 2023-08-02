from hash_map_repeated.hash_map_repeated import repeated_word
def test_repeated_word():
    # Test case 1: Regular sentence with a repeated word
    text1 = 'Once upon a time, there was a brave princess who...'
    assert repeated_word(text1) == 'a', "Test case 1 failed"

    # Test case 2: Multiple repeated words, first one should be returned
    text2 = 'It was the best of times, it was the worst of times...'
    assert repeated_word(text2) == 'it', "Test case 2 failed"

    # Test case 3: No repeated words, should return 'no words found'
    text3 = 'This is a test sentence without any repeated words.'
    assert repeated_word(text3) == 'no words found', "Test case 3 failed"

    # Test case 4: Repeated words with different capitalizations, should be treated as the same word
    text4 = 'This is a test sentence with a Repeated word and a repeated word.'
    assert repeated_word(text4) == 'a', "Test case 4 failed"

    # Test case 5: Empty string, should return 'no words found'
    text5 = ''
    assert repeated_word(text5) == 'no words found', "Test case 5 failed"

    print("All test cases passed.")

# Run the test cases
test_repeated_word()
