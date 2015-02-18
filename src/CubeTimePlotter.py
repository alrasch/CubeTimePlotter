__author__ = 'aleksander'
from Helper import Helper
import plotly.plotly as py
from plotly.graph_objs import *


class CubeTimePlotter:

    helper = None
    times = None
    file = None

    def __init__(self):
        self.helper = Helper()
        self.times = self.get_times()
        self.init()

    def init(self):
        self.plot()
        print "Lifetime average: " + self.helper.get_lifetime_avg(self.times).__str__()
        print "Lifetime best:    " + self.helper.get_lifetime_best(self.times).__str__()

    def load_file(self):
        try:
            filepath = "/home/aleksander/Dropbox/Aleks/Cubing/Times/20150218/3x3.csv"
            with open(filepath) as f:
                content = f.readlines()
            return content
        except TypeError as e:
            print "A TypeError occurred while trying to load file.\nMessage: " + e.message
        except Exception as e:
            print "An exception occurred while trying to load file.\nMessage: " + e.message


    def get_times(self):
        content = self.load_file()

        times = []

        for line in content:
            time = line[22:]
            min = time[0:2]
            sec = time[3:5]
            centi = time[6:8]
            seccenti = sec + "." + centi

            try:
                seccenti = float(seccenti)
                min = float(min)
                addsec = 0
                if min > 0:
                    addsec = min * 60
                times.append(float(seccenti + addsec))
            except ValueError as e:
                print "ValueError in get_times(): " + e.message
            except Exception as e:
                print e.__class__ + " in get_times(): " + e.message

        #Reverse the list because Speedcube Timer lists them from last to first
        times.reverse()

        return times

    def plot(self):

        #Make a trace for the times
        times = self.get_times()
        x = []
        for i in range(1, len(times) + 1):
            x.append(i)
        trace1 = Scatter(x = x, y = times)

        #Make a trace for the average of last 5
        averages = [0, 0, 0, 0]
        for i in range(4, len(times)):
            subtable = []
            for j in range(i-4, i+1):
                subtable.append(times[j])
            avg = self.helper.get_avg(subtable)
            averages.append(avg)

        x = []
        for i in range(1, len(averages)+1):
            x.append(i)

        trace2 = Scatter(x = x, y = averages)

        data = Data([trace1, trace2])
        plot_url = py.plot(data, filename = 'basic-line')