# CubeTimePlotter

**Disclaimer:**

This project is entirely niche. The code is meant for one specific purpose, and takes input in one specific way. There is no scalability to this project, and none is intended.

**Purpose:**

The Android App called Speedcube Timer exports your records to a .csv file. This script compiles the times, and outputs a graph of all times and averages to plot.ly.

##Setup

```
pip install -r requirements.txt
```

The plotting funcitonality of this program uses [Plot.ly](https://plot.ly), it requires a user account and API key. Sign up and go to the [Getting Started](https://plot.ly/python/getting-started/) section of their API docs to get a key.

##Usage

```
python src/main.py [[-i] input file] [-o output file] [-h] [--no-plot]
```

- `-i filename`: set input file. (filename required, `-i` is not)
- `-o filename`: set output file. (optional)
- `-h`: print usage and exit. (optional)
- `--no-plot`: do not plot times. (optional)

##Example Output:

![alt tag](https://github.com/AlecTheDev/CubeTimePlotter/blob/master/img/Example1.png)
