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

def lower_text(text):
    return text.lower()

def find_palindrome(text, index):
    k = index + 1
    forwards = True
    has_palindrome = True
    while index > -1 and k < len(text) and has_palindrome:
        has_palindrome = False
        incr = [(-1,1), (0,1), (-1, 0)]
        for a,b in incr:
            if index+a < 0 or k+b > len(text):
                continue
            if is_palindrome(text[index+a:k+b]):
                has_palindrome = True
                index = index + a
                k = k + b
                break
    return (index, k)

    
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = lower_text(text)
    start = end = 0
    for index, sub in enumerate(text):
        if index > start and index < end:
            continue
        (j, k) = find_palindrome(text, index)
        if k - j > end - start: 
            start = j
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
    