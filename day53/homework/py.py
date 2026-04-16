# return masked string
def maskify(cc):
    
    

    
        if len(cc) <= 4:
            return cc
        return "#" * (len(cc) - 4) + cc[-4:]



def warn_the_sheep(queue):


    index = 0
    for i in range(len(queue)):
        if queue[i] == "wolf":
            index = i
            break
    
    if index == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
    
    
    number = len(queue) - index - 1
    
    return "Oi! Sheep number " + str(number) + "! You are about to be eaten by a wolf!"


def number(lines):
    
    result = []
    

    for i in range(len(lines)):
        
        line = str(i + 1) + ": " + lines[i]
        result.append(line)
    
    return result



def distinct(seq):

    result = []
    
    
    for i in seq:
        
        if i not in result:
            result.append(i)
    
    return result



def human_years_cat_years_dog_years(human_years):
    
    catYears = 0
    dogYears = 0
    
    
    if human_years >= 1:
        catYears += 15
        dogYears += 15
    

    if human_years >= 2:
        catYears += 9
        dogYears += 9
    
    
    if human_years > 2:
        extra_years = human_years - 2
        catYears += extra_years * 4
        dogYears += extra_years * 5
    
    return [human_years, catYears, dogYears]



