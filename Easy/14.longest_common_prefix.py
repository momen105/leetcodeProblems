def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]  # Initialize prefix with the first string

    for string in strs[1:]:

        while string[: len(prefix)] != prefix:
            prefix = prefix[:-1]  # Remove the last character of the prefix
            if prefix == "":
                return ""  # If prefix becomes empty, there is no common prefix

    return prefix


result = longest_common_prefix(["flower", "flow", "flight"])
