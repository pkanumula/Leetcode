class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove underscores and check if the sequence of 'L' and 'R' matches
        if start.replace('_', '') != target.replace('_', ''):
            return False

        # Iterate through both strings to ensure valid movement for 'L' and 'R'
        start_pointer, target_pointer = 0, 0
        n = len(start)

        while start_pointer < n and target_pointer < n:
            # Skip underscores in both strings
            while start_pointer < n and start[start_pointer] == '_':
                start_pointer += 1
            while target_pointer < n and target[target_pointer] == '_':
                target_pointer += 1

            # If both pointers are at the end, the strings are transformable
            if start_pointer == n and target_pointer == n:
                return True

            # If only one pointer is at the end, transformation is not possible
            if start_pointer == n or target_pointer == n:
                return False

            # Check if the characters match and ensure valid movement
            if start[start_pointer] != target[target_pointer]:
                return False

            if start[start_pointer] == 'L' and start_pointer < target_pointer:
                return False  # 'L' can only move left

            if start[start_pointer] == 'R' and start_pointer > target_pointer:
                return False  # 'R' can only move right

            # Move both pointers to the next position
            start_pointer += 1
            target_pointer += 1

        return True
