def is_valid_parentheses(s):
    stack = []
    opening_brackets = {"(", "[", "{"}
    closing_brackets = {")", "]", "}"}
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_pairs[stack.pop()] != char:
                return False
    return not stack


result = is_valid_parentheses("([]{})")
print(result)
