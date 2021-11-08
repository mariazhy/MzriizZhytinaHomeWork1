def remove_duplicates(s: str):
    """
    Task 1: This method removes duplicates in a string.
    :param s: input string
    """
    my_list = s.split()
    for i in my_list:
        if my_list.count(i) > 1:
            my_list.remove(i)
    output_s = ' '.join(my_list)
    return output_s
