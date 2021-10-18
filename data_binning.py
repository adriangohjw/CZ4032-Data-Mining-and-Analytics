import pandas as pd
import numpy as np

#discretize the continnuous variables
#column by column discretization
def data_binning(column):
    
    data = np.sort(column)
    
    min = data[0]
    max = data[len(data)-1]
    counter = len(data)

    Q1 = np.percentile(data,25)
    Q3 = np.percentile(data,75)
    IQR = Q3-Q1

    no_of_bins = (max-min)/(2*IQR*(counter**(-1/3)))
    w = (max-min)/no_of_bins

    bins = []
    for i in range(int(no_of_bins)):
        bins.append(min+((i+1)*w))

    columns = np.digitize(column,bins)
    return columns