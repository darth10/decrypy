"""

@author: Akhil Wali
"""

from decgui2 import *
from decrypy import *

class decapp2(QtGui.QMainWindow):
    def __init__(self, ui_layout):
        QtGui.QMainWindow.__init__(self)
        
        self.ui = ui_layout
        ui_layout.setupUi(self)
    
    def decryptMessages(self):
        handles=self.ui.getHandles()
        y = YDecryptor(self.file,handles['local'],handles['remote'])
        
        mesgs = y.getMessages()
        if mesgs == False:
            #display message
            QtGui.QMessageBox.question(self,'',"Not readable",QtGui.QMessageBox.Ok)
        else:
            self.ui.setMessages(mesgs)
    
    def openClicked(self):
        filegui=QtGui.QFileDialog(parent=self)
        self.file=filegui.getOpenFileName(filter="*.dat")
    
    def exitClicked(self):
        self.close()

if __name__=='__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = decapp2(Ui_decappWindow())
    window.show()
    
    sys.exit(app.exec_())
