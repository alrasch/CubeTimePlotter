from CubeTimePlotter import CubeTimePlotter

import sys
import getopt


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:i:", ["no-plot"])
    except getopt.GetoptError as err:
        print str(err)
        printusage()

    inputfile = ""
    outputfile = ""
    plot = True
    #parse arguments from getopt
    for option, arg in opts:
        if option == "-h":
            printusage()
        elif option == "-i":
            inputfile = arg
        elif option == "-o":
            outputfile = arg
        elif option == "--no-plot":
            plot = False

    #do not plot if --no-plot present
    if "--no-plot" in args:
        plot = False
        args.remove("--no-plot")

    #grab inputFilename if -i not specified
    if len(args) > 0: 
        inputfile = args[0]

    if len(inputfile) == 0:
        print "inputfile required"
        printusage()

    ctp = CubeTimePlotter(inputfile, outputfile, plot)
    ctp.init()


def printusage():
    print "main.py [[-i] input file] [-o output file] [-h] [--no-plot]"
    exit(0)


if __name__ == "__main__":
    main()