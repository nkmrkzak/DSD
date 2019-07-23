def get_years_list(born):
    """
        >>> get_years_list(2000)
        [2000, 2001, 2002, 2003, 2004]

        >>> get_years_list(2020)
        [2020, 2021, 2022, 2023, 2024]

        >>> get_years_list('invalid arg')
        Traceback (most recent call last):
        ...
        TypeError: must be str, not int

        >>> get_years_list(None)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
    """
    return list(range(born, born + 5))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()