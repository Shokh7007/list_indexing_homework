def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a=0
    isTrue=True
    while a<len(list1)-1:
        if list1[a]!=list1[a+1]:
            isTrue=False
        a+=1
    return isTrue
print(main(['asdf','asdf','asdf',123]))