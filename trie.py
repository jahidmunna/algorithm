from typing import Dict

class TrieNode:
    def __init__(self) -> None:
        """
        TrieNode class represents a node in the Trie data structure.
        Each node has a dictionary to store child nodes and a flag indicating if it forms a complete word.
        """
        self.childs: Dict[str, TrieNode] = dict()
        self.is_completed_word: bool = False

class Trie:
    def __init__(self) -> None:
        """
        Trie class represents a Trie data structure.
        It is used for efficient storage and retrieval of a dynamic set or associative array of strings.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        Parameters:
            - word (str): The word to be inserted into the Trie.

        Time Complexity: O(m), where m is the length of the word.
        Space Complexity: O(m), where m is the length of the word.
        """
        node = self.root
        for char in word:
            if char not in node.childs:
                node.childs[char] = TrieNode()
            node = node.childs[char]

        node.is_completed_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.

        Parameters:
            - word (str): The word to be searched in the Trie.

        Return:
            - bool: True if the word is found, False otherwise.

        Time Complexity: O(m), where m is the length of the word.
        Space Complexity: O(1)
        """
        node = self.root
        for char in word:
            if char not in node.childs:
                return False
            node = node.childs[char]

        return node.is_completed_word



if __name__ == '__main__':
    # Examples
    words = ['cat', 'car', 'bat', 'batman']
    
    # Insert into Trie
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    # Search
    print(trie.search('cat')) # True
    print(trie.search('car')) # True
    print(trie.search('ba')) # False
    print(trie.search('bat')) # True
    print(trie.search('batmans')) # False
    print(trie.search('batmans')) # False
    
