def anagrams(str1, str2):
    # convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

string1 = "Bare"
string2 = "Bear"

if anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}'  not anagrams.")
