# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decgui2.ui'
#
# Created: Tue May 04 16:42:02 2010
#      by: PyQt4 UI code generator 4.7.3
#
"""

@author: Akhil Wali
"""

from PyQt4 import QtCore, QtGui

class Ui_decappWindow(object):
    def setupUi(self, decappWindow):
        decappWindow.setObjectName("decappWindow")
        decappWindow.resize(302, 412)
        decappWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtGui.QWidget(decappWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open = QtGui.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(0, 0, 301, 41))
        self.open.setObjectName("open")
        self.local = QtGui.QLineEdit(self.centralwidget)
        self.local.setGeometry(QtCore.QRect(110, 40, 191, 20))
        self.local.setObjectName("local")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 111, 20))
        self.label_2.setObjectName("label_2")
        self.remote = QtGui.QLineEdit(self.centralwidget)
        self.remote.setGeometry(QtCore.QRect(110, 60, 191, 20))
        self.remote.setObjectName("remote")
        self.go = QtGui.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(0, 80, 301, 41))
        self.go.setObjectName("go")
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(0, 360, 301, 51))
        self.exit.setObjectName("exit")
        self.messages = QtGui.QTableWidget(self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(0, 120, 301, 241))
        self.messages.setObjectName("messages")
        decappWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(decappWindow)
        QtCore.QObject.connect(self.open, QtCore.SIGNAL("clicked()"), decappWindow.openClicked)
        QtCore.QObject.connect(self.go, QtCore.SIGNAL("clicked()"), decappWindow.decryptMessages)
        QtCore.QObject.connect(self.exit, QtCore.SIGNAL("clicked()"), decappWindow.exitClicked)
        QtCore.QMetaObject.connectSlotsByName(decappWindow)

    def retranslateUi(self, decappWindow):
        decappWindow.setWindowTitle(QtGui.QApplication.translate("decappWindow", "decrypy", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("decappWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("decappWindow", "Local username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("decappWindow", "Remote username:", None, QtGui.QApplication.UnicodeUTF8))
        self.go.setText(QtGui.QApplication.translate("decappWindow", "Decrypt!", None, QtGui.QApplication.UnicodeUTF8))
        self.exit.setText(QtGui.QApplication.translate("decappWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.initTable()

    def initTable(self):
        self.messages.clear()
        head=["Sender","Message"]
        self.messages.setColumnCount(len(head))
        self.messages.setHorizontalHeaderLabels(head)
        self.messages.setColumnWidth(0,100)
        self.messages.setColumnWidth(1,197)
        
    def getHandles(self):
        return {'local':str(self.local.text()),'remote':str(self.remote.text())}
        
    def setMessages(self,mesgs):
        self.initTable()
        self.messages.setRowCount(len(mesgs))
        
        cur=0
        for i in mesgs:
            item = QtGui.QTableWidgetItem(i['sr'])
            self.messages.setItem(cur,0,item)
            item = QtGui.QTableWidgetItem(i['message'])
            self.messages.setItem(cur,1,item)
            cur+=1
        
        self.messages.resizeColumnsToContents()
    
        
