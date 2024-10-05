# Define a function that takes a string as input and returns a boolean value
def is_palindrome(s):
    # remove any non alphanumeric character from the string and convert to lowercase
    s ="".join(c for c in s if c.isalnum()).lower()
    #compare the string with its reverse
    return s == s[::-1]
input_string="mum"
print(is_palindrome(input_string))
