def get_years_list(born: int):
    """
        >>> get_years_list(2000)
        [2000, 2001, 2002, 2003, 2004]
        
        >>> get_years_list(2020)
        [2020, 2021, 2022, 2023, 2024]

        >>> get_years_list('invalid arg')
        Traceback (most recent call last):
        ...
        TypeError: must be str, not int
    """
    return list(range(born, born + 5))

def get_three_years_old(years_list:list):
    """
        >>> get_three_years_old(get_years_list(1900))
        1903
        
        >>> get_three_years_old('invalid args')
        'a'
        
        >>> get_three_years_old(None)
        Traceback (most recent call last):
        ...
        TypeError: 'NoneType' object is not subscriptable

        >>> get_three_years_old(1)
        Traceback (most recent call last):
        ...
        TypeError: 'int' object is not subscriptable
    """
    return years_list[3]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()