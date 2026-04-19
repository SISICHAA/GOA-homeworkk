def create_phone_number(n):
    
    return "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + \
           str(n[3]) + str(n[4]) + str(n[5]) + "-" + \
           str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
   



def to_float_array(arr): 
    
    result = []

    for i in arr:
        result.append(float(i))

    return result


def capitalize(s):
    even = ""
    
    odd = ""

    for i in range(len(s)):
        
        if i % 2 == 0:
            even += s[i].upper()
            odd += s[i]
        else:
            even += s[i]
            odd += s[i].upper()

    return [even, odd]



def adjacent_element_product(array):
    
    max_product = array[0] * array[1]

    for i in range(len(array) - 1):
        product = array[i] * array[i + 1]

        if product > max_product:
            max_product = product

    return max_product