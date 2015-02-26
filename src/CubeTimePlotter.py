from reportlab.graphics.samples.scatter import Scatter

import Helper
import FileHandler


__author__ = 'aleksander'
import plotly.plotly as py
from plotly.graph_objs import *


def plot(times):

    #Make a trace for the times
    x = []
    for i in range(1, len(times) + 1):
        x.append(i)
    trace1 = Scatter(x=x, y=times)

    #Make a trace for the average of last 5
    averages = [0, 0, 0, 0]
    for i in range(4, len(times)):
        subtable = []
        for j in range(i-4, i+1):
            subtable.append(times[j])
        avg = Helper.get_avg(subtable)
        averages.append(avg)

    x = []
    for i in range(1, len(averages)+1):
        x.append(i)

    trace2 = Scatter(x=x, y=averages)

    data = Data([trace1, trace2])
    #py.plot(data, filename='basic-line')


class CubeTimePlotter:

    def __init__(self):
        self.times = FileHandler.get_times()

    def init(self):
        plot(self.times)

        print "---"

        print "Number of solves:        " + str(Helper.get_number_of_solves(self.times))

        print "---"

        print "Lifetime average:        " + str(Helper.get_lifetime_avg(self.times))
        print "Lifetime best:           " + str(Helper.get_lifetime_best(self.times))
        print "Lifetime best 5:         " + ', '.join(str(i) for i in Helper.get_lifetime_n_best(self.times, 5))

        print "---"

        print "List of last 5:          " + str(Helper.get_list_of_last_n(5, self.times))
        print "Average of last 5:       " + str(Helper.get_avg_of_last_n(5, self.times))

        print "---"

        print "Average of last 10:      " + str(Helper.get_avg_of_last_n(10, self.times))
        print "Average of last 12:      " + str(Helper.get_avg_of_last_n(12, self.times))
        print "Average of last 100:     " + str(Helper.get_avg_of_last_n(100, self.times))

        print "---"

        print "List of first 5:         " + str(Helper.get_list_of_first_n(5, self.times))
        print "Average of first 5:      " + str(Helper.get_avg_of_first_n(5, self.times))

        print "---"

        print "Average of first 10:     " + str(Helper.get_avg_of_first_n(10, self.times))
        print "Average of first 12:     " + str(Helper.get_avg_of_first_n(12, self.times))
        print "Average of first 100:    " + str(Helper.get_avg_of_first_n(100, self.times))

        print "---"

        print "Percentage change in avg of 5:   " + str(Helper.get_percentage_improvement_of_first_to_last_n(5, self.times))
