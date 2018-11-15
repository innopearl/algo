#https://stackoverflow.com/questions/48125674/how-to-read-multiple-csv-files-store-data-and-plot-in-one-figure-using-python?rq=1

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from matplotlib import dates

#
### Set your path to the folder containing the .csv files
PATH = './' # Use your path

### Fetch all files in path
fileNames = os.listdir(PATH)

### Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

### Configure Plot
def configurePlot():
    numPlot = 1
    gs  = gridspec.GridSpec(numPlot, 1, height_ratios=[1])
    ax = plt.subplot(gs[0])

    ax.fmt_xdata = DateFormatter("%Y-%m-%d %H:%M:%S")
    ax.set_xlabel('Time')
    ax.set_ylabel('Y')

    #http://leancrew.com/all-this/2015/01/labeling-time-series/
    days = dates.DayLocator()
    hours = dates.HourLocator()
    minutes = dates.MinuteLocator()
    seconds = dates.SecondLocator()
    dfmt = dates.DateFormatter('%m%d-%H:%M')

    #2018-03-16 13:25:31,113
    #datemin = datetime.strptime(time[0], "%Y-%m-%d %H:%M:%S")
    #datemax = datetime.strptime(time[len(time)-1], "%Y-%m-%d %H:%M:%S")
    #logger.info('{}  {}'.format(datemin, datemax))
    try:
        #ax.xaxis.set_major_locator(minutes)
        #ax.xaxis.set_minor_locator(seconds)
        ax.xaxis.set_major_locator(hours)
        ax.xaxis.set_minor_locator(minutes)
    except:
        pass
    ax.xaxis.set_major_formatter(dfmt)
    #ax.set_xlim(datemin, datemax)
    #ax.set_xlim(time[0], time[len(time)-1])

    ax.legend()
    return ax
### Loop over all files
ax = configurePlot()
for file in fileNames:

    ### Read .csv file and append to list
    df = pd.read_csv(PATH + file, sep=",")
    print(df.head())
    time = df.ix[:, 'T']
    x = df.ix[:, 'X']
    y = df.ix[:, 'Y']

    #https://matplotlib.org/users/colors.html
    time = pd.to_datetime(time)
    ### Create line for every file
    ax.plot(time, y, label=file) #color='C1', 

### Generate the plot
plt.show()
