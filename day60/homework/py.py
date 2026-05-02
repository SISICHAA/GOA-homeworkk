def delete_nth(order,max_e):
    
    result = []
    for num in order:
        if result.count(num) < max_e:
            result.append(num)
    return result



def digital_root(n):
    while n > 9: 
        total = 0
        
        for digit in str(n):
            total += int(digit)
        
        n = total  
    
    return n


def clean_string(s):
    stack = []

    for i in s:
        if i == '#':
            if stack:
                stack.pop()  
        else:
            stack.append(i)  

    return ''.join(stack)