class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Memoization dictionary to store already computed results
        memo = {}
        
        def compute(expression):
            # If we already computed this expression, return the stored result
            if expression in memo:
                return memo[expression]
            
            result = []
            # Traverse through the expression to find an operator
            for i, char in enumerate(expression):
                if char in "+-*":  # If we find an operator
                    # Recursively solve left and right parts
                    left_results = compute(expression[:i])
                    right_results = compute(expression[i+1:])
                    
                    # Combine results based on the current operator
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                result.append(left + right)
                            elif char == '-':
                                result.append(left - right)
                            elif char == '*':
                                result.append(left * right)
            
            # If no operator is found, it means the expression is just a number
            if not result:
                result.append(int(expression))
            
            # Store the result in memoization dictionary
            memo[expression] = result
            return result
        
        # Call the helper function to compute the result
        return compute(expression)
