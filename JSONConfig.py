#!/usr/bin/pyton3.4

# Importing
import os
import json

# Defining the JSONConfig class
class JSONConfig ():

	# Defining the JSONConfig class constructor, which takes the RelativeConfigFilePath
	def __init__(self, jsonRelativeConfigFilePath):

		try:

			# Reading the file
			absoluteConfigFilePath = os.path.abspath(os.path.join(os.getcwd(), jsonRelativeConfigFilePath))
			configFile = open(absoluteConfigFilePath, 'r')
			configFileContent = configFile.read()
			configFile.close()

			# Declaring the json object
			self.configFileContentJSON = json.loads(configFileContent)

		except(Exception):

			# Printing the error message
			print('Error: '+'Unable to read config file correctly!')

	# Returning the json object
	def getObject(self):
		return self.configFileContentJSON
