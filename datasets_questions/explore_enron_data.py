#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
count = 0
for key in enron_data:
    if(enron_data[key]['poi'] == 1):
        count = count + 1
print "number of POI: ", count
print "number of messages from Wesley Colwell to POIs: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "exercised stock options of Jeff Skilling: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

############### How many folks have the quantified salary? #########################################
print "\ntotal memebers: ", len(enron_data.keys())
count_salary = 0
count_email = 0
for key in enron_data:
    if(enron_data[key]['salary'] != 'NaN'):
        count_salary = count_salary + 1
    if(enron_data[key]['email_address'] != 'NaN'):
        count_email = count_email + 1
print "folks that have quantified salary: ", count_salary
print "folks that have email address: ",count_email

############## What percentage of people have 'NaN' for their total payments? ######################
count_tp = 0
for key in enron_data:
    if(enron_data[key]['total_payments'] == 'NaN'):
        count_tp = count_tp + 1
print "\npercentage of people that have 'NaN' for their total payments: ", count_tp/len(enron_data.keys())

############# What percentage of POIs have 'NaN' for their total payments? ###########################
count_poi_Ntp = 0
count_poi = 0
for key in enron_data:
    if(enron_data[key]['poi'] == True):
        count_poi = count_poi + 1
        if(enron_data[key]['total_payments'] == 'NaN'):
            count_poi_Ntp = count_poi_Ntp + 1
print "\npercentage of POIs that have 'NaN' for their total payments: ", count_poi_Ntp/count_poi
