def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=0
    while a<=len(list1) and list1[a]==1:
        return list1[a]
        a=a+1
print(main([1,0,0,1,0]))