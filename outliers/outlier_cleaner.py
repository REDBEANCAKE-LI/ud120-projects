#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = [net_worths[i]-predictions[i] for i in range(0,len(ages))]
    error_abs = [abs(error[i]) for i in range(0,len(ages))]
    cleaned_data = [(ages[i],net_worths[i],error[i]) for i in range(0,len(ages))]
    ### delete the outliers ###
    for i in range(0,int(math.ceil(len(ages)*0.1))):
        index = error_abs.index(max(error_abs))
        del error_abs[index]
        del cleaned_data[index]
    return cleaned_data 

