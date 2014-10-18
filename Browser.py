#!/usr/bin/pyton3.4

# Importing
from   gi.repository import Gtk
from   gi.repository import WebKit
import os
import json
import Api

# Defining the BrowserWindow class, which extends Gtk.Window
class BrowserWindow (Gtk.Window):

	# Defining the BrowserWindow class constructor, which takes the Title, DefaultWidth, DefaultHeight, Resizability, IconPath, ContentPath, OverrideBrowserViewProperties
	def __init__(self, windowTitle, windowDefaultWidth, windowDefaultHeight, windowResizability, windowIconPath, windowContentPath, windowOverrideBrowserViewProperties):

		# Running the super's constructor
		Gtk.Window.__init__(self, title=windowTitle)

		# Getting the cwd
		cwd = os.getcwd()

		# Defining itself
		self.BrowserWindow = self;
		# Setting position, Requesting size, Setting resizability, Setting icon
		self.set_position(Gtk.WindowPosition.CENTER)
		self.BrowserWindow.set_size_request(windowDefaultWidth, windowDefaultHeight)
		self.BrowserWindow.set_resizable(windowResizability)
		self.BrowserWindow.set_icon_from_file(os.path.abspath(os.path.join(cwd, windowIconPath)))

		# Defining the ScrolledWindow control
		self.ScrollWindow = Gtk.ScrolledWindow()
		self.ScrollWindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

		# Defining the WebView control
		self.BrowserView = WebKit.WebView()

		"""Deprecated
		# Setting (all) properties to their default values
		#  All information were taken from "http://webkitgtk.org/reference/webkitgtk/stable/WebKitWebSettings.html"
		self.BrowserView.get_settings().set_property('auto-load-images', True)
		self.BrowserView.get_settings().set_property('auto-resize-window', False)
		self.BrowserView.get_settings().set_property('auto-shrink-images', True)
		self.BrowserView.get_settings().set_property('cursive-font-family', "serif")
		self.BrowserView.get_settings().set_property('default-encoding', "iso-8859-1")
		self.BrowserView.get_settings().set_property('default-font-family', "sans-serif")
		self.BrowserView.get_settings().set_property('default-font-size', 12)
		self.BrowserView.get_settings().set_property('default-monospace-font-size', 10)
		self.BrowserView.get_settings().set_property('editing-behavior', WebKit.EditingBehavior.UNIX)
		self.BrowserView.get_settings().set_property('enable-accelerated-compositing', False)
		self.BrowserView.get_settings().set_property('enable-caret-browsing', False)
		self.BrowserView.get_settings().set_property('enable-default-context-menu', True)
		self.BrowserView.get_settings().set_property('enable-developer-extras', False)
		self.BrowserView.get_settings().set_property('enable-display-of-insecure-content', True)
		self.BrowserView.get_settings().set_property('enable-dns-prefetching', True)
		self.BrowserView.get_settings().set_property('enable-dom-paste', False)
		self.BrowserView.get_settings().set_property('enable-file-access-from-file-uris', False)
		self.BrowserView.get_settings().set_property('enable-frame-flattening', False)
		self.BrowserView.get_settings().set_property('enable-fullscreen', True)
		self.BrowserView.get_settings().set_property('enable-html5-database', True)
		self.BrowserView.get_settings().set_property('enable-html5-local-storage', True)
		self.BrowserView.get_settings().set_property('enable-hyperlink-auditing', False)
		self.BrowserView.get_settings().set_property('enable-java-applet', True)
		self.BrowserView.get_settings().set_property('enable-media-stream', False)
		self.BrowserView.get_settings().set_property('enable-mediasource', False)
		self.BrowserView.get_settings().set_property('enable-offline-web-application-cache', True)
		self.BrowserView.get_settings().set_property('enable-page-cache', False)
		self.BrowserView.get_settings().set_property('enable-plugins', True)
		self.BrowserView.get_settings().set_property('enable-private-browsing', False)
		self.BrowserView.get_settings().set_property('enable-running-of-insecure-content', True)
		self.BrowserView.get_settings().set_property('enable-scripts', True)
		self.BrowserView.get_settings().set_property('enable-site-specific-quirks', False)
		self.BrowserView.get_settings().set_property('enable-smooth-scrolling', False)
		self.BrowserView.get_settings().set_property('enable-spatial-navigation', False)
		self.BrowserView.get_settings().set_property('enable-spell-checking', False)
		self.BrowserView.get_settings().set_property('enable-universal-access-from-file-uris', False)
		self.BrowserView.get_settings().set_property('enable-webaudio', False)
		self.BrowserView.get_settings().set_property('enable-webgl', False)
		self.BrowserView.get_settings().set_property('enable-xss-auditor', True)
		self.BrowserView.get_settings().set_property('enforce-96-dpi', False)
		self.BrowserView.get_settings().set_property('fantasy-font-family', "serif")
		self.BrowserView.get_settings().set_property('html5-local-storage-database-path', "$HOME/.local/share/webkit/databases")
		self.BrowserView.get_settings().set_property('javascript-can-access-clipboard', False)
		self.BrowserView.get_settings().set_property('javascript-can-open-windows-automatically', False)
		self.BrowserView.get_settings().set_property('media-playback-allows-inline', True)
		self.BrowserView.get_settings().set_property('media-playback-requires-user-gesture', False)
		self.BrowserView.get_settings().set_property('minimum-font-size', 5)
		self.BrowserView.get_settings().set_property('minimum-logical-font-size', 5)
		self.BrowserView.get_settings().set_property('monospace-font-family', "monospace")
		self.BrowserView.get_settings().set_property('print-backgrounds', True)
		self.BrowserView.get_settings().set_property('resizable-text-areas', True)
		self.BrowserView.get_settings().set_property('respect-image-orientation', False)
		self.BrowserView.get_settings().set_property('sans-serif-font-family', "sans-serif")
		self.BrowserView.get_settings().set_property('serif-font-family', "serif")
		self.BrowserView.get_settings().set_property('spell-checking-languages', None)
		self.BrowserView.get_settings().set_property('tab-key-cycles-through-elements', True)
		self.BrowserView.get_settings().set_property('user-agent', "")
		self.BrowserView.get_settings().set_property('user-stylesheet-uri', None)
		self.BrowserView.get_settings().set_property('zoom-step', 0.1)
		"""

		# Overriding BrowserView properties
		for(browser_property)in(windowOverrideBrowserViewProperties):

			# Set the property with key to value
			self.BrowserView.get_settings().set_property(browser_property["key"], browser_property["value"])

		# Loading the main file
		self.BrowserView.load_uri('file://'+os.path.abspath(os.path.join(cwd, windowContentPath)))

		# Setting up the "x-js-py:" api layer
		#  Initializing and declaring the Api class
		self.Api = Api.Api()
		#  Connecting the "navigation-policy-decision-requested" with the "api_request_handler" method
		self.BrowserView.connect("navigation-policy-decision-requested", self.api_request_handler)

		# Adding the WebView control to the ScrolledWindow
		self.ScrollWindow.add(self.BrowserView)
		# Adding the ScrolledWindow to the window
		self.add(self.ScrollWindow)

		# Connecting the "delete-event" with the "destroy" method
		self.connect("delete-event", self.destroy)
		# Showing all controls
		self.show_all()

		# Starting the main Gtk thread
		Gtk.main()

	# Handling the "navigation-policy-decision-requested"
	def api_request_handler(self, view, frame, request, action, decision):

		# Getting the full request uri
		request_uri = request.get_uri()

		# Checking if the request uri starts with a known protocol-prefix
		if(request_uri.startswith('x-js-py:')):

			# Ignoreing the request
			decision.ignore()

			# Removing the protocol-prefix from the request uri
			request_uri = request_uri.replace('x-js-py:', '')

			# Predefining the needed parameters
			call_parameter_target = None
			call_parameter_arguments = None
			call_parameter_callback = None

			# Looping through all parameters in the request uri
			for(parameter)in(request_uri.split('|:|')):

				if(parameter.startswith('call_parameter_target=')):
					call_parameter_target = parameter.replace('call_parameter_target=', '')
				if(parameter.startswith('call_parameter_arguments=')):
					call_parameter_arguments = parameter.replace('call_parameter_arguments=', '')
					call_parameter_arguments = json.loads(call_parameter_arguments)
				if(parameter.startswith('call_parameter_callback=')):
					call_parameter_callback = parameter.replace('call_parameter_callback=', '')

			# Verifying the parameters
			if(call_parameter_target != None)and(call_parameter_arguments != None)and(call_parameter_callback != None):

				# Checking if the API_METHODS list contains the method name
				if(call_parameter_target)in(self.Api.API_METHODS):

					# Run the callback javascript function with the result json as argument which is returned by the api method
					try:
						self.BrowserView.execute_script(call_parameter_callback+'('+json.dumps(getattr(Api, call_parameter_target)(call_parameter_arguments))+')')
					except(Exception):
						print('Error: '+'Unable to execute requested api method or javascript callback!')

				else:

					# Printing the error message
					print('Error: '+'Unable to find requested api method!')

			else:

				# Printing the error message
				print('Error: '+'Unable to find all needed parameters!')

			# Marking the request as handled by returning "True"
			return(True)

		# Marking the request as unhandled by returning "False"
		return(False)

	# Handling the "delete-event"
	def destroy(self, widget, data=None):

		# Quit the main Gtk thread
		Gtk.main_quit()
