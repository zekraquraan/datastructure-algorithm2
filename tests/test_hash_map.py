import pytest
from hash_table.hash_table import HashTable

def test_set():
    hashtable = HashTable()
    hashtable.set('key1', 'value1')
    assert hashtable.get('key1') == 'value1'
def test_retrieve():
    hashtable = HashTable()
    hashtable.set('key1', 'value1')
    assert hashtable.get('key1') == 'value1'

def test_non_existing_key():
    hashtable = HashTable()
    assert hashtable.get('non_existing_key') is None
def test_keys():
    hashtable = HashTable()
    hashtable.set('key1', 'value1')
    hashtable.set('key2', 'value2')
    hashtable.set('key3', 'value3')
    assert set(hashtable.keys()) == {'key1', 'key2', 'key3'}

def test_bucket_collision():
    hashtable = HashTable(size=2)  # Small size to force collision
    hashtable.set('key1', 'value1')
    hashtable.set('key2', 'value2')
    assert hashtable.get('key1') == 'value1'
    assert hashtable.get('key2') == 'value2'
def test_hashing():
    hashtable = HashTable(size=100)  # Large size to avoid collisions
    key = 'test_key'
    hashed_index = hashtable._HashTable__hash(key)
    assert 0 <= hashed_index < 100

