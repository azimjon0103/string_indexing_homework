from re import A


def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=int(s[0])
    a+=int(s[1])
    a+=int(s[2])
    a+=int(s[3])
    a+=int(s[4])
    return a
print(main('12332'))    