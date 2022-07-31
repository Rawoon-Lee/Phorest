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
        MainWindow.resize(879, 991)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stack = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack.setGeometry(QtCore.QRect(0, 480, 800, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setObjectName("stack")
        self.InitPage = QtWidgets.QWidget()
        self.InitPage.setObjectName("InitPage")
        self.label = QtWidgets.QLabel(self.InitPage)
        self.label.setGeometry(QtCore.QRect(180, 240, 451, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stack.addWidget(self.InitPage)
        self.ChoosePeoplePage = QtWidgets.QWidget()
        self.ChoosePeoplePage.setObjectName("ChoosePeoplePage")
        self.label_3 = QtWidgets.QLabel(self.ChoosePeoplePage)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 471, 71))
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.ChoosePeoplePage)
        self.line_2.setGeometry(QtCore.QRect(0, 160, 801, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.ChoosePeoplePage)
        self.label_4.setGeometry(QtCore.QRect(120, 120, 181, 41))
        self.label_4.setObjectName("label_4")
        self.NowPeople = QtWidgets.QLabel(self.ChoosePeoplePage)
        self.NowPeople.setGeometry(QtCore.QRect(320, 120, 41, 41))
        self.NowPeople.setObjectName("NowPeople")
        self.RecommandBtn = QtWidgets.QPushButton(self.ChoosePeoplePage)
        self.RecommandBtn.setGeometry(QtCore.QRect(570, 60, 101, 61))
        self.RecommandBtn.setObjectName("RecommandBtn")
        self.NextBtn = QtWidgets.QPushButton(self.ChoosePeoplePage)
        self.NextBtn.setGeometry(QtCore.QRect(700, 60, 61, 61))
        self.NextBtn.setStyleSheet("border-image:url(\'./nextImg.png\')")
        self.NextBtn.setText("")
        self.NextBtn.setObjectName("NextBtn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ChoosePeoplePage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 180, 781, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.Btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn3.sizePolicy().hasHeightForWidth())
        self.Btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn3.setFont(font)
        self.Btn3.setObjectName("Btn3")
        self.gridLayout.addWidget(self.Btn3, 0, 2, 1, 1)
        self.Btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn5.sizePolicy().hasHeightForWidth())
        self.Btn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn5.setFont(font)
        self.Btn5.setObjectName("Btn5")
        self.gridLayout.addWidget(self.Btn5, 1, 0, 1, 1)
        self.Btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Btn1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn1.sizePolicy().hasHeightForWidth())
        self.Btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn1.setFont(font)
        self.Btn1.setObjectName("Btn1")
        self.gridLayout.addWidget(self.Btn1, 0, 0, 1, 1)
        self.Btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn6.sizePolicy().hasHeightForWidth())
        self.Btn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn6.setFont(font)
        self.Btn6.setObjectName("Btn6")
        self.gridLayout.addWidget(self.Btn6, 1, 1, 1, 1)
        self.Btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn2.sizePolicy().hasHeightForWidth())
        self.Btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn2.setFont(font)
        self.Btn2.setObjectName("Btn2")
        self.gridLayout.addWidget(self.Btn2, 0, 1, 1, 1)
        self.Btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn4.sizePolicy().hasHeightForWidth())
        self.Btn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn4.setFont(font)
        self.Btn4.setObjectName("Btn4")
        self.gridLayout.addWidget(self.Btn4, 0, 3, 1, 1)
        self.Btn7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn7.sizePolicy().hasHeightForWidth())
        self.Btn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn7.setFont(font)
        self.Btn7.setObjectName("Btn7")
        self.gridLayout.addWidget(self.Btn7, 1, 2, 1, 1)
        self.Btn8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn8.sizePolicy().hasHeightForWidth())
        self.Btn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.Btn8.setFont(font)
        self.Btn8.setObjectName("Btn8")
        self.gridLayout.addWidget(self.Btn8, 1, 3, 1, 1)
        self.stack.addWidget(self.ChoosePeoplePage)
        self.ShotPage = QtWidgets.QWidget()
        self.ShotPage.setObjectName("ShotPage")
        self.Btn_Already = QtWidgets.QPushButton(self.ShotPage)
        self.Btn_Already.setGeometry(QtCore.QRect(240, 170, 311, 151))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.Btn_Already.setFont(font)
        self.Btn_Already.setAutoFillBackground(False)
        self.Btn_Already.setAutoDefault(False)
        self.Btn_Already.setDefault(False)
        self.Btn_Already.setFlat(False)
        self.Btn_Already.setObjectName("Btn_Already")
        self.Btn_Back_2 = QtWidgets.QPushButton(self.ShotPage)
        self.Btn_Back_2.setGeometry(QtCore.QRect(50, 40, 81, 71))
        self.Btn_Back_2.setStyleSheet("color: white;\n"
"background-color: rgb(58, 134, 255);\n"
"border-radius: 5px;")
        self.Btn_Back_2.setObjectName("Btn_Back_2")
        self.stack.addWidget(self.ShotPage)
        self.PhotoPage = QtWidgets.QWidget()
        self.PhotoPage.setObjectName("PhotoPage")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.PhotoPage)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 691, 461))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(45, 18, 43, 18)
        self.gridLayout_3.setHorizontalSpacing(70)
        self.gridLayout_3.setVerticalSpacing(25)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Photo3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Photo3.setStyleSheet("QLabel{\n"
"    border : 3px double #ABF760;\n"
"}")
        self.Photo3.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo3.setObjectName("Photo3")
        self.gridLayout_3.addWidget(self.Photo3, 1, 0, 1, 1)
        self.Photo1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Photo1.setStyleSheet("QLabel{\n"
"    border : 3px double #ABF760;\n"
"}")
        self.Photo1.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo1.setObjectName("Photo1")
        self.gridLayout_3.addWidget(self.Photo1, 0, 0, 1, 1)
        self.Photo2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Photo2.setStyleSheet("QLabel{\n"
"    border : 3px double #ABF760;\n"
"}")
        self.Photo2.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo2.setObjectName("Photo2")
        self.gridLayout_3.addWidget(self.Photo2, 0, 1, 1, 1)
        self.Photo4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Photo4.setStyleSheet("QLabel{\n"
"    border : 3px double #ABF760;\n"
"}")
        self.Photo4.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo4.setObjectName("Photo4")
        self.gridLayout_3.addWidget(self.Photo4, 1, 1, 1, 1)
        self.NextBtn_3 = QtWidgets.QPushButton(self.PhotoPage)
        self.NextBtn_3.setGeometry(QtCore.QRect(730, 410, 61, 61))
        self.NextBtn_3.setStyleSheet("border-image:url(\'./nextImg.png\')")
        self.NextBtn_3.setText("")
        self.NextBtn_3.setObjectName("NextBtn_3")
        self.label_2 = QtWidgets.QLabel(self.PhotoPage)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 691, 461))
        self.label_2.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.PhotoPage)
        self.line.setGeometry(QtCore.QRect(343, 10, 51, 461))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.PhotoPage)
        self.line_4.setGeometry(QtCore.QRect(20, 225, 691, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.stack.addWidget(self.PhotoPage)
        self.ChooseFramePage = QtWidgets.QWidget()
        self.ChooseFramePage.setObjectName("ChooseFramePage")
        self.label_5 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_5.setGeometry(QtCore.QRect(50, 50, 471, 71))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_6.setGeometry(QtCore.QRect(50, 110, 491, 31))
        self.label_6.setObjectName("label_6")
        self.line_3 = QtWidgets.QFrame(self.ChooseFramePage)
        self.line_3.setGeometry(QtCore.QRect(0, 160, 801, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.BottomFrameStack = QtWidgets.QStackedWidget(self.ChooseFramePage)
        self.BottomFrameStack.setGeometry(QtCore.QRect(30, 190, 621, 271))
        self.BottomFrameStack.setObjectName("BottomFrameStack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(70, 20, 481, 241))
        self.label_7.setStyleSheet("border-radious : 5%;\n"
"background-color : rgb(255, 255, 0);\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Frame_Next_Btn = QtWidgets.QPushButton(self.page)
        self.Frame_Next_Btn.setGeometry(QtCore.QRect(560, 200, 51, 61))
        self.Frame_Next_Btn.setStyleSheet("QPushButton{\n"
"    background: #00AE68;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #181818;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Frame_Next_Btn.setObjectName("Frame_Next_Btn")
        self.Frame_Prev_Btn = QtWidgets.QPushButton(self.page)
        self.Frame_Prev_Btn.setGeometry(QtCore.QRect(10, 200, 51, 61))
        self.Frame_Prev_Btn.setStyleSheet("QPushButton{\n"
"    background: #00AE68;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #181818;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Frame_Prev_Btn.setObjectName("Frame_Prev_Btn")
        self.BottomFrameStack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.BottomFrameStack.addWidget(self.page_2)
        self.label_8 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_8.setGeometry(QtCore.QRect(680, 200, 101, 111))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setIndent(0)
        self.label_8.setObjectName("label_8")
        self.PrintBtn = QtWidgets.QPushButton(self.ChooseFramePage)
        self.PrintBtn.setGeometry(QtCore.QRect(700, 380, 71, 71))
        self.PrintBtn.setStyleSheet("QPushButton{\n"
"    background: #00AE68;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #181818;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.PrintBtn.setObjectName("PrintBtn")
        self.ApplyBtn = QtWidgets.QPushButton(self.ChooseFramePage)
        self.ApplyBtn.setGeometry(QtCore.QRect(650, 100, 61, 51))
        self.ApplyBtn.setStyleSheet("QPushButton{\n"
"    background: #00AE68;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #181818;\n"
"    color: #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.ApplyBtn.setObjectName("ApplyBtn")
        self.lineEdit = QtWidgets.QLineEdit(self.ChooseFramePage)
        self.lineEdit.setGeometry(QtCore.QRect(600, 60, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(self.ChooseFramePage)
        self.label_9.setGeometry(QtCore.QRect(580, 30, 211, 31))
        self.label_9.setObjectName("label_9")
        self.stack.addWidget(self.ChooseFramePage)
        self.PrintingPage = QtWidgets.QWidget()
        self.PrintingPage.setObjectName("PrintingPage")
        self.label_10 = QtWidgets.QLabel(self.PrintingPage)
        self.label_10.setGeometry(QtCore.QRect(60, 150, 691, 161))
        self.label_10.setObjectName("label_10")
        self.stack.addWidget(self.PrintingPage)
        self.DonePrinting = QtWidgets.QWidget()
        self.DonePrinting.setObjectName("DonePrinting")
        self.label_11 = QtWidgets.QLabel(self.DonePrinting)
        self.label_11.setGeometry(QtCore.QRect(60, 130, 691, 211))
        self.label_11.setObjectName("label_11")
        self.stack.addWidget(self.DonePrinting)
        self.TopStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.TopStack.setGeometry(QtCore.QRect(0, 0, 800, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TopStack.sizePolicy().hasHeightForWidth())
        self.TopStack.setSizePolicy(sizePolicy)
        self.TopStack.setObjectName("TopStack")
        self.LogoPage = QtWidgets.QWidget()
        self.LogoPage.setObjectName("LogoPage")
        self.LogoImg = QtWidgets.QLabel(self.LogoPage)
        self.LogoImg.setGeometry(QtCore.QRect(290, 120, 200, 200))
        self.LogoImg.setStyleSheet("border-image:url(\'./logo.png\')")
        self.LogoImg.setText("")
        self.LogoImg.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoImg.setObjectName("LogoImg")
        self.TopStack.addWidget(self.LogoPage)
        self.RecommandPosePage = QtWidgets.QWidget()
        self.RecommandPosePage.setObjectName("RecommandPosePage")
        self.PoseImg = QtWidgets.QLabel(self.RecommandPosePage)
        self.PoseImg.setGeometry(QtCore.QRect(120, 20, 571, 431))
        self.PoseImg.setStyleSheet("QLabel{\n"
"    border : 3px double #ABF760;\n"
"}")
        self.PoseImg.setAlignment(QtCore.Qt.AlignCenter)
        self.PoseImg.setObjectName("PoseImg")
        self.LeftBtn = QtWidgets.QPushButton(self.RecommandPosePage)
        self.LeftBtn.setGeometry(QtCore.QRect(20, 380, 71, 71))
        self.LeftBtn.setObjectName("LeftBtn")
        self.RightBtn = QtWidgets.QPushButton(self.RecommandPosePage)
        self.RightBtn.setGeometry(QtCore.QRect(720, 380, 71, 71))
        self.RightBtn.setObjectName("RightBtn")
        self.TopStack.addWidget(self.RecommandPosePage)
        self.ShotPage_Top = QtWidgets.QWidget()
        self.ShotPage_Top.setObjectName("ShotPage_Top")
        self.Label_Camera = QtWidgets.QLabel(self.ShotPage_Top)
        self.Label_Camera.setGeometry(QtCore.QRect(180, 40, 561, 401))
        self.Label_Camera.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.Label_Camera.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Camera.setObjectName("Label_Camera")
        self.Label_Timer = QtWidgets.QLabel(self.ShotPage_Top)
        self.Label_Timer.setGeometry(QtCore.QRect(40, 40, 91, 141))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(36)
        self.Label_Timer.setFont(font)
        self.Label_Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Timer.setObjectName("Label_Timer")
        self.TopStack.addWidget(self.ShotPage_Top)
        self.CheckPhoto = QtWidgets.QWidget()
        self.CheckPhoto.setObjectName("CheckPhoto")
        self.Top_Big_Photo = QtWidgets.QLabel(self.CheckPhoto)
        self.Top_Big_Photo.setGeometry(QtCore.QRect(100, 20, 581, 431))
        self.Top_Big_Photo.setStyleSheet("QLabel{\n"
"    border : 3px solid black;\n"
"}")
        self.Top_Big_Photo.setAlignment(QtCore.Qt.AlignCenter)
        self.Top_Big_Photo.setObjectName("Top_Big_Photo")
        self.TopStack.addWidget(self.CheckPhoto)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.PhotoPlusFrame = QtWidgets.QLabel(self.page_3)
        self.PhotoPlusFrame.setGeometry(QtCore.QRect(100, 20, 581, 430))
        self.PhotoPlusFrame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PhotoPlusFrame.setStyleSheet("QLabel{\n"
"    border : 1px solid black;\n"
"}")
        self.PhotoPlusFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.PhotoPlusFrame.setObjectName("PhotoPlusFrame")
        self.TopStack.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stack.setCurrentIndex(3)
        self.TopStack.setCurrentIndex(4)
        self.RecommandBtn.clicked.connect(MainWindow.RecommandPose) # type: ignore
        self.NextBtn.clicked.connect(MainWindow.NextBottomButton_to_2) # type: ignore
        self.Btn1.clicked.connect(MainWindow.Press_Btn1) # type: ignore
        self.Btn2.clicked.connect(MainWindow.Press_Btn2) # type: ignore
        self.Btn3.clicked.connect(MainWindow.Press_Btn3) # type: ignore
        self.Btn4.clicked.connect(MainWindow.Press_Btn4) # type: ignore
        self.Btn5.clicked.connect(MainWindow.Press_Btn5) # type: ignore
        self.Btn6.clicked.connect(MainWindow.Press_Btn6) # type: ignore
        self.Btn7.clicked.connect(MainWindow.Press_Btn7) # type: ignore
        self.Btn8.clicked.connect(MainWindow.Press_Btn8) # type: ignore
        self.Btn_Already.clicked.connect(MainWindow.Press_PreparedBtn) # type: ignore
        self.Btn_Back_2.clicked.connect(MainWindow.Press_Back) # type: ignore
        self.NextBtn_3.clicked.connect(MainWindow.NextBottomButton_to_4) # type: ignore
        self.PrintBtn.clicked.connect(MainWindow.Press_Printing) # type: ignore
        self.ApplyBtn.clicked.connect(MainWindow.Press_Applying) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">터치하여 PhoRest를 시작해 보세요</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">촬영할 인원수를 선택해주세요</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">설정된 인원수 : </span></p></body></html>"))
        self.NowPeople.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">N명</span></p></body></html>"))
        self.RecommandBtn.setText(_translate("MainWindow", "추천 포즈"))
        self.Btn3.setText(_translate("MainWindow", "3명"))
        self.Btn5.setText(_translate("MainWindow", "5명"))
        self.Btn1.setText(_translate("MainWindow", "1명"))
        self.Btn6.setText(_translate("MainWindow", "6명"))
        self.Btn2.setText(_translate("MainWindow", "2명"))
        self.Btn4.setText(_translate("MainWindow", "4명"))
        self.Btn7.setText(_translate("MainWindow", "7명"))
        self.Btn8.setText(_translate("MainWindow", "8명"))
        self.Btn_Already.setText(_translate("MainWindow", "촬영 시작"))
        self.Btn_Back_2.setText(_translate("MainWindow", "뒤로"))
        self.Photo3.setText(_translate("MainWindow", "이미지 3"))
        self.Photo1.setText(_translate("MainWindow", "이미지 1"))
        self.Photo2.setText(_translate("MainWindow", "이미지 2"))
        self.Photo4.setText(_translate("MainWindow", "이미지 4"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">사용할 프레임을 선택해주세요</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">기본 프레임 외의 프레임을 사용하고 싶다면 고유 프레임 번호를 입력하세요 </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "기본 프레임 (2개씩 2~3장?)"))
        self.Frame_Next_Btn.setText(_translate("MainWindow", ">"))
        self.Frame_Prev_Btn.setText(_translate("MainWindow", "<"))
        self.label_8.setText(_translate("MainWindow", "QR코드"))
        self.PrintBtn.setText(_translate("MainWindow", "Print"))
        self.ApplyBtn.setText(_translate("MainWindow", "적용"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\"> 고유프레임 번호를 입력해주세요 </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">인쇄중 디자인 어케 꾸미징</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">인쇄중일땐 위에 프레임 사진 계속 띄워놓을예정</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">인쇄 끝나면 인쇄완료 창 띄우고<br/>아무곳이나 클릭시 처음 화면으로 돌아가기</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">인쇄 완료<br/><br/>아무곳이나 클릭시 되돌아가고</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">1분간 냅둬도 초기화면으로 돌아가게 구현해야징</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.PoseImg.setText(_translate("MainWindow", "포즈 이미지"))
        self.LeftBtn.setText(_translate("MainWindow", "왼쪽"))
        self.RightBtn.setText(_translate("MainWindow", "오른쪽"))
        self.Label_Camera.setText(_translate("MainWindow", "카메라 화면 띄워줄 공간"))
        self.Label_Timer.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">15</p></body></html>"))
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
