def is_mapping_possible(arr, s):
    def encode_string(string, mapping):
        return int(''.join(str(mapping.get(char, '')) for char in string))

    def backtrack(index, mapping, used_digits):
        if index == len(arr):
            # Check if the sum of encoded values is equal to the encoded value of the target string
            return encode_string(arr[0], mapping) + encode_string(arr[1], mapping) == encode_string(s, mapping)

        current_word = arr[index]
        for char in current_word:
            if char not in mapping:
                for digit in range(10):
                    if digit not in used_digits:
                        mapping[char] = digit
                        used_digits.add(digit)
                        if backtrack(index + 1, mapping, used_digits):
                            return True
                        mapping.pop(char)
                        used_digits.remove(digit)
        return False

    # Check if mapping is possible starting from the first word
    return backtrack(0, {}, set())

# Example usage
if __name__ == "__main__":
    arr = ["SEND", "MORE"]
    s = "MONEY"

    result = is_mapping_possible(arr, s)

    # Output the result
    if result:
        print("Yes, mapping is possible.")
    else:
        print("No, mapping is not possible.")
