__author__ = 'aleksander'

import ListHelper


def get_avg(table):
    if len(table) == 0:
        return None
    sum = 0
    for value in table:
        try:
            sum += value
        except Exception as e:
            print "Error in getting average of table: " + str(e)
    avg = sum/len(table)
    return avg


def get_avg_of_first_n(n, times):
    first_n = times[0:n]
    return get_avg(first_n)


def get_avg_of_last_n(n, times):
    last_n = times[-1*n:]
    return get_avg(last_n)


def get_lifetime_n_best(times, n):
    if len(times) < 1:
        return None
    best = []
    for i in range(0, n):
        lowest = ListHelper.get_lowest_from_list(times)
        best.append(lowest)
        times.remove(lowest)
    return best


def get_percentage_improvement_of_first_to_last_n(n, times):
    avg_of_first_n = get_avg_of_first_n(n, times)
    avg_of_last_n = get_avg_of_last_n(n, times)

    fractional_change = 1 - (avg_of_last_n / avg_of_first_n)

    percent_change = fractional_change * 100

    return percent_change


def get_best_avg_of_n(n, times):
    current_best = None
    best_solves = None

    for i in range(0, len(times)-n+1):
        subtable = times[i:i+n]
        this_avg = get_avg(subtable)
        if this_avg < current_best or current_best is None:
            current_best = this_avg
            best_solves = subtable

    return [current_best, best_solves]