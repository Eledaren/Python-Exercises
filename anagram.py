# Enter by input two strings and check if they are anagrams
# If the second string is an anagram of the first one, print "Anagrams"
# If not, print "Not anagrams"

def Anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    
    if sorted(string1) == sorted(string2):
        print("Anagrams")
    else:
        print("Not anagrams")

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print(string1, string2)

Anagrams(string1, string2)