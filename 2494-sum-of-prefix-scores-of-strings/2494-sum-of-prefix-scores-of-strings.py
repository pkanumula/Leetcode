class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0  # Count of how many words have this prefix

class Solution:
    def sumPrefixScores(self, words):
        root = TrieNode()
        
        # Function to insert a word into the Trie and update prefix counts
        def insert(word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.prefix_count += 1
        
        # Insert all words into the Trie
        for word in words:
            insert(word)
        
        # Function to calculate the score for a word based on its prefixes
        def calculate_score(word):
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.prefix_count
            return score
        
        # Calculate scores for all words
        return [calculate_score(word) for word in words]