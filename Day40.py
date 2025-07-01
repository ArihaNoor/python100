#Secret Code Language 

import random
import string

word = input("Enter word to encode: ")

def encode(word):
    if(len(word)>=3):
        encoded_word = word[1:] + word[0]
        random_first = getRandomCharacters()
        random_last = getRandomCharacters()
        encoded_word = random_first + word[1:] + word[0] + random_last
        return encoded_word
    else:
        return word[::-1]
    
def decode(word):
    if(len(word)>=3):
        decoded_word = word[3:-3]
        decoded_word1 = decoded_word[-1] 
        decoded_word2 = decoded_word1 + decoded_word[:-1] 
        return decoded_word2
    else:
        return word[::-1]
    
def getRandomCharacters():
    random_chars = random.choices(string.ascii_letters, k=3)
    return ''.join(random_chars)
                
x = encode(word)

print("Encoded Word is: ", x)

y = decode(x)

print("Decoded Word is: ", y)
