class Solution:
    def isValid(self, s: str) -> bool:
        queue = ""
        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                queue += letter
            else:
                try:
                    if queue[-1] == "(" and letter == ")":
                        queue = queue[:len(queue)-1]
                    elif queue[-1] == "[" and letter == "]":
                        queue = queue[:len(queue)-1]
                    elif queue[-1] == "{" and letter == "}":
                        queue = queue[:len(queue)-1]
                    else:
                        return False
                except:
                    return False
        
        return len(queue) == 0