"""
/***************************************************************************
Name			 	 : IDECANARIAS Search
Description          : Perform querys in toponimia
Date                 : 19/Aug/11 
copyright            : (C) 2011 by Felix J. Hdez
email                : fhernandeze@grafcan.es 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "IDECANARIAS" 
def description():
  return "Perform querys in Local toponimia"
def version(): 
  return "Version 1.03" 
def qgisMinimumVersion():
  return "1.8"
def icon():
  return "icon.png"
def authorName():
	return "Felix Jose Hernandez"
def classFactory(iface): 
  # load IdecanariasSearch class from file IdecanariasSearch
  from IDESearch import IDESearch 
  return IDESearch(iface)
