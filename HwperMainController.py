# -*- coding: utf-8 -*-
#
# Hwper with Cocoa
# author : Ho-seong Son <me@sookcha.com>
# 2014. 04.
#
#

from PyObjCTools import AppHelper
from Cocoa import *
from Foundation import *

import os
import os.path
import logging
import sys
import urllib
import urllib2
import tempfile
import StringIO

from hwp5.dataio import ParseError
from hwp5.xmlmodel import Hwp5File
from tempfile import mkstemp

from hwp5 import __version__ as version
from hwp5.proc import rest_to_docopt
from hwp5.proc import init_logger
from hwp5.errors import InvalidHwp5FileError
from hwp5.hwp5odt import *
from tempfile import mkstemp
from hwp5.plat import get_xslt
from hwp5.hwp5odt import hwp5_resources_filename
from lxml import etree
from docopt import docopt



class HwperMainController(NSWindowController):
    searchFileButton = objc.IBOutlet()
    odtButton = objc.IBOutlet()
    label = objc.IBOutlet()
    label2 = objc.IBOutlet()

    fileName = ""

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)

    @objc.IBAction
    def toODT_(self, sender):
    	
         
      xslt = plat.get_xslt()
      rng = plat.get_relaxng()
      
      hwp5file = Hwp5File(self.fileName)
      
      destName = self.fileName.replace(".hwp",".odt")
      
      ODTSingleDocumentConverter(xslt, rng).convert_to(hwp5file,destName)

    @objc.IBAction
    def fileSearch_(self, sender):
        panel = NSOpenPanel.openPanel()
        panel.setCanCreateDirectories_(True)
        panel.setCanChooseDirectories_(True)
        panel.setCanChooseFiles_(True)
        if panel.runModal() == NSOKButton:
          self.label.setStringValue_(panel.filename())
          self.fileName = panel.filename()
        return

    def hwp5odt(hwp5file, base_dir):
      """docstring for hwp5odt"""

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    viewController = HwperMainController.alloc().initWithWindowNibName_("HwperMain")
    viewController.showWindow_(viewController)
    NSApp.activateIgnoringOtherApps_(True)

    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()
