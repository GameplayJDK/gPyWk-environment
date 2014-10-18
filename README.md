# gPyWk-environment

## Introduction

gPyWk-environment represents the term "Graphical Python WebKit"-environment and is a HTML5 framework for the linux operation system written entirely in python (3.4.0). It depends on GNOME's GObjectIntrospection for python (pyGI), which isn't available for Windows yet.

Only consisting of a scrollable WebKit WebView and a powerful and flexible "x-js-py" api layer, bundled with a JSONConfig parser and the JavaScript api bindings, it is lightweight while also being a solid base to build your desktop application on.

## Features

* Detailed configuartion
* Fullfeatured WebKit browser which can be customized completely through the application-specific configuartion
* Powerful "x-js-py" api layer with JavaScript bindings

Planned features are:

* Windows support (vista and newer)
* Packaging tool 

## Requirements

* [GNOME's GObject Introspection (pyGI) 3.12.0-1 or newer](https://wiki.gnome.org/Projects/PyGObject/)
* [Python 3.4.0 or newer](https://www.python.org/download/releases/3.4.0/)

## Downloads

* **v0.0.1a** - Release scheduled for 10/20/2014
  * [.tar.gz Archive]() (Coming soon)
  * [Launchpad PPA]() (Coming soon)

## Installation

* Download and extract the latest version to a folder of your choice (for example `~/Documents/tmp/gPyWk-environment-development`)
* Edit the Application.json file to suite your application (e.g. Title, Width, Height, Properties)
* Modify the default.html file (but make sure to import `Api.js` correctly)
* Run the script for the operation system of your choice (linux = .sh; Windows = .bat)

## Documentation

The documentation is in progress and will be available under `https://github.com/GameplayJDK/gPyWk-environment/tree/master/documentation` [#](https://github.com/GameplayJDK/gPyWk-environment/tree/master/documentation).

**Important:** Make sure you read the blog article on [How to use the gPyWk-environment to create a HTML5 desktop application]() (Coming soon)

## Bug Notice

* **Warning:** This project is an early release state. It may contain bugs that influence the functionality of your application! Please also notice, that the `x-js-py` api layer is existent, but not fully finished yet.

## License

```
Copyright (C) 2014 GameplayJDK

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
```
View full license [here](http://www.gnu.org/license/gpl.txt).
