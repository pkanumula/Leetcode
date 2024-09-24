class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_number = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, number):
        node = self.root
        for digit in str(number):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.end_of_number = True
    
    def longest_common_prefix(self, number):
        node = self.root
        common_length = 0
        for digit in str(number):
            if digit in node.children:
                node = node.children[digit]
                common_length += 1
            else:
                break
        return common_length

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        trie = Trie()
        
        # Insert all elements of arr1 into the Trie
        for num in arr1:
            trie.insert(num)
        
        # Check the longest common prefix with elements of arr2
        max_len = 0
        for num in arr2:
            max_len = max(max_len, trie.longest_common_prefix(num))
        
        return max_len
