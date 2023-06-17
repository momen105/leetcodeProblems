def repeatedSubstringPattern(s):
    n = len(s)
    # Check for potential divisors
    for i in range(1, n // 2 + 1):

        if n % i == 0:
            # Construct potential substring
            substring = s[:i]

            # Check if substring repeats to form s
            if substring * (n // i) == s:
                return True

    return False


print(repeatedSubstringPattern("abcabc"))
