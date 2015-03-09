from reportlab.graphics.samples.scatter import Scatter
from plotly.graph_objs import *
from os import linesep as newline

import ListHelper as Lh
import FileHandler as Fh
import mathematics.MathHelper as Mh
import plotly.plotly as py

import time


class CubeTimePlotter:

    def __init__(self, inputfile, outputfile="", plot=True):
        self.inputFile = inputfile
        self.outputFile = outputfile
        self.plot = plot
        self.times = Fh.get_times(inputfile)

    def init(self):
        if self.plot:
            start = time.time()
            self.plottimes(self.times)
            end = time.time()
            plot_time = end-start
            print "Plotting time: " + str("%.5f" % plot_time)

        start = time.time()
        self.writeout(self.times)
        end = time.time()
        writeout_time = end-start
        print "Writeout time: " + str("%.5f" % writeout_time)

    def plottimes(self, times):
        #Make a trace for the times
        x = range(1, len(times) + 1)
        trace1 = Scatter(x=x, y=times, mode='markers')

        #Make a trace for the average of last 5
        #Commented out, as it clutters the graph
        # averages = [0, 0, 0, 0]
        # for i in range(4, len(times)):
        #     subtable = []
        #     for j in range(i-4, i+1):
        #         subtable.append(times[j])
        #     avg = Mh.get_avg(subtable)
        #     averages.append(avg)
        #
        # x = range(1, len(averages)+1)
        # trace2 = Scatter(x=x, y=averages, mode='markers')

        data = Data([trace1])
        py.plot(data, filename=self.inputFile)

    def writeout(self, times):
        output = self.parsetimes(times)
        if len(self.outputFile) > 0:
            self.saveoutput(output)
        else:
            print output

    def saveoutput(self, out):
        f = open(self.outputFile, "w")
        f.write(out)
        f.close()

    def parsetimes(self, times):
        hr = "---" + newline
        out = hr

        out += "Number of solves:                " + str(Lh.get_number_of_solves(times)) + newline
        out += hr

        out += "Lifetime average:                " + str(Lh.get_lifetime_avg(times)) + newline
        out += "Lifetime best:                   " + str(Lh.get_lifetime_best(times)) + newline
        out += "Lifetime best 5:                 " + \
               ', '.join(str(i) for i in Mh.get_lifetime_n_best(times, 5)) + newline
        out += hr

        out += "List of last 5:                  " + str(Lh.get_list_of_last_n(5, times)) + newline
        out += "Average of last 5:               " + str(Mh.get_avg_of_last_n(5, times)) + newline
        out += hr

        out += "Average of last 10:              " + str(Mh.get_avg_of_last_n(10, times)) + newline
        out += "Average of last 12:              " + str(Mh.get_avg_of_last_n(12, times)) + newline
        out += "Average of last 100:             " + str(Mh.get_avg_of_last_n(100, times)) + newline
        out += hr

        out += "List of first 5:                 " + str(Lh.get_list_of_first_n(5, times)) + newline
        out += "Average of first 5:              " + str(Mh.get_avg_of_first_n(5, times)) + newline
        out += hr

        out += "Average of first 10:             " + str(Mh.get_avg_of_first_n(10, times)) + newline
        out += "Average of first 12:             " + str(Mh.get_avg_of_first_n(12, times)) + newline
        out += "Average of first 100:            " + str(Mh.get_avg_of_first_n(100, times)) + newline
        out += hr

        out += "Percentage change in avg of 5:   " + \
            str("%.2f" % Mh.get_percentage_improvement_of_first_to_last_n(5, times)) + newline
        out += "Percentage change in avg of 10:  " + \
            str("%.2f" % Mh.get_percentage_improvement_of_first_to_last_n(10, times)) + newline
        out += "Percentage change in avg of 12:  " + \
            str("%.2f" % Mh.get_percentage_improvement_of_first_to_last_n(12, times)) + newline
        out += hr

        best5 = Mh.get_best_avg_of_n(5, times)
        out += "Best Ao5 so far:                 " + \
            str(best5[0]) + " with the solves: " + \
            ', ' . join(str(i) for i in best5[1]) + newline
        out += "Best Ao12 so far:                " + str(Mh.get_best_avg_of_n(12, times)[0]) + newline
        out += "Best Ao100 so far:               " + str(Mh.get_best_avg_of_n(100, times)[0]) + newline

        return out