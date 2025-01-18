def is_palindrome(string):
    # Removing spaces and converting to lowercase
    cleaned_string = ''.join(string.split()).lower()
    
    # Checking if the string is equal to its reverse
    if cleaned_string == cleaned_string[::-1]:
        return True
    return False


word = input("Enter a string to check for palindrome: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
