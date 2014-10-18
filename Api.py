#!/usr/bin/pyton3.4

# Defining the Api class
class Api ():

	# Defining the Api class constructor
	def __init__(self):

		# Declaring the API_METHODS list
		self.API_METHODS = []

		# --- Append all names of the api methods to API_METHODS below ---
		self.API_METHODS.append("run")

# --- Define all api methods below ---

def run(s):
	return({"rtext":"now running "+str(s[0])})
