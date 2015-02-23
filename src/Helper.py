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


def get_avg_of_last_n(n, times):
    last_n = times[-1*n:]

    sum = 0
    for time in last_n:
        sum += time

    avg = sum / len(last_n)

    return avg


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