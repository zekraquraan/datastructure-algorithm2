import pytest
from hashmap_left_join.hashmap_left_join import leftJoin, HashTable

def test_leftJoin():
    # Create two hash maps
    hm1 = HashTable()
    hm1.set("happy", "joyful")
    hm1.set("sad", "unhappy")
    hm1.set("big", "large")

    hm2 = HashTable()
    hm2.set("happy", "sad")
    hm2.set("angry", "calm")
    hm2.set("big", "small")

    result = leftJoin(hm1, hm2)

    expected_result = [['happy', 'joyful', 'sad'], ['sad', 'unhappy', None], ['big', 'large', 'small']]

    assert result == expected_result


def test_leftJoin_empty():
    hm3 = HashTable()
    hm4 = HashTable()
    result2 = leftJoin(hm3, hm4)
    assert result2 == []

def test_leftJoin2():
    hm1 = HashTable()
    hm1.set("dog", "puppy")
    hm1.set("cat", "kitten")
    hm1.set("fish", "fry")

    hm2 = HashTable()
    hm2.set("dog", "adult")
    hm2.set("lion", "cub")
    hm2.set("fish", "adult")

    result3 = leftJoin(hm1, hm2)
    expected_result3 = [['dog', 'puppy', 'adult'], ['cat', 'kitten', None], ['fish', 'fry', 'adult']]
    assert result3 == expected_result3

def test_leftJoin3():
    hm7 = HashTable()
    hm7.set("apple", "fruit")
    hm7.set("book", "read")
    hm7.set("car", "drive")
    hm7.set("door", "open")

    hm8 = HashTable()
    hm8.set("book", "write")
    hm8.set("apple", "healthy")
    hm8.set("dog", "pet")
    hm8.set("car", "vehicle")

    result4 = leftJoin(hm7, hm8)
    expected_result4 = [['apple', 'fruit', 'healthy'], ['book', 'read', 'write'], ['car', 'drive', 'vehicle'], ['door', 'open', None]]
    assert result4 == expected_result4