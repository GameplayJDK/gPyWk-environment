#!/usr/bin/pyton3.4

# Importing
import JSONConfig
import Browser

# Defining the Main class
class Main ():

	# Defining the Main class constructor
	def __init__(self, configPath):

		# Creating a new instance of JSONConfig
		config = JSONConfig.JSONConfig(configPath).getObject()

		# Creating a new instance of BrowserWindow
		Browser.BrowserWindow(config["Window"]["Title"], config["Window"]["Width"], config["Window"]["Height"], config["Window"]["Resizability"], config["Window"]["Icon"], config["Content"]["HTML"], config["Browser"])
