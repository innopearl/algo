

import os
import pandas as pd
import matplotlib.pyplot as plt

### Set your path to the folder containing the .csv files
PATH = './' # Use your path

### Fetch all files in path
fileNames = os.listdir(PATH)

### Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

### Loop over all files
for file in fileNames:

    ### Read .csv file and append to list
    df = pd.read_csv(PATH + file, sep=",")
    print(df.head())

    t = df.ix[:, 'T']
    x = df.ix[:, 'X']
    y = df.ix[:, 'Y']

    ### Create line for every file
    plt.plot(x, y, label=file) #color='C1', 

### Generate the plot
plt.show()
