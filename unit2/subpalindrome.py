# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!
    
def is_palindrome(text):
    return text == text[::-1]
    
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = text.lower()
    start = 0
    end = 0
    reverse_text = text[::-1]
    for index, sub in enumerate(text):
        if index > start and index < end:
            continue
        k = index
        current_sub = ""
        while current_sub in reverse_text and k < len(reverse_text): 
            current_sub = current_sub + text[k]
            k = k + 1
            if is_palindrome(text[index:k]) and len(text[index:k]) > len(text[start:end]):
                start = index 
                end = k
    return (start,end)        

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'