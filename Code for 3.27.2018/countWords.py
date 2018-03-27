##Count words in 4 novels
##Author: nmessa

def count_words(filename):
    #Add code here
    
    return count

def count_long_words(filename):
    #Add code here

    
    return count

def cleanup(word):
    cleaned = ""
    for ch in word:
        if ch.isalpha():
            cleaned += ch
        else:
            pass
    cleaned = cleaned.capitalize()
    return cleaned

def sortWords(filename):
    #Add code here
    
    
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
counters = []
counters2 = []

for filename in filenames:
    counters.append(count_words(filename))
    counters2.append(count_long_words(filename))

print ("Words in each novel")
print ("Alice in Wonderland", counters[0])
print ("Siddhartha", counters[1])
print ("Moby Dick", counters[2])
print ("Little Women", counters[3])
print()
print ("Long words in each novel")
print ("Alice in Wonderland", counters2[0])
print ("Siddhartha", counters2[1])
print ("Moby Dick", counters2[2])
print ("Little Women", counters2[3])

sortWords('alice.txt')
