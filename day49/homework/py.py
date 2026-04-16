def solution(number):
    

    
    if number < 0:
        return 0

    total = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


def find_it(seq):
    
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num

def spin_words(sentence):
    
    words = sentence.split()
    result = ""  

    for i, word in enumerate(words):
        
        if len(word) >= 5:
            word = word[::-1]

        
        result += word

        if i != len(words) - 1:
            result += " "

    return result


def array_diff(a, b):
    
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return result