__author__ = 'aleksander'


class Helper:

    def __init__(self):
        pass

    def get_avg(self, table):
        if len(table) == 0:
            return None
        sum = 0
        for value in table:
            try:
                sum += value
            except Exception as e:
                print e.__str__()
        avg = sum/len(table)
        return avg

    def avg_of_last_n(self, n, times):
        last_n = times[-1*n:]

        sum = 0
        for time in last_n:
            sum += time

        avg = sum / len(last_n)

        return avg

    def lifetime_avg(self, times):
        if len(times) < 1:
            return None
        sum = 0
        for time in times:
            try:
                sum += time
            except Exception as e:
                print e.__str__()

        avg = sum/len(times)
        return avg