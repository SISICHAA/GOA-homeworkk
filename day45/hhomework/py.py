def accum(st):
    result = []
    for i in range(len(st)):
        result.append(st[i].upper() + st[i].lower() * i)
    return "-".join(result)



def litres(time):
    return int(time * 0.5)


def to_jaden_case(string):
    result = ""
    words = string.split()
    
    for i in range(len(words)):
        result += words[i].capitalize()
        if i != len(words) - 1:
            result += " "
    
    return result


def lovefunc( flower1, flower2 ):
    
    return (flower1 + flower2) % 2 == 1


def maps(a):

    new = []
    
    for i in a:
        new.append( i * 2)
            
    return new


