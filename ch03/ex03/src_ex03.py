def get_years_list(born: int) -> list:
    """
        >>> get_years_list(2000)
        [2000, 2001, 2002, 2003, 2004]

        >>> get_years_list(2020)
        [2020, 2021, 2022, 2023, 2024]
    """
    return list(range(born, born + 5))

def get_latest_years_old(yeas_list:list) -> int:
    """
        >>> get_latest_years_old(get_years_list(1900))
        1904

        >>> get_latest_years_old('invalid args')
        's'
        
        >>> get_latest_years_old(None)
        Traceback (most recent call last):
        ...
        TypeError: 'NoneType' object is not subscriptable

        >>> get_latest_years_old(1)
        Traceback (most recent call last):
        ...
        TypeError: 'int' object is not subscriptable
    """
    return yeas_list[-1]