from collections import Counter
import time

start = time.time()

def check_anagram(string1, string2):
    # Comparing len of string to see if they are of same length or not
    if len(string1) != len(string2):
        return False
    
    # Creating dict of frequency of every charachter in string1
    fq = {}
    for s in string1:
        if s in fq:
            fq[s] +=1
        else:
            fq[s] = 1
    
    # Another way of getting frequency or occurence of char in string
    # fq = Counter(string1)

    # Iterating in second string to check if they are in frquency 
    for s in string2:
        if s not in fq or fq[s] == 0:
            return False # If s is not in fq then string1 is not a anagram of string2
        else:
            fq[s] -=1 # Reducing fq of the char by 1 if present

    return True

anagram_data = [
    ['listen', 'silent'],
    ['hello', 'world'],
    ['evil', 'vile'],
    ['abc', 'def'],
    ['cinema', 'iceman'],
    ['army', 'mary'],
    ['debit card', 'bad credit'],
    ['astronomer', 'moon starer'],
    ['the Morse code', 'Here come dots'],
    ['Dormitory', 'Dirty room'],
    ['slot machines', 'cash lost in me'],
    ['Astronomers', 'Moon starer'],
    ['mother in law', 'woman Hitler'],
    ['funeral', 'real fun'],
    ['The Morse Code!', 'Here come dots'],
    ['Vacation times', "I'm not as active"],
    ['Eleven plus two', 'Twelve plus one'],
    ['Schoolmaster', 'The classroom'],
    ['Listen', 'Silent'],
    ['The eyes', 'They see']
]

for i in anagram_data:

    if check_anagram(i[0], i[1]):
        i.append(1)
    else:
        i.append(0)

print(anagram_data)

end = time.time()
print(f"Time took {end  - start}")