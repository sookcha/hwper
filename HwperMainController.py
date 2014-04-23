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

from hwp5 import __version__ as version
from hwp5.proc import rest_to_docopt
from hwp5.proc import init_logger
from hwp5.errors import InvalidHwp5FileError
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
        hwpFileName = self.label.getStringValue
        self.label2.setStringValue_(hwpFileName)
 
    @objc.IBAction
    def fileSearch_(self, sender):
        panel = NSOpenPanel.openPanel()
        panel.setCanCreateDirectories_(True)
        panel.setCanChooseDirectories_(True)
        panel.setCanChooseFiles_(True)
        if panel.runModal() == NSOKButton:          
          self.label.setStringValue_(panel.filename())
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
