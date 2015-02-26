__author__ = 'aleksander'


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

    sum = 0
    for time in first_n:
        sum += time
    avg = sum / len(first_n)
    return avg


def get_avg_of_last_n(n, times):
    last_n = times[-1*n:]

    sum = 0
    for time in last_n:
        sum += time

    avg = sum / len(last_n)

    return avg


def get_list_of_first_n(n, times):
    first_n = times[0:n]

    return ', ' . join(str(time) for time in first_n)


def get_list_of_last_n(n, times):
    last_n = times[-1 * n:]

    return ', ' . join(str(time) for time in last_n)


def get_lifetime_avg(times):
    if len(times) < 1:
        return None
    sum = 0
    for time in times:
        try:
            sum += time
        except Exception as e:
            print "Error in getting lifetime average: " + e.message

    avg = sum/len(times)
    return avg


def get_lowest_from_list(list):
    lowest = None
    for value in list:
        if lowest == None or lowest > value:
            lowest = value
    return lowest


def get_lifetime_n_best(times, n):
    if len(times) < 1:
        return None
    best = []
    for i in range(0, n):
        lowest = get_lowest_from_list(times)
        best.append(lowest)
        times.remove(lowest)
    return best


def get_percentage_improvement_of_first_to_last_n(n, times):
    avg_of_first_n = get_avg_of_first_n(n, times)
    avg_of_last_n = get_avg_of_last_n(n, times)

    fractional_change = 1 - (avg_of_last_n / avg_of_first_n)

    percent_change = fractional_change * 100

    return percent_change


def get_number_of_solves(times):
    return len(times)