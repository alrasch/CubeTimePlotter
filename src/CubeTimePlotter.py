from reportlab.graphics.samples.scatter import Scatter

import ListHelper as Lh
import FileHandler as Fh
import mathematics.MathHelper as Mh
import plotly.plotly as py
import time
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
        avg = Mh.get_avg(subtable)
        averages.append(avg)

    x = []
    for i in range(1, len(averages)+1):
        x.append(i)

    trace2 = Scatter(x=x, y=averages)

    data = Data([trace1, trace2])
    py.plot(data, filename='basic-line')


def writeout(times):

    print "---"

    print "Number of solves:                " + str(Lh.get_number_of_solves(times))

    print "---"

    print "Lifetime average:                " + str(Lh.get_lifetime_avg(times))
    print "Lifetime best:                   " + str(Lh.get_lifetime_best(times))
    print "Lifetime best 5:                 " + ', '.join(str(i) for i in Mh.get_lifetime_n_best(times, 5))

    print "---"

    print "List of last 5:                  " + str(Lh.get_list_of_last_n(5, times))
    print "Average of last 5:               " + str(Mh.get_avg_of_last_n(5, times))

    print "---"

    print "Average of last 10:              " + str(Mh.get_avg_of_last_n(10, times))
    print "Average of last 12:              " + str(Mh.get_avg_of_last_n(12, times))
    print "Average of last 100:             " + str(Mh.get_avg_of_last_n(100, times))

    print "---"

    print "List of first 5:                 " + str(Lh.get_list_of_first_n(5, times))
    print "Average of first 5:              " + str(Mh.get_avg_of_first_n(5, times))

    print "---"

    print "Average of first 10:             " + str(Mh.get_avg_of_first_n(10, times))
    print "Average of first 12:             " + str(Mh.get_avg_of_first_n(12, times))
    print "Average of first 100:            " + str(Mh.get_avg_of_first_n(100, times))

    print "---"

    print "Percentage change in avg of 5:   " + \
          str("%.2f" % Mh.get_percentage_improvement_of_first_to_last_n(5, times))
    print "Percentage change in avg of 10:  " + \
          str("%.2f" % Mh.get_percentage_improvement_of_first_to_last_n(10, times))
    print "Percentage change in avg of 12:  " + \
          str("%.2f" % Mh.get_percentage_improvement_of_first_to_last_n(12, times))

    print "---"

    best5 = Mh.get_best_avg_of_n(5, times)
    print "Best Ao5 so far:                 " + \
          str(best5[0]) + " with the solves: " + \
          ', ' . join(str(i) for i in best5[1])
    print "Best Ao12 so far:                " + str(Mh.get_best_avg_of_n(12, times)[0])
    print "Best Ao100 so far:               " + str(Mh.get_best_avg_of_n(100, times)[0])


class CubeTimePlotter:

    def __init__(self):
        self.times = Fh.get_times()

    def init(self):
        start = time.time()
        plot(self.times)
        end = time.time()
        plot_time = end-start
        print "Plotting time: " + str("%.5f" % plot_time)

        start = time.time()
        writeout(self.times)
        end = time.time()
        writeout_time = end-start
        print "Writeout time: " + str("%.5f" % writeout_time)
