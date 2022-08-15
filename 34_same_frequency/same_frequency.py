def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count1 = {}
    for num in num1:
        count1[num] = count1.get(num, 0) +1
    return count1

    count2 = {}
    for num in num2:
        count2[num] = count1.get(num, 0) +1
    return count2

    return count1 == count2
