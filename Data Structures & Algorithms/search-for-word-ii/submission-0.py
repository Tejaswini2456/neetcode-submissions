class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):

        # -------------------------
        # 1. Build the Trie
        # -------------------------
        root = TrieNode()

        for word in words:
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            # Store the complete word at the final node
            curr.word = word

        # -------------------------
        # 2. DFS on the board
        # -------------------------
        result = []

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):

            # Current character
            char = board[r][c]

            # If this character doesn't continue
            # any word in the Trie, stop
            if char not in node.children:
                return

            # Move to the corresponding Trie node
            node = node.children[char]

            # We found a complete word
            if node.word:
                result.append(node.word)

                # Avoid adding the same word again
                node.word = None

            # Mark current board cell as visited
            board[r][c] = "#"

            # Four possible directions
            directions = [
                (1, 0),    # down
                (-1, 0),   # up
                (0, 1),    # right
                (0, -1)    # left
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check boundaries and whether cell is already visited
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] != "#"
                ):
                    dfs(nr, nc, node)

            # Restore the original character
            board[r][c] = char

        # -------------------------
        # 3. Start DFS from every cell
        # -------------------------
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
        