#!/usr/bin/python

import os
import sys
import optparse

def dir_scan():

	print os.listdir(dir)
	if(f != None):
		for i in os.listdir(dir):
			f.write(i+"\n")

def all_dir_scan():
	
	for (path, dirs, files)  in os.walk(dir):
		print (str(path) + str(dirs))
		if ( f != None):
			f.write('Directory List is : "')
			f.write(str(path)+'"'+"\n")
	if ( f != None):
		f.write("\n\n-----------------------------------------------------------------------------------------------------\n\n\n")		
	for (path, dirs, files) in os.walk(dir):
		for file in files:
			print (str(path) + str(file))
			if( f != None):
				f.write('File List is : "')
				f.write(str(path)+str(file)+'"'+"\n")


parser = optparse.OptionParser("Enter the -d <Directory>, Want to Result file is -f <Create Result file>, Enter the -a <Scan the All>")
parser.add_option("-d", dest="dir", type="string", default=None, help="Please Enter the Directory Location")
parser.add_option("-f", dest="file", type="string", default=None, help="Create Result file Option.\nInput True is Reading Directory path craete file and You wnat create different directory Create file is Input Directory Location")
parser.add_option("-a", dest="all", type="string", default=None, help="Option is print, Input Directory Under All file & Directory")
(option, arg) =  parser.parse_args()

if(option.dir == None):
	print("Please Input Value is Directory Location")
	sys.exit()

elif(os.access(option.dir, os.F_OK) != True):
	print("Please Input Value is Normal Directory Loaction")
	sys.exit()

elif(option.file == None):
	dir = option.dir
	f = None
	if ( option.all != None):
		all_dir_scan()
		sys.exit()
	dir_scan()

elif(option.file == True or option.file == "true"):
	dir = option.dir
	f = open(dir+"/result.txt", "w")
	if(option.all != None):
		all_dir_scan()
		sys.exit()
	dir_scan()

elif(option.file !=None):
	dir = option.dir
	f = open("/"+option.file+"/result.txt", "w")
	if(option.all != None):
		all_dir_scan()
		sys.exit()
	dir_scan()

