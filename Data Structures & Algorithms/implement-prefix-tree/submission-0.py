class PrefixTree:

    def __init__(self):
        self.tree = []

    def insert(self, word: str) -> None:
        self.tree.append(word)

    def search(self, word: str) -> bool:
        return word in self.tree

    def startsWith(self, prefix: str) -> bool:
        for word in self.tree:
            if word[:len(prefix)] == prefix:
                return True
        return False