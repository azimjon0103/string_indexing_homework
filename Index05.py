def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0].isdigit():
        if s[1].isdigit():
            if s[2].isdigit():
                if s[3].isdigit():
                   if s[4].isdigit(): 
                    return len(s[4])+len(s[3])+ len(s[2])+ len(s[1])+len(s[0]) 
    if s[0].isdigit():
        if s[1].isdigit():
            if s[2].isdigit():
                if s[3].isdigit():
                   if s[4].isalpha(): 
                    return len(s[3])+ len(s[2])+ len(s[1])+len(s[0])         
    if s[0].isdigit():
        if s[1].isdigit():
            if s[2].isdigit():
                if s[3].isalpha():
                   if s[4].isdigit(): 
                    return len(s[4])+ len(s[2])+ len(s[1])+len(s[0]) 
    if s[0].isdigit():
        if s[1].isdigit():
            if s[2].isalpha():
                if s[3].isdigit():
                   if s[4].isdigit(): 
                    return len(s[4])+len(s[3])+ len(s[1])+len(s[0])       
    if s[0].isdigit():
        if s[1].isalpha():
            if s[2].isdigit():
                if s[3].isdigit():
                   if s[4].isdigit(): 
                    return len(s[4])+len(s[3])+ len(s[2])+len(s[0])   
    if s[0].isalpha():
        if s[1].isdigit():
            if s[2].isdigit():
                if s[3].isdigit():
                   if s[4].isdigit(): 
                    return len(s[4])+len(s[3])+ len(s[2])+ len(s[1])                                        
    if s[0].isalpha():
        if s[1].isalpha():
            if s[2].isalpha():
                if s[3].isalpha():
                   if s[4].isalpha(): 
                    return False      
print(main('dfgsa'))