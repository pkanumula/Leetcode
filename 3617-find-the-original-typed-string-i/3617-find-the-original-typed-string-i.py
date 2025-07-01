class Solution:
    def possibleStringCount(self, word: str) -> int:
        from itertools import groupby

        # Step 1: Group the word by consecutive characters
        groups = [(char, len(list(group))) for char, group in groupby(word)]

        results = set()
        results.add(word)  # Case with no mistake

        # Step 2: Try reducing each group with count > 1
        for i, (char, count) in enumerate(groups):
            if count > 1:
                for reduced_count in range(1, count):
                    # Build the new word with reduced count in this group
                    new_word = ''
                    for j, (c, cnt) in enumerate(groups):
                        if j == i:
                            new_word += c * reduced_count
                        else:
                            new_word += c * cnt
                    results.add(new_word)

        return len(results)
