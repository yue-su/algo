def longestPath(root):
    def dfs(node, parent_val, length):
        if not node:
            return

        # If the current node continues the sequence
        if node.value == parent_val + 1:
            length += 1
        else:
            length = 1

        # Update max_length
        nonlocal max_length
        max_length = max(max_length, length)

        # Recurse on both children
        dfs(node.left, node.value, length)
        dfs(node.right, node.value, length)

    max_length = 0
    dfs(root, float('-inf'), 0)
    return max_length
