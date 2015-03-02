__author__ = 'aleksander'


def load_file():
    try:
        filepath = "/home/aleksander/Dropbox/Aleks/Cubing/Times/20150227/3x3.csv"
        with open(filepath) as f:
            content = f.readlines()
        return content
    except TypeError as e:
        print "A TypeError occurred while trying to load file.\nMessage: " + e.message
    except Exception as e:
        print "An exception occurred while trying to load file.\nMessage: " + e.message


def get_times():
    content = load_file()

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
        except ValueError:
            continue
        except Exception as e:
            print "Exception in get_times(): " + e.message

    #Reverse the list because Speedcube Timer lists them from last to first
    times.reverse()

    return times
