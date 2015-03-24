__author__ = 'aleksander'

import ListHelper as Lh
import copy
import math


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


def get_avg_with_elimination(times):
    best_solve = None
    worst_solve = None

    times2 = copy.deepcopy(times)

    for i in range(0, len(times2)-1):
        if best_solve is None or best_solve > times2[i]:
            best_solve = times2[i]
        if worst_solve is None or worst_solve < times2[i]:
            worst_solve = times2[i]

    times2.remove(best_solve)
    times2.remove(worst_solve)

    avg_of_remaining = get_avg(times2)

    return avg_of_remaining


def get_avg_of_first_n(n, times):
    first_n = times[0:n]
    return get_avg_with_elimination(first_n)


def get_avg_of_last_n(n, times):
    last_n = times[-1*n:]
    return get_avg_with_elimination(last_n)


def get_lifetime_n_best(times, n):
    if len(times) < 1:
        return None
    best = []
    for i in range(0, n):
        lowest = Lh.get_lowest_from_list(times)
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
        this_avg = get_avg_with_elimination(subtable)
        if this_avg < current_best or current_best is None:
            current_best = this_avg
            best_solves = subtable

    return [current_best, best_solves]


def get_current_sub_x(times):
    ao100 = get_avg_of_last_n(100, times)
    rounded_up = int(math.ceil(ao100))
    subx = rounded_up + 1
    return subx