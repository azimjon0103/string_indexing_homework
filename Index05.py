def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    c=0
    if s[0]=='0':
        c+=1
    if s[0]=='1':
        c+=1
    if s[0]=='2':
        c+=1
    if s[0]=='3':
        c+=1
    if s[0]=='4':
        c+=1
    if s[0]=='5':
        c+=1
    if s[0]=='6':
        return 1
    if s[0]=='7':
        c+=1
    if s[0]=='8':
        c+=1
    if s[0]=='9':
        c+=1                       
    if s[0]=='0':
        c+=1
    if s[1]=='1':
        c+=1
    if s[1]=='2':
        c+=1
    if s[1]=='3':
        c+=1
    if s[1]=='4':
        c+=1
    if s[1]=='5':
        c+=1
    if s[1]=='6':
        c+=1
    if s[1]=='7':
        c+=1
    if s[1]=='8':
        c+=1
    if s[1]=='9':
        c+=1
    if s[2]=='0':
        c+=1
    if s[2]=='1':
        c+=1
    if s[2]=='2':
        c+=1
    if s[2]=='3':
        c+=1
    if s[2]=='4':
        c+=1
    if s[2]=='5':
        c+=1
    if s[2]=='6':
        c+=1
    if s[2]=='7':
        c+=1
    if s[2]=='8':
        c+=1
    if s[2]=='9':
        c+=1
    if s[3]=='0':
        c+=1
    if s[3]=='1':
        c+=1
    if s[3]==2:
        c+=1
    if s[3]=='3':
        c+=1
    if s[3]=='4':
        c+=1
    if s[3]=='5':
        c+=1
    if s[3]=='6':
        c+=1
    if s[3]=='7':
        c+=1
    if s[3]=='8':
        c+=1
    if s[3]=='9':
        c+=1
    if s[4]=='0':
        c+=1
    if s[4]=='1':
        c+=1
    if s[4]=='2':
        c+=1
    if s[4]=='3':
        c+=1
    if s[4]=='4':
        c+=1
    if s[4]=='5':
        c+=1
    if s[4]=='6':
        c+=1
    if s[4]=='7':
        c+=1
    if s[4]=='8':
        c+=1
    if s[4]=='9':
        c+=1    
    return c                 
print(main('3253z'))