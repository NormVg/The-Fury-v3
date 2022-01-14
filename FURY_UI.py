from PyQt5 import QtCore, QtGui, QtWidgets
########################################################

from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import startfile
import time
##############################################################
from THE_FURY import run_fury,take_command
import sys
from keyboard import press_and_release
import pyautogui
from speak import speak
###############################################################

class MainThreado(QThread):
    
    def __init__(self):
        super(MainThreado,self).__init__()

    def run(self):
        self.wake_up()
        
    def wake_up(self):

         press_and_release('windows + m')
         time.sleep(11)
         pyautogui.keyDown("alt")
         pyautogui.press("tab")
         pyautogui.keyUp("alt")
         while True:
            
             
                self.start =  take_command()
                if "wake up" in self.start or "fury" in self.start:
                    speak("i am online boss")
                    run_fury()  
                    #offline()

                elif "leave me alone" in self.start or "shutdown" in self.start:
                    speak("have a good day boss")
                    time.sleep(1)    
                    sys.exit()



startFunction = MainThreado()

class loadingScreen(QWidget):
    def __init__(self): 
        super().__init__()

        self.setFixedSize(640,360)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation = QLabel(self)
        self.movie = QMovie("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\GUI\\loading.gif")
        self.label_animation.setMovie(self.movie)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground,on=True)
        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(10000, self.stopAnimation)
        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

###########################################################################

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
            
        MainWindow.setObjectName("THE FURY")
        MainWindow.resize(1220, 629)
        MainWindow.setFixedSize(1220,629)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BACKGROUND = QtWidgets.QLabel(self.centralwidget)
        self.BACKGROUND.setGeometry(QtCore.QRect(-14, -30, 1251, 701))
        self.BACKGROUND.setText("")
        self.BACKGROUND.setPixmap(QtGui.QPixmap("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\GUI\\backgroung.jpg"))
        self.BACKGROUND.setScaledContents(True)
        self.BACKGROUND.setObjectName("BACKGROUND")
        self.GIF = QtWidgets.QLabel(self.centralwidget)
        self.GIF.setGeometry(QtCore.QRect(0, -30, 1211, 651))
        self.GIF.setText("")
        self.GIF.setPixmap(QtGui.QPixmap("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\GUI\\main.gif"))
        
        self.GIF.setScaledContents(True)
        self.GIF.setObjectName("GIF")
        
        self.FURY_LOGO = QtWidgets.QLabel(self.centralwidget)
        self.FURY_LOGO.setGeometry(QtCore.QRect(10, 10, 441, 161))
        self.FURY_LOGO.setText("")
        self.FURY_LOGO.setPixmap(QtGui.QPixmap("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\GUI\\fury.png"))
        self.FURY_LOGO.setObjectName("FURY_LOGO")
        self.INPUT = QtWidgets.QLabel(self.centralwidget)
        self.INPUT.setGeometry(QtCore.QRect(6, 500, 521, 101))
        self.INPUT.setStyleSheet("font: 10pt \"Agency FB\";")
        self.INPUT.setText("")
        self.INPUT.setObjectName("INPUT")
        self.EXET = QtWidgets.QPushButton(self.centralwidget)
        self.EXET.setGeometry(QtCore.QRect(1030, 550, 181, 51))
        self.EXET.setStyleSheet("background-color: rgb(189, 147, 249) ;font: 12pt \"OCR A Std\"")
        #self.EXET.setStyleSheet("background-color: rgb(80, 250, 123);")
        self.EXET.setObjectName("EXIT")
        self.FIG = QtWidgets.QLabel(self.centralwidget)
        self.FIG.setGeometry(QtCore.QRect(870, 0, 349, 369))
        self.FIG.setText("")
        self.FIG.setPixmap(QtGui.QPixmap("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\GUI\\ico.png"))

        self.FIG.setScaledContents(True)
        self.FIG.setObjectName("FIG")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setStyleSheet("background-color: rgb(80, 250, 123);")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.How_to_use = QtWidgets.QAction(MainWindow)
        self.How_to_use.setObjectName("How_to_use")
        self.info = QtWidgets.QAction(MainWindow)
        self.info.setObjectName("info")
        self.Program_files = QtWidgets.QAction(MainWindow)
        self.Program_files.setObjectName("Program_files")
        self.menuOptions.addAction(self.How_to_use)
        self.menuOptions.addAction(self.info)
        self.menuOptions.addAction(self.Program_files)
        self.menubar.addAction(self.menuOptions.menuAction())
        

        startFunction.start()
###############################################################################################################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def clicked_exit(o,p):
        try:
            #while True:
                speak('shutting systems down,,,,,,,,,,')
                time.sleep(2)
                sys.exit()
        except:
            sys.exit()

    def how(o,p):
        startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\how to use.txt")

    def infom(o,p):
        startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\FURY.docx")

    def files(o,p):
        startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury")
#######################################################################################################################
    def retranslateUi(self, MainWindow):
        self.loadingscreen = loadingScreen()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "THE FURY"))
        self.EXET.setText(_translate("MainWindow", "EXIT"))
        self.EXET.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.EXET.clicked.connect(self.clicked_exit)
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.How_to_use.setText(_translate("MainWindow", "How to use"))
        self.How_to_use.triggered.connect(self.how)
        self.info.setText(_translate("MainWindow", "Info"))
        self.info.triggered.connect(self.infom)
        self.Program_files.setText(_translate("MainWindow", "Program files"))
        self.Program_files.triggered.connect(self.files)
        self.movies = QMovie("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\all file\\20210726-4_1080p.gif")
        self.GIF.setMovie(self.movies)
        self.movies.start()
        startFunction.start()        
##########################################################################################################


def run_gui():
        app = QtWidgets.QApplication(sys.argv)
        GUI = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(GUI)
        GUI.show()
        sys.exit(app.exec_())

#####################################################################################################

if __name__ == "__main__":

    from NPEM import npem

    
    def password():
             speak('powering up system')
             npem()
             speak('system powered up')

             extracted_pass = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\password.txt",'rt')
             password = extracted_pass.read()
             password = str(password)
             speak("verify your self")
             passcode = pyautogui.password('Verify your self. ')
             speak("verification done")
             



             if  passcode == password:
                 print("access granted")
                 speak("access granted")
                 
                 run_gui()
 
             else:
                 print("access not granted")
                 speak("access not granted")
                 sys.exit()
    password()
  


