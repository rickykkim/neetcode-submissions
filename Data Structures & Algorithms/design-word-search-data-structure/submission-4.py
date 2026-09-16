class WordNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = WordNode()
            curr = curr.children[letter]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        status = False

        def dfs(curr, idx):
            nonlocal status
            if status == True:
                return True
            if idx == len(word):
                status = curr.endOfWord
                return curr.endOfWord
            
            if word[idx] == ".":
                for _, node in curr.children.items():
                    dfs(node, idx + 1)
            else:
                if word[idx] not in curr.children:
                    return False
                curr = curr.children[word[idx]]
                dfs(curr, idx + 1)

        dfs(self.root, 0)
        return status

        # . = run for loop across all children
        # a = only that particular word in children