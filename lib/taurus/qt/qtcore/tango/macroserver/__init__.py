#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""
MacroServer extension for taurus Qt
"""

__docformat__ = 'restructuredtext'

from .macroserver import *

def registerExtensions():
    """Registers the macroserver extensions in the :class:`taurus.core.tango.TangoFactory`"""
    import taurus
    factory = taurus.Factory()
    factory.registerDeviceClass('MacroServer', QMacroServer)
    factory.registerDeviceClass('Door', QDoor)
    