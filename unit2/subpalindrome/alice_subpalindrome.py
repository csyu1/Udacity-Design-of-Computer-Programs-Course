import re
from subpalindrome import longest_subpalindrome_slice

def pre_process_file(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return ' '.join(text.split())
    
def words_only(text):
    words = re.findall(r'[a-zA-Z]+', text)
    return ' '.join(words)
    
text = pre_process_file('alice_in_wonderland.txt')
words = words_only(text)
palindrome_index = longest_subpalindrome_slice(words)
print words[palindrome_index[0]:palindrome_index[1]]