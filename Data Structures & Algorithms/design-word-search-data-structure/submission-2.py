class WordNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = WordNode()
            current = current.children[c]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            c = word[i]
            if c == ".":
                return any(dfs(child, i+1) for child in node.children.values())
            if c in node.children:
                return dfs(node.children[c], i+1)
            return False   
        
        return dfs(self.root, 0)