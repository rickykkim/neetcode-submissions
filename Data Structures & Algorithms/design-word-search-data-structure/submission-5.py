class WordNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = WordNode()
            curr = curr.children[w]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, idx, state):
            if word[idx] == ".":
                for _, nextNode in node.children.items():
                    if idx == len(word) - 1:
                        return nextNode.endOfWord
                    state = state or dfs(nextNode, idx+1, state)
            elif word[idx] in node.children:
                nextNode = node.children[word[idx]]
                if idx == len(word) - 1:
                    return nextNode.endOfWord
                state = state or dfs(nextNode, idx+1, state)
            else:
                return False

            return state
        
        return dfs(self.root, 0, False)

        # . = run for loop across all children
        # a = only that particular word in children