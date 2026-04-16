def get_middle(s):
    
    leng = len(s)
    middle = leng // 2
    
    if leng % 2 == 0:
        return s[middle - 1] + s[middle] 
    else:
        return s[middle]
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    if len(test) != len(original):
        return False
    
    for i in test:
        if test.count(i) != original.count(i):
            return False
    
    return True

def maskify(cc):
    
    

    
        if len(cc) <= 4:
            return cc
        return "#" * (len(cc) - 4) + cc[-4:]



def check_exam(arr1, arr2):
    score = 0

    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0
        elif arr1[i] == arr2[i]:
            score += 4
        else:
            score -= 1

    if score < 0:
        score = 0

    return score
            

def create_phone_number(n):
    
    return "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + \
           str(n[3]) + str(n[4]) + str(n[5]) + "-" + \
           str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
           