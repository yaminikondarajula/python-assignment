def is_palindrome(s: str) -> bool:
    # Clean the string: remove non-alphanumeric and make lowercase
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

# Main program
word = input("Enter a string: ")

if is_palindrome(word):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
