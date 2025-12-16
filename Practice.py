def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = "madam"
print(f"{s} is a palindrome" if is_palindrome(s) else f"{s} is not a palindrome")
