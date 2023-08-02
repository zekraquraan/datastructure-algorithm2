# Hash Table

## author :Zekra Quraan

## white board:
[whiteboard](./ttt1.png)

## Approach & Efficiency

### Approach

Create a BinaryTree class and a Hashtable class: The BinaryTree class represents a binary tree and has a method called pre_order() that returns the pre-order traversal of the tree, i.e., a list of values obtained by visiting nodes in the order (root, left, right). The Hashtable class implements a basic hashtable data structure with methods like set, get, has, etc.

Define the tree_intersection function: The function takes two binary trees, tree_1 and tree_2, as inputs and aims to find the common values present in both trees.

Initialize an empty list common: This list will be used to store the common values found in both trees.

Get pre-order traversals of the two binary trees: The pre-order traversals of tree_1 and tree_2 are obtained by calling their respective pre_order() methods.

Create a Hashtable instance: We create a Hashtable instance called hashtable to store the values of tree_1.

Store values from tree_1 in the hashtable: We loop through the pre-order traversal of tree_1 and insert each value into the hashtable as a key, with the string representation of the value as the key (converted to a string using str(value)).

Check for common values in tree_2: We loop through the pre-order traversal of tree_2 and check if each value exists in the hashtable using the has method. If the value is found in the hashtable, it means it's a common value, and we append it to the common list.

Return the common list: After checking for common values in both trees, the function returns the common list containing the values that are present in both trees.

Create two binary trees (tree and tree2): The code initializes two binary trees with their respective nodes and values.

Call the tree_intersection function: The tree_intersection function is called with the two binary trees (tree and tree2) as arguments, and it prints the common values found in both trees.

### Efficiency
 the space complexity of a hashtable can be approximated as O(n) in the average and worst-case scenarios, where n is the number of key-value pairs stored, and the actual performance depends on the quality of the hash function and the handling of collisions.
The time complexity of the hash function is O(k), where k is the length of the key. Since the keys' length is usually small and constant, the hash function can be considered as O(1).



## 3. Solution
python3 tree_intersection.py
pytest test_tree_intersection