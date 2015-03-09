__author__ = 'aleksander'


import mathematics.MathHelper as Mh


def get_lifetime_best(times):
    best = None
    for time in times:
        if best is None:
            best = time
        elif time < best:
            best = time
    if best is not None:
        return best
    return False


def get_list_of_first_n(n, times):
    first_n = times[0:n]
    return ', ' . join(str(time) for time in first_n)


def get_list_of_last_n(n, times):
    last_n = times[-1 * n:]
    return ', ' . join(str(time) for time in last_n)


def get_lifetime_avg(times):
    return Mh.get_avg(times)


def get_lowest_from_list(values):
    lowest = None
    for value in values:
        if lowest is None or lowest > value:
            lowest = value
    return lowest


def get_number_of_solves(times):
    return len(times)