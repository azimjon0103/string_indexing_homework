def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0]=='*' :
        return 0
    if s[1]=='*' :
        return 1
    if s[2]=='*' :
        return 2
    if s[3]=='*' :
        return 3
    if s[4]=='*' :
        return 4               
    elif s[0]!='*':
        return False 
    elif s[1]!='*':
        return False 
    elif s[2]!='*':
        return False 
    elif s[3]!='*':
        return False 
    elif s[4]!='*':
        return False                   
print(main('42111'))    