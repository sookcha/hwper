from PyObjCTools import AppHelper
from Cocoa import *
from Foundation import *

class HwperMainController(NSWindowController):
    searchFileButton = objc.IBOutlet()
    odfButton = objc.IBOutlet()
    
    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)
        
    @objc.IBAction
    def toODT_(self, sender):
        
 
    @objc.IBAction
    def fileSearch_(self, sender):
        self.count -= 1
        
    def updateDisplay(self):
        self.counterTextField.setStringValue_(self.count)
    
            
if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    viewController = HwperMainController.alloc().initWithWindowNibName_("HwperMain")
    viewController.showWindow_(viewController)
    NSApp.activateIgnoringOtherApps_(True)
    
    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()