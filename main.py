def csIsomorphicStrings(a, b):
    # first find the length of each string
    s1 = len(a)
    s2 = len(b)
    
    # length of both strings needs to be the same in order to be True
    if s1 != s2:
        return False
    

    return True