from PyObjCTools import AppHelper
from Cocoa import *
from Foundation import *

class HwperMainController(NSWindowController):
    searchFileButton = objc.IBOutlet()
    odtButton = objc.IBOutlet()
    label = objc.IBOutlet()
    
    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)
        self.count = 0
        
    @objc.IBAction
    def toODT_(self, sender):
        self.count += 1
        self.label.setStringValue_(self.count)
 
    @objc.IBAction
    def fileSearch_(self, sender):
        panel = NSOpenPanel.openPanel()
        panel.setCanCreateDirectories_(True)
        panel.setCanChooseDirectories_(True)
        panel.setCanChooseFiles_(True)
        if panel.runModal() == NSOKButton:
          return panel.filename()
        return
            
if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    viewController = HwperMainController.alloc().initWithWindowNibName_("HwperMain")
    viewController.showWindow_(viewController)
    NSApp.activateIgnoringOtherApps_(True)
    
    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()
