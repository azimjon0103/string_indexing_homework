def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit():
        return int(s)
    if s.isalpha():
        return -1    
print(main('j'))    