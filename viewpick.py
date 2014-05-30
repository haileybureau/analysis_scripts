#!/usr/bin/env python
#
#author: Hailey Bureau
#latest edits: 15 April 2014
#
import pprint, pickle

filename=raw_input('Hi! What file would you like to unpickle? (Example: 01-wc.pkl) ')#asks for the filename 
pkl_file = open(filename, 'rb')#plugs in user input and "rb"= read only

data1 = pickle.load(pkl_file)#load the pickle file
pprint.pprint(data1)#print the contents of the pickle file

pkl_file.close()#close the pickle file 
print "That's all she wrote!"
