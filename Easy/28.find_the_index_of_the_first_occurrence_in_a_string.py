def find_first_occurrence(string, substring):
    return string.find(substring)

def find_first_occurrence_alt(string, substring):
    # Using the index() method
    try:
        index = string.index(substring)
        return index
    except ValueError:
        # Handle the case when the substring is not found
        return -1

# Example usage:
text = "Hello, World! This is a test."
substring = "Worldfff"

index = find_first_occurrence(text, substring)
print("Using find():", index)  # Output: 7

index_alt = find_first_occurrence_alt(text, substring)
print("Using index():", index_alt)  # Output: 7
