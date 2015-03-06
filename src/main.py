from CubeTimePlotter import CubeTimePlotter

import sys
import getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:i:", ["no-plot"])
    except getopt.GetoptError as err:
        print str(err)
        printUsage()

    inputFile = ""
    outputFile = ""
    plot = True
    #parse arguemnets from getopt
    for option, arg in opts:
        if option == "-h":
            printUsage()
        elif option == "-i":
            inputFile = arg
        elif option == "-o":
            outputFile = arg
        elif option == "--no-plot":
            plot = False

    #do not plot if --no-plot present
    if "--no-plot" in args:
        plot = False
        args.remove("--no-plot")

    #grab inputFilename if -i not specified
    if len(args) > 0: 
        inputFile = args[0]

    if len(inputFile) == 0:
        print "inputFile required"
        printUsage()

    ctp = CubeTimePlotter(inputFile, outputFile, plot)
    ctp.init()


def printUsage():
    print "main.py [[-i] input file] [-o output file] [-h] [--no-plot]"
    exit(0)


if __name__ == "__main__":
    main()