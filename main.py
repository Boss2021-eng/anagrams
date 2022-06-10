# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    
    # convert the two words to lowercase
    str1 = word1.lower()
    str2 = word2.lower()
    
    # check if the length of the two words are the same
    if len(str1) == len(str2):
            
        # sort the strings
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        
        # compare the sorted strings and return the same 
        if sorted_str1 == sorted_str2:
            print (True)
        else:
            print(False)
    else:
        return False
    
find_anagrams('care','race')
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if list(word1) == list(word2):
        print(True)
    else:
        print (False)

find_anagrams("spar","rasp")

print(list('spar')) == print(list('rasp'))
print((list('spar')) == (list('rasp')))

find_anagrams('race', 'care')
find_anagrams('meat', 'team')
find_anagrams('meal', 'team')