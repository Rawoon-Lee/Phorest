# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1296, 1389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stack = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack.setGeometry(QtCore.QRect(0, 660, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setStyleSheet("background-color : #FFF7E7")
        self.stack.setObjectName("stack")
        self.InitPage = QtWidgets.QWidget()
        self.InitPage.setObjectName("InitPage")
        self.label = QtWidgets.QLabel(self.InitPage)
        self.label.setGeometry(QtCore.QRect(4, 330, 1271, 60))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color : #000000")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stack.addWidget(self.InitPage)
        self.ChoosePeoplePage = QtWidgets.QWidget()
        self.ChoosePeoplePage.setObjectName("ChoosePeoplePage")
        self.label_3 = QtWidgets.QLabel(self.ChoosePeoplePage)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 840, 100))
        font = QtGui.QFont()
        font.setFamily("Leferi Point Type Special")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.NextBtn = QtWidgets.QPushButton(self.ChoosePeoplePage)
        self.NextBtn.setGeometry(QtCore.QRect(1070, 40, 160, 100))
        font = QtGui.QFont()
        font.setFamily("Leferi Point Type Special")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.NextBtn.setFont(font)
        self.NextBtn.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20%;\n"
"}")
        self.NextBtn.setObjectName("NextBtn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ChoosePeoplePage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 170, 1261, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 20, 50, 20)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setObjectName("gridLayout")
        self.Btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn3.sizePolicy().hasHeightForWidth())
        self.Btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Btn3.setFont(font)
        self.Btn3.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 50%;\n"
"}")
        self.Btn3.setObjectName("Btn3")
        self.gridLayout.addWidget(self.Btn3, 0, 2, 1, 1)
        self.Btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Btn1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn1.sizePolicy().hasHeightForWidth())
        self.Btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Btn1.setFont(font)
        self.Btn1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Btn1.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 50%;\n"
"}")
        self.Btn1.setObjectName("Btn1")
        self.gridLayout.addWidget(self.Btn1, 0, 0, 1, 1)
        self.Btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn2.sizePolicy().hasHeightForWidth())
        self.Btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Btn2.setFont(font)
        self.Btn2.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 50%;\n"
"}")
        self.Btn2.setObjectName("Btn2")
        self.gridLayout.addWidget(self.Btn2, 0, 1, 1, 1)
        self.Btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn6.sizePolicy().hasHeightForWidth())
        self.Btn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Btn6.setFont(font)
        self.Btn6.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 50%;\n"
"}")
        self.Btn6.setObjectName("Btn6")
        self.gridLayout.addWidget(self.Btn6, 1, 2, 1, 1)
        self.Btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn5.sizePolicy().hasHeightForWidth())
        self.Btn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Btn5.setFont(font)
        self.Btn5.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 50%;\n"
"}")
        self.Btn5.setObjectName("Btn5")
        self.gridLayout.addWidget(self.Btn5, 1, 1, 1, 1)
        self.Btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn4.sizePolicy().hasHeightForWidth())
        self.Btn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Btn4.setFont(font)
        self.Btn4.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 50%;\n"
"}")
        self.Btn4.setObjectName("Btn4")
        self.gridLayout.addWidget(self.Btn4, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.ChoosePeoplePage)
        self.label_7.setGeometry(QtCore.QRect(220, 110, 831, 41))
        font = QtGui.QFont()
        font.setFamily("Leferi Point Type Special")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stack.addWidget(self.ChoosePeoplePage)
        self.ShotPage = QtWidgets.QWidget()
        self.ShotPage.setObjectName("ShotPage")
        self.Btn_Already = QtWidgets.QPushButton(self.ShotPage)
        self.Btn_Already.setGeometry(QtCore.QRect(410, 260, 460, 200))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Already.setFont(font)
        self.Btn_Already.setAutoFillBackground(False)
        self.Btn_Already.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-radius: 4px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20px;\n"
"}")
        self.Btn_Already.setAutoDefault(False)
        self.Btn_Already.setDefault(False)
        self.Btn_Already.setFlat(False)
        self.Btn_Already.setObjectName("Btn_Already")
        self.Btn_Back_2 = QtWidgets.QPushButton(self.ShotPage)
        self.Btn_Back_2.setGeometry(QtCore.QRect(40, 40, 160, 100))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Back_2.setFont(font)
        self.Btn_Back_2.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-radius: 4px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20px;\n"
"}")
        self.Btn_Back_2.setObjectName("Btn_Back_2")
        self.stack.addWidget(self.ShotPage)
        self.PhotoPage = QtWidgets.QWidget()
        self.PhotoPage.setObjectName("PhotoPage")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.PhotoPage)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 160, 1201, 541))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(85, 25, 85, 25)
        self.gridLayout_3.setHorizontalSpacing(142)
        self.gridLayout_3.setVerticalSpacing(32)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Photo3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.Photo3.setFont(font)
        self.Photo3.setStyleSheet("QLabel{\n"
"    border : 3px double #000000;\n"
"}")
        self.Photo3.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo3.setObjectName("Photo3")
        self.gridLayout_3.addWidget(self.Photo3, 1, 0, 1, 1)
        self.Photo1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.Photo1.setFont(font)
        self.Photo1.setStyleSheet("QLabel{\n"
"    border : 3px double #000000;\n"
"}")
        self.Photo1.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo1.setObjectName("Photo1")
        self.gridLayout_3.addWidget(self.Photo1, 0, 0, 1, 1)
        self.Photo2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.Photo2.setFont(font)
        self.Photo2.setStyleSheet("QLabel{\n"
"    border : 3px double #000000;\n"
"}")
        self.Photo2.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo2.setObjectName("Photo2")
        self.gridLayout_3.addWidget(self.Photo2, 0, 1, 1, 1)
        self.Photo4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.Photo4.setFont(font)
        self.Photo4.setStyleSheet("QLabel{\n"
"    border : 3px double #000000;\n"
"}")
        self.Photo4.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo4.setObjectName("Photo4")
        self.gridLayout_3.addWidget(self.Photo4, 1, 1, 1, 1)
        self.NextBtn_3 = QtWidgets.QPushButton(self.PhotoPage)
        self.NextBtn_3.setGeometry(QtCore.QRect(1070, 40, 160, 100))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NextBtn_3.setFont(font)
        self.NextBtn_3.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-radius: 4px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20px;\n"
"}")
        self.NextBtn_3.setObjectName("NextBtn_3")
        self.label_2 = QtWidgets.QLabel(self.PhotoPage)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 1200, 540))
        self.label_2.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.NextBtn_3.raise_()
        self.stack.addWidget(self.PhotoPage)
        self.ChooseFramePage = QtWidgets.QWidget()
        self.ChooseFramePage.setObjectName("ChooseFramePage")
        self.label_5 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_5.setGeometry(QtCore.QRect(220, 40, 840, 100))
        font = QtGui.QFont()
        font.setFamily("Leferi Point Type Special")
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.PrintBtn = QtWidgets.QPushButton(self.ChooseFramePage)
        self.PrintBtn.setGeometry(QtCore.QRect(1070, 40, 160, 100))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PrintBtn.setFont(font)
        self.PrintBtn.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-radius: 4px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20px;\n"
"}")
        self.PrintBtn.setObjectName("PrintBtn")
        self.ApplyBtn = QtWidgets.QPushButton(self.ChooseFramePage)
        self.ApplyBtn.setGeometry(QtCore.QRect(1120, 570, 140, 80))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ApplyBtn.setFont(font)
        self.ApplyBtn.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-radius: 4px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20px;\n"
"}")
        self.ApplyBtn.setObjectName("ApplyBtn")
        self.Frame_Id = QtWidgets.QLineEdit(self.ChooseFramePage)
        self.Frame_Id.setGeometry(QtCore.QRect(850, 570, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Frame_Id.setFont(font)
        self.Frame_Id.setStyleSheet("")
        self.Frame_Id.setText("")
        self.Frame_Id.setAlignment(QtCore.Qt.AlignCenter)
        self.Frame_Id.setObjectName("Frame_Id")
        self.Basic_Frame_1 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_1.setGeometry(QtCore.QRect(110, 170, 300, 80))
        self.Basic_Frame_1.setStyleSheet("background-color : #FFFFFF")
        self.Basic_Frame_1.setText("")
        self.Basic_Frame_1.setObjectName("Basic_Frame_1")
        self.Basic_Frame_2 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_2.setGeometry(QtCore.QRect(110, 310, 300, 80))
        self.Basic_Frame_2.setStyleSheet("background-color : #DEFF99")
        self.Basic_Frame_2.setText("")
        self.Basic_Frame_2.setObjectName("Basic_Frame_2")
        self.Basic_Frame_3 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_3.setGeometry(QtCore.QRect(110, 450, 300, 80))
        self.Basic_Frame_3.setStyleSheet("background-color : #BDD0FF    ")
        self.Basic_Frame_3.setText("")
        self.Basic_Frame_3.setObjectName("Basic_Frame_3")
        self.Basic_Frame_4 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_4.setGeometry(QtCore.QRect(110, 580, 300, 80))
        self.Basic_Frame_4.setStyleSheet("background-color : #B871FF")
        self.Basic_Frame_4.setText("")
        self.Basic_Frame_4.setObjectName("Basic_Frame_4")
        self.Basic_Frame_5 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_5.setGeometry(QtCore.QRect(470, 170, 300, 80))
        self.Basic_Frame_5.setStyleSheet("background-color : #000000\n"
"")
        self.Basic_Frame_5.setText("")
        self.Basic_Frame_5.setObjectName("Basic_Frame_5")
        self.Basic_Frame_6 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_6.setGeometry(QtCore.QRect(470, 310, 300, 80))
        self.Basic_Frame_6.setStyleSheet("border-image:url(\'./BasicFrame/stripe.jpg\')")
        self.Basic_Frame_6.setText("")
        self.Basic_Frame_6.setObjectName("Basic_Frame_6")
        self.Basic_Frame_7 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_7.setGeometry(QtCore.QRect(470, 450, 300, 80))
        self.Basic_Frame_7.setStyleSheet("border-image:url(\'./BasicFrame/ddangddang.png\')")
        self.Basic_Frame_7.setText("")
        self.Basic_Frame_7.setObjectName("Basic_Frame_7")
        self.Basic_Frame_8 = QtWidgets.QPushButton(self.ChooseFramePage)
        self.Basic_Frame_8.setGeometry(QtCore.QRect(470, 570, 300, 80))
        self.Basic_Frame_8.setStyleSheet("background-color : #84FFF8\n"
"")
        self.Basic_Frame_8.setText("")
        self.Basic_Frame_8.setObjectName("Basic_Frame_8")
        self.label_6 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_6.setGeometry(QtCore.QRect(859, 160, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Leferi Point Type Special")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_4.setGeometry(QtCore.QRect(940, 240, 250, 250))
        self.label_4.setStyleSheet("border-image:url(\'./QR_Dummy.png\')")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_8.setGeometry(QtCore.QRect(849, 500, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Leferi Point Type Special")
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stack.addWidget(self.ChooseFramePage)
        self.PrintingPage = QtWidgets.QWidget()
        self.PrintingPage.setObjectName("PrintingPage")
        self.label_10 = QtWidgets.QLabel(self.PrintingPage)
        self.label_10.setGeometry(QtCore.QRect(250, 270, 691, 161))
        self.label_10.setObjectName("label_10")
        self.stack.addWidget(self.PrintingPage)
        self.DonePrinting = QtWidgets.QWidget()
        self.DonePrinting.setObjectName("DonePrinting")
        self.label_11 = QtWidgets.QLabel(self.DonePrinting)
        self.label_11.setGeometry(QtCore.QRect(0, 350, 1280, 180))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.LogoImg_2 = QtWidgets.QLabel(self.DonePrinting)
        self.LogoImg_2.setGeometry(QtCore.QRect(540, 160, 200, 200))
        self.LogoImg_2.setStyleSheet("border-image:url(\'./logo.png\')")
        self.LogoImg_2.setText("")
        self.LogoImg_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoImg_2.setObjectName("LogoImg_2")
        self.stack.addWidget(self.DonePrinting)
        self.TopStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.TopStack.setGeometry(QtCore.QRect(0, 0, 1280, 660))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TopStack.sizePolicy().hasHeightForWidth())
        self.TopStack.setSizePolicy(sizePolicy)
        self.TopStack.setStyleSheet("background-color : #FFF7E7")
        self.TopStack.setObjectName("TopStack")
        self.LogoPage = QtWidgets.QWidget()
        self.LogoPage.setObjectName("LogoPage")
        self.LogoImg = QtWidgets.QLabel(self.LogoPage)
        self.LogoImg.setGeometry(QtCore.QRect(540, 230, 200, 200))
        self.LogoImg.setStyleSheet("border-image:url(\'./logo.png\')")
        self.LogoImg.setText("")
        self.LogoImg.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoImg.setObjectName("LogoImg")
        self.TopStack.addWidget(self.LogoPage)
        self.RecommandPosePage = QtWidgets.QWidget()
        self.RecommandPosePage.setObjectName("RecommandPosePage")
        self.LeftBtn = QtWidgets.QPushButton(self.RecommandPosePage)
        self.LeftBtn.setGeometry(QtCore.QRect(60, 265, 130, 130))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LeftBtn.setFont(font)
        self.LeftBtn.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20%;\n"
"}")
        self.LeftBtn.setObjectName("LeftBtn")
        self.RightBtn = QtWidgets.QPushButton(self.RecommandPosePage)
        self.RightBtn.setGeometry(QtCore.QRect(1090, 265, 130, 130))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.RightBtn.setFont(font)
        self.RightBtn.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: #F8F8F8        ;\n"
"    padding: 12px;\n"
"    border-bottom: 4px solid #c8c8c8;\n"
"    border-radius: 20%;\n"
"}")
        self.RightBtn.setObjectName("RightBtn")
        self.PoseStack = QtWidgets.QStackedWidget(self.RecommandPosePage)
        self.PoseStack.setGeometry(QtCore.QRect(200, 10, 880, 640))
        self.PoseStack.setObjectName("PoseStack")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.PoseImg_1 = QtWidgets.QLabel(self.page1)
        self.PoseImg_1.setGeometry(QtCore.QRect(40, 20, 800, 600))
        self.PoseImg_1.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.PoseImg_1.setAlignment(QtCore.Qt.AlignCenter)
        self.PoseImg_1.setObjectName("PoseImg_1")
        self.PoseStack.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.PoseImg_2 = QtWidgets.QLabel(self.page2)
        self.PoseImg_2.setGeometry(QtCore.QRect(40, 20, 800, 600))
        self.PoseImg_2.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.PoseImg_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PoseImg_2.setObjectName("PoseImg_2")
        self.PoseStack.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.PoseImg_3 = QtWidgets.QLabel(self.page3)
        self.PoseImg_3.setGeometry(QtCore.QRect(40, 20, 800, 600))
        self.PoseImg_3.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.PoseImg_3.setAlignment(QtCore.Qt.AlignCenter)
        self.PoseImg_3.setObjectName("PoseImg_3")
        self.PoseStack.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.PoseImg_4 = QtWidgets.QLabel(self.page4)
        self.PoseImg_4.setGeometry(QtCore.QRect(40, 20, 800, 600))
        self.PoseImg_4.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.PoseImg_4.setAlignment(QtCore.Qt.AlignCenter)
        self.PoseImg_4.setObjectName("PoseImg_4")
        self.PoseStack.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.PoseImg_5 = QtWidgets.QLabel(self.page5)
        self.PoseImg_5.setGeometry(QtCore.QRect(40, 20, 800, 600))
        self.PoseImg_5.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.PoseImg_5.setAlignment(QtCore.Qt.AlignCenter)
        self.PoseImg_5.setObjectName("PoseImg_5")
        self.PoseStack.addWidget(self.page5)
        self.TopStack.addWidget(self.RecommandPosePage)
        self.ShotPage_Top = QtWidgets.QWidget()
        self.ShotPage_Top.setObjectName("ShotPage_Top")
        self.Label_Camera = QtWidgets.QLabel(self.ShotPage_Top)
        self.Label_Camera.setGeometry(QtCore.QRect(240, 30, 800, 600))
        self.Label_Camera.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.Label_Camera.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Camera.setObjectName("Label_Camera")
        self.Label_Timer = QtWidgets.QLabel(self.ShotPage_Top)
        self.Label_Timer.setGeometry(QtCore.QRect(30, 40, 161, 201))
        font = QtGui.QFont()
        font.setFamily("Leferi Base Type Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Timer.setFont(font)
        self.Label_Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Timer.setObjectName("Label_Timer")
        self.TopStack.addWidget(self.ShotPage_Top)
        self.CheckPhoto = QtWidgets.QWidget()
        self.CheckPhoto.setObjectName("CheckPhoto")
        self.Top_Big_Photo = QtWidgets.QLabel(self.CheckPhoto)
        self.Top_Big_Photo.setGeometry(QtCore.QRect(240, 30, 800, 600))
        self.Top_Big_Photo.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.Top_Big_Photo.setAlignment(QtCore.Qt.AlignCenter)
        self.Top_Big_Photo.setObjectName("Top_Big_Photo")
        self.TopStack.addWidget(self.CheckPhoto)
        self.SuccessPage = QtWidgets.QWidget()
        self.SuccessPage.setObjectName("SuccessPage")
        self.PhotoPlusFrame = QtWidgets.QLabel(self.SuccessPage)
        self.PhotoPlusFrame.setGeometry(QtCore.QRect(200, 30, 900, 600))
        self.PhotoPlusFrame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PhotoPlusFrame.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.PhotoPlusFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.PhotoPlusFrame.setObjectName("PhotoPlusFrame")
        self.TopStack.addWidget(self.SuccessPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stack.setCurrentIndex(6)
        self.TopStack.setCurrentIndex(1)
        self.PoseStack.setCurrentIndex(0)
        self.NextBtn.clicked.connect(MainWindow.NextBottomButton_to_2) # type: ignore
        self.Btn1.clicked.connect(MainWindow.Press_Btn1) # type: ignore
        self.Btn2.clicked.connect(MainWindow.Press_Btn2) # type: ignore
        self.Btn3.clicked.connect(MainWindow.Press_Btn3) # type: ignore
        self.Btn4.clicked.connect(MainWindow.Press_Btn4) # type: ignore
        self.Btn5.clicked.connect(MainWindow.Press_Btn5) # type: ignore
        self.Btn6.clicked.connect(MainWindow.Press_Btn6) # type: ignore
        self.Btn_Already.clicked.connect(MainWindow.Press_PreparedBtn) # type: ignore
        self.Btn_Back_2.clicked.connect(MainWindow.Press_Back) # type: ignore
        self.NextBtn_3.clicked.connect(MainWindow.NextBottomButton_to_4) # type: ignore
        self.PrintBtn.clicked.connect(MainWindow.Press_Printing) # type: ignore
        self.ApplyBtn.clicked.connect(MainWindow.Press_Applying) # type: ignore
        self.Basic_Frame_1.clicked.connect(MainWindow.Press_BasicFrame1) # type: ignore
        self.Basic_Frame_2.clicked.connect(MainWindow.Press_BasicFrame2) # type: ignore
        self.Basic_Frame_3.clicked.connect(MainWindow.Press_BasicFrame3) # type: ignore
        self.Basic_Frame_4.clicked.connect(MainWindow.Press_BasicFrame4) # type: ignore
        self.Basic_Frame_5.clicked.connect(MainWindow.Press_BasicFrame5) # type: ignore
        self.Basic_Frame_6.clicked.connect(MainWindow.Press_BasicFrame6) # type: ignore
        self.Basic_Frame_7.clicked.connect(MainWindow.Press_BasicFrame7) # type: ignore
        self.Basic_Frame_8.clicked.connect(MainWindow.Press_BasicFrame8) # type: ignore
        self.RightBtn.clicked.connect(MainWindow.Press_RightBtn) # type: ignore
        self.LeftBtn.clicked.connect(MainWindow.Press_LeftBtn) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">터치하여 PhoRest를 시작해 보세요</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:400;\">촬영할 인원수를 선택해주세요</span></p></body></html>"))
        self.NextBtn.setText(_translate("MainWindow", "다음"))
        self.Btn3.setText(_translate("MainWindow", "3명"))
        self.Btn1.setText(_translate("MainWindow", "1명"))
        self.Btn2.setText(_translate("MainWindow", "2명"))
        self.Btn6.setText(_translate("MainWindow", "6명"))
        self.Btn5.setText(_translate("MainWindow", "5명"))
        self.Btn4.setText(_translate("MainWindow", "4명"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">버튼을 클릭하면 위쪽 화면에 추천 포즈가 나타납니다</span></p></body></html>"))
        self.Btn_Already.setText(_translate("MainWindow", "촬영 시작"))
        self.Btn_Back_2.setText(_translate("MainWindow", "뒤로"))
        self.Photo3.setText(_translate("MainWindow", "3"))
        self.Photo1.setText(_translate("MainWindow", "1"))
        self.Photo2.setText(_translate("MainWindow", "2"))
        self.Photo4.setText(_translate("MainWindow", "4"))
        self.NextBtn_3.setText(_translate("MainWindow", ">"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">사용할 프레임을 선택해주세요</span></p></body></html>"))
        self.PrintBtn.setText(_translate("MainWindow", "다음"))
        self.ApplyBtn.setText(_translate("MainWindow", "적용"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">더 많은 프레임 적용하기</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">프레임 번호를 입력 후 적용 버튼을 눌러주세요</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">이 화면 건너 뛰네;;</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">당신의 추억을 가져가세요</span></p></body></html>"))
        self.LeftBtn.setText(_translate("MainWindow", "<"))
        self.RightBtn.setText(_translate("MainWindow", ">"))
        self.PoseImg_1.setText(_translate("MainWindow", "포즈 이미지 1"))
        self.PoseImg_2.setText(_translate("MainWindow", "포즈 이미지 2"))
        self.PoseImg_3.setText(_translate("MainWindow", "포즈 이미지 3"))
        self.PoseImg_4.setText(_translate("MainWindow", "포즈 이미지 4"))
        self.PoseImg_5.setText(_translate("MainWindow", "포즈 이미지 5"))
        self.Label_Camera.setText(_translate("MainWindow", "카메라 화면 띄워줄 공간"))
        self.Label_Timer.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">15</span></p></body></html>"))
        self.Top_Big_Photo.setText(_translate("MainWindow", "이미지 크게 보여줄 공간"))
        self.PhotoPlusFrame.setText(_translate("MainWindow", "프레임 적용 이미지를 띄워줄 예정"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())