def hours():
    print(coretime(9, 5))


def coretime(start, end, work_threshold=15):
    """
    Parameters
    ----------
    start : int
        Working start time
    end : int
        Working end time
    Returns
    -------
    core_time_string : string
        coretime text

    Raises
    ---------
    ValueError
        if start or end is under 1 or over 24
    OverWorkedException
        労基に相談してください
    """

    worktime = end - start
    if start < 1 or start > 24 or end < 1 or end > 24:
        raise ValueError('please set parameter from 1 to 24')

    while worktime < 0:
        worktime += 12
    if worktime > work_threshold:
        from workException import OverworkedException
        raise OverworkedException('労基に相談してください')
    return 'Open '+str(start)+'-'+str(end)+' daily'
