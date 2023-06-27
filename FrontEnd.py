# Form implementation generated from reading ui file 'FormTuber.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import time
import sys
import os
from BackEnd import Downloader, check_folder
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(527, 219)
        MainWindow.setMinimumSize(QtCore.QSize(527, 219))
        MainWindow.setMaximumSize(QtCore.QSize(527, 219))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 232, 198), stop:1 rgb(255, 32, 54));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(180, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartButton.setFont(font)
        self.StartButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.StartButton.setAutoFillBackground(False)
        self.StartButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"")
        self.StartButton.setObjectName("StartButton")
        self.StartButton.clicked.connect(self.download)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 451, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.TextURL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TextURL.setGeometry(QtCore.QRect(80, 60, 381, 22))
        self.TextURL.setObjectName("TextURL")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(140, 110, 281, 24))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.downloader = Downloader()
        self.downloader.progress.connect(self.update_progress_bar)
        self.labelURL = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelURL.setGeometry(QtCore.QRect(30, 60, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelURL.setFont(font)
        self.labelURL.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.labelURL.setObjectName("labelURL")
        self.VideoButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.VideoButton.setGeometry(QtCore.QRect(81, 101, 49, 17))
        self.VideoButton.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.VideoButton.setObjectName("VideoButton")
        self.AudioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.AudioButton.setGeometry(QtCore.QRect(81, 124, 50, 17))
        self.AudioButton.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.AudioButton.setObjectName("AudioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Insert your link below, check Audio or Video and Download"))
        self.labelURL.setText(_translate("MainWindow", "URL : "))
        self.VideoButton.setText(_translate("MainWindow", "Video"))
        self.AudioButton.setText(_translate("MainWindow", "Audio"))
    
    def update_progress_bar(self, progress):
        self.progressBar.setValue(int(progress))     
    
    def download(self):
        url = self.TextURL.text()
        try:
            if url != None:
                if self.VideoButton.isChecked():
                    self.label.setText('Downloading video...')
                    self.progressBar.setValue(0)
                    self.downloader.download_video(url)
                    self.label.setText('Video has been downloaded!')
                if self.AudioButton.isChecked():
                    self.label.setText('Downloading audio...')
                    self.progressBar.setValue(0)
                    self.downloader.download_audio(url)
                    self.label.setText('Audio has been downloaded!')
            else:
                self.label.setText('Insert you link please and try again')
        except:
            self.label.setText('Error! Check your link please and try again')

if __name__ == "__main__":
    check_folder()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Create a QPixmap instance with the path to your desired image file
    pixmap = QPixmap(f"{os.environ['UserProfile']}/OneDrive/Desktop/CodeStudio/ContentSaver/ContentSaver/inbox.png")
    #C:/Users/Balab/OneDrive/Desktop/CodeStudio/ContentSaver/ContentSaver/inbox.png
    # Convert the QPixmap to a QIcon
    icon = QIcon(pixmap)
    MainWindow.setWindowIcon(icon)
    MainWindow.show()
    sys.exit(app.exec())

'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())'''