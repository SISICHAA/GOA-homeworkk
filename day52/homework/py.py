def solution(number):
    

    
    if number < 0:
        return 0

    total = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total



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
            
                
def high_and_low(numbers):

    number_list = numbers.split()
    
    
    int_list = []
    for i in number_list:
        int_list.append(int(i))
    
    highest = int_list[0]
    for i in int_list:
        if i > highest:
            highest = i
    
    lowest = int_list[0]
    for i in int_list:
        if i < lowest:
            lowest = i
    
    result = str(highest) + " " + str(lowest)
    return result



def find_short(s):

    words = s.split()
    
    shortest_len = len(words[0])
    

    for i in words:
        if len(i) < shortest_len:
            shortest_len = len(i)
    

    return shortest_len



def remove(s):
    
    
    end = 0
    
    for i in reversed(s):
        if i == "!":
            end += 1
        else:
            break
    
    
    clean = ""
    for i in s:
        if i != "!":
            clean += i
    

    result = clean + "!" * end
    
    return result



def points(games):

    total_points = 0
    
    
    for i in games:
        score = i.split(":")
        x = int(score[0])  
        y = int(score[1])  
        
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
        else:
            total_points += 0
    
    return total_points