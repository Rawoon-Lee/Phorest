import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
import Main_Ui
import time
import threading
import cv2
import os
from PIL import Image, ImageDraw, ImageFont
import datetime as dt
import qrcode

stop_event = threading.Event()

class MainWindow(QMainWindow, Main_Ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.initImgs()

        # recommand_pose_flag 초기화 0 : 안켜진상태 1 : 켜진상태
        self.recommand_pose_flag = 0

        # Stacked Widget을 처음 화면으로 돌리기
        self.stack.setCurrentIndex(0)
        self.TopStack.setCurrentIndex(0)

        # 마우스 클릭 이벤트 설정
        self.setMouseTracking(True)

        # 촬영버튼에 사용할 타이머기능 세팅
        self.timer = QTimer(self)
        self.timer.setInterval(1000)

        # 촬영화면에서 클릭 방지를 위해 flag변수 하나 채용
        self.Shot_Click_Flag = 0

        # frame color id 초기화
        self.Frame_Color_Id = "#FFFFFF"

        self.ShotPhoto_thread = threading.Thread(target=self.ShotPhoto)
        self.ShotPhoto_thread.setDaemon(True)
        self.RunCamera_thread = threading.Thread(target=self.Run_Camera)
        self.RunCamera_thread.setDaemon(True)
        self.lock = threading.Lock()

        self.show()

    def initImgs(self):
        # 이전에 이미지 라벨별로 저장했던 것들 초기화 해줘야함
        self.Photo1.clear()
        self.Photo2.clear()
        self.Photo3.clear()
        self.Photo4.clear()

        self.Top_Big_Photo.clear()
        self.Label_Camera.clear()

    # 첫번째 화면에서는 어느 화면이던 클릭하면 두번째 화면으로 넘어간다
    def mousePressEvent(self, e):
        # 마우스 좌표 파악
        print("Mouse Point : x={0},y={1}".format(e.x(), e.y()))
        if (self.stack.currentIndex() == 0):
            self.stack.setCurrentIndex(1)
            self.Btn1.setCheckable(True)
            self.Btn2.setCheckable(True)
            self.Btn3.setCheckable(True)
            self.Btn4.setCheckable(True)
            self.Btn5.setCheckable(True)
            self.Btn6.setCheckable(True)
            self.Btn7.setCheckable(True)
            self.Btn8.setCheckable(True)
            self.Btn1.setAutoExclusive(True)
            self.Btn2.setAutoExclusive(True)
            self.Btn3.setAutoExclusive(True)
            self.Btn4.setAutoExclusive(True)
            self.Btn5.setAutoExclusive(True)
            self.Btn6.setAutoExclusive(True)
            self.Btn7.setAutoExclusive(True)
            self.Btn8.setAutoExclusive(True)
            self.ChooseBtnNum = 0
        # 이미지 클릭시 크게 띄워줄것임
        if (self.stack.currentIndex() == 3 and self.TopStack.currentIndex() == 3 and self.Shot_Click_Flag):
            # 이미지1
            if (e.x() >= 67 and e.x() <= 544 and e.y() >= 752 and e.y() <= 1062):
                self.Top_Big_Photo.setStyleSheet("border-image:url('./photoDir/photo1.jpg')")
            elif (e.x() >= 615 and e.x() <= 1091 and e.y() >= 752 and e.y() <= 1062):
                self.Top_Big_Photo.setStyleSheet("border-image:url('./photoDir/photo2.jpg')")
            elif (e.x() >= 67 and e.x() <= 544 and e.y() >= 1112 and e.y() <= 1422):
                self.Top_Big_Photo.setStyleSheet("border-image:url('./photoDir/photo3.jpg')")
            elif (e.x() >= 615 and e.x() <= 1091 and e.y() >= 1112 and e.y() <= 1422):
                self.Top_Big_Photo.setStyleSheet("border-image:url('./photoDir/photo4.jpg')")

        # 마지막 인쇄 완료 페이지
        if (self.stack.currentIndex() == 6):
            self.stack.setCurrentIndex(0)
            self.TopStack.setCurrentIndex(0)

    # ---------------------- 2. 인원 선택 칸 -----------------------
    # 두번째 화면에서는 각 버튼마다 이벤트 존재
    def RecommandPose(self):
        if (self.recommand_pose_flag == 1):
            self.recommand_pose_flag = 0
            self.TopStack.setCurrentIndex(0)
        else:
            self.recommand_pose_flag = 1
            self.NowPeople.setText(self.NowPeople.text())
            # 이미지 받아와서 띄워놓는 코드 작성

            self.TopStack.setCurrentIndex(1)

    def NextBottomButton_to_2(self):
        if (self.ChooseBtnNum != 0):
            self.stack.setCurrentIndex(2)

    def Press_Btn1(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">1명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">1명</span></p></body></html>"))
            if self.ChooseBtnNum == 2:
                self.Btn2.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 3:
                self.Btn3.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 4:
                self.Btn4.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 5:
                self.Btn5.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 6:
                self.Btn6.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 7:
                self.Btn7.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 8:
                self.Btn8.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 1

            self.Btn1.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_Btn2(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">2명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">2명</span></p></body></html>"))

            if self.ChooseBtnNum == 1:
                self.Btn1.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 3:
                self.Btn3.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 4:
                self.Btn4.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 5:
                self.Btn5.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 6:
                self.Btn6.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 7:
                self.Btn7.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 8:
                self.Btn8.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 2

            self.Btn2.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_Btn3(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">3명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">3명</span></p></body></html>"))

            if self.ChooseBtnNum == 1:
                self.Btn1.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 2:
                self.Btn2.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 4:
                self.Btn4.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 5:
                self.Btn5.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 6:
                self.Btn6.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 7:
                self.Btn7.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 8:
                self.Btn8.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 3

            self.Btn3.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_Btn4(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">4명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">4명</span></p></body></html>"))

            if self.ChooseBtnNum == 1:
                self.Btn1.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 3:
                self.Btn3.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 2:
                self.Btn2.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 5:
                self.Btn5.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 6:
                self.Btn6.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 7:
                self.Btn7.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 8:
                self.Btn8.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 4

            self.Btn4.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_Btn5(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">5명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">5명</span></p></body></html>"))

            if self.ChooseBtnNum == 1:
                self.Btn1.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 3:
                self.Btn3.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 4:
                self.Btn4.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 2:
                self.Btn2.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 6:
                self.Btn6.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 7:
                self.Btn7.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 8:
                self.Btn8.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 5

            self.Btn5.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_Btn6(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">6명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">6명</span></p></body></html>"))

            if self.ChooseBtnNum == 1:
                self.Btn1.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 3:
                self.Btn3.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 4:
                self.Btn4.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 5:
                self.Btn5.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 2:
                self.Btn2.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 7:
                self.Btn7.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 8:
                self.Btn8.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 6

            self.Btn6.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_Btn7(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">7명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">7명</span></p></body></html>"))

            if self.ChooseBtnNum == 1:
                self.Btn1.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 3:
                self.Btn3.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 4:
                self.Btn4.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 5:
                self.Btn5.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 6:
                self.Btn6.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 2:
                self.Btn2.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 8:
                self.Btn8.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 7

            self.Btn7.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_Btn8(self):
        if (self.recommand_pose_flag == 0):
            _translate = QtCore.QCoreApplication.translate
            self.NowPeople.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">8명</span></p></body></html>"))
            self.NowPeople_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">8명</span></p></body></html>"))

            if self.ChooseBtnNum == 1:
                self.Btn1.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 3:
                self.Btn3.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 4:
                self.Btn4.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 5:
                self.Btn5.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 6:
                self.Btn6.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 7:
                self.Btn7.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")
            elif self.ChooseBtnNum == 2:
                self.Btn2.setStyleSheet("QPushButton{"
                                        "color: #FF8200;"
                                        "background-color: #FFE650		;"
                                        "padding: 12px;"
                                        "border-radius: 4px;"
                                        "border-bottom: 4px solid #FFC81E;"
                                        "border-radius: 20px;"
                                        "}")

            self.ChooseBtnNum = 8

            self.Btn8.setStyleSheet("QPushButton{"
                                    "color: white;"
                                    "background-color: #FFB937		;"
                                    "padding: 12px;"
                                    "border-radius: 4px;"
                                    "border-bottom: 4px solid #FF8200;"
                                    "border-radius: 20px;"
                                    "}")

    def Press_CloseBtn(self):
        self.recommand_pose_flag = 0
        self.TopStack.setCurrentIndex(0)

    # -------------------------- 3번째 촬영버튼 페이지 ------------------------------
    # 15초간의 타이머 작동
    def Press_PreparedBtn(self):
        self.CurrentPhotoCnt = 0

        # 먼저 촬영페이지의 넥스트 버튼 클릭 방지를 위해 Disable 처리
        self.NextBtn_3.setDisabled(True)
        self.NextBtn_3.hide()

        self.stack.setCurrentIndex(3)
        self.TopStack.setCurrentIndex(2)

        # 카메라에서 시간초마다 사진을 찍게 하려면 별도 스레드에서 구현
        self.ShotPhoto_thread.start()
        self.RunCamera_thread.start()

    def Run_Camera(self):
        self.cap = cv2.VideoCapture(0)
        # print("작동중?")
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        # print("width: {} height: {}".format(width,height))
        self.Label_Camera.resize(900, 600)

        while self.CurrentPhotoCnt < 4:
            stop_event.wait()
            ret, img = self.cap.read()
            if ret:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.flip(img, 1)
                h, w, c = img.shape
                qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
                Videopixmap = QPixmap.fromImage(qImg)
                self.Label_Camera.setPixmap(Videopixmap)
            else:
                print("cannot read camera")
                break
        self.cap.release()

    # ----------------------------4번째 촬영 페이지---------------------------------
    def ShotPhoto(self):
        stop_event.set()
        # 타이머 작동
        self.StartTime = 5
        for num in range(1, 5):
            for i in range(self.StartTime, 0, -1):
                self.Label_Timer.setText(str(i))
                time.sleep(1)
            self.Label_Timer.setText("0")
            self.kimchi(num)
            self.CurrentPhotoCnt += 1

            # 사진을 찍는 신호 보냄
            # 그러면 다른 스레드에서 신호가 오면 사진을 찍고 flag 다시 원래대로 돌려놓음
            # 사진을 찍을 때 애니메이션 기능을 넣어서 사용자가 사진이 찍힌건지 확인 가능해야한다.
            # 이때 파일경로 마지막 파일명은 "photo{}".format(self.CurrentPhotoCnt+1)"
            # self.CurrentPhotoCnt 가 3이면 찍고, 0으로 돌려놓음
            # 사진이 저장되는 시간을 확보하기 위해서 3초간의 sleep을 둠
            # time.sleep(1)

            pixmap = QPixmap("./photoDir/photo{}".format(num))
            pixmap = pixmap.scaledToHeight(300)
            if (num == 1):
                self.Photo1.setPixmap(pixmap)
            elif (num == 2):
                self.Photo2.setPixmap(pixmap)
            elif (num == 3):
                self.Photo3.setPixmap(pixmap)
            elif (num == 4):
                self.Photo4.setPixmap(pixmap)

            stop_event.set()

        # 다 찍었으면 TopPage 다음페이지로, 넥스트 버튼 나타나게
        self.Shot_Click_Flag = 1
        self.NextBtn_3.setEnabled(True)
        self.NextBtn_3.setVisible(True)
        self.Top_Big_Photo.setStyleSheet("border-image:url('./photoDir/photo1.jpg')")
        self.TopStack.setCurrentIndex(3)

        self.make_image()
        time.sleep(1)

    def make_image(self):
        img1 = Image.open("./photoDir/photo1.jpg")
        img2 = Image.open("./photoDir/photo2.jpg")
        img3 = Image.open("./photoDir/photo3.jpg")
        img4 = Image.open("./photoDir/photo4.jpg")

        img_size = (600, 425)

        img1 = img1.resize(img_size)
        img2 = img2.resize(img_size)
        img3 = img3.resize(img_size)
        img4 = img4.resize(img_size)

        new_img = Image.new("RGBA", (1500, 1000), (0, 0, 0, 0))
        new_img.paste(img1, (50, 50))
        new_img.paste(img2, (img_size[0] + 100, 50))
        new_img.paste(img3, (50, img_size[1] + 100))
        new_img.paste(img4, (img_size[0] + 100, img_size[1] + 100))

        # make QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=2,
            border=1
        )

        url = 'http://i7a101.p.ssafy.io/api/frame/'
        qr.add_data(url)
        qr.make()
        qrimg = qr.make_image(fill_color='black', back_color='white')
        qrimg.save('./photoDir/QRCodeImg.jpg')

        QRcode = Image.open("./photoDir/QRCodeImg.jpg")
        QRcode = qrimg.resize((130, 130))
        new_img.paste(QRcode, ((img_size[0] * 2) + 100 + 10, 1000 - 50 - 130))

        '''# watermark
        waterFont = ImageFont.truetype('./703.ttf', 60)
        mark_width, mark_height = waterFont.getsize('PhoRest')
        watermark = Image.new('RGBA', (mark_width, mark_height), (0, 0, 0, 0))
        waterdraw = ImageDraw.Draw(watermark)
        waterdraw.text((0, 0), 'PhoRest', fill='black', font=waterFont, align='center')
        watermark = watermark.rotate(90, expand=1)

        new_img.paste(watermark, ((img_size[0] * 2) + 100 + 10, 1000 - 50 - 130 - 20 - mark_width), watermark)

        # datestr
        time = dt.datetime.now()
        datestr = time.strftime('%Y/%m/%d')
        dateFont = ImageFont.truetype('./703.ttf', 30)
        date_width, date_height = dateFont.getsize(datestr)
        datemark = Image.new('RGBA', (date_width, date_height), (0, 0, 0, 0))
        datedraw = ImageDraw.Draw(datemark)
        datedraw.text((0, 0), datestr, fill='black', font=dateFont, align='center')
        datemark = datemark.rotate(90, expand=1)

        new_img.paste(datemark, ((img_size[0] * 2) + 100 + 10 + mark_height + 10, 1000 - 50 - 130 - 20 - date_width),
                      datemark)'''

        new_img.save("./photoDir/merged_img.png", "PNG")

    def kimchi(self, num):
        self.lock.acquire()
        self.TopStack.setStyleSheet("background-color : #FFFFFF")
        ret, img = self.cap.read()
        img = cv2.flip(img, 1)
        cv2.imwrite('./photoDir/photo{}.jpg'.format(num), img)

        stop_event.clear()

        time.sleep(0.5)
        self.TopStack.setStyleSheet("background-color : #FFF7E7")
        time.sleep(0.5)
        self.stack.setStyleSheet("background-color : #FFF7E7")
        time.sleep(0.5)
        print("Kimchi")
        self.lock.release()
        time.sleep(1)

    def NextBottomButton_to_4(self):
        self.stack.setCurrentIndex(4)
        self.TopStack.setCurrentIndex(4)

    def Press_Back(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() - 1)

    # -------------------------- 5번째 프레임 선택 페이지 ------------------------------

    # 프레임까지 적용하여 화면에 띄워주는 버튼
    def Press_Applying(self):
        print("Apply")

    def make_Frame_Img(self, num):
        FrameImg = Image.open('./Frame/Frame_{}.jpg'.format(num))
        img = Image.open('./photoDir/merged_img.png')
        FrameImg.paste(img, (0, 0), img)
        FrameImg = FrameImg.resize((900, 600))
        FrameImg.save('./FramePulsImg.png', 'PNG')
        pixmap = QPixmap('./FramePulsImg.png')
        self.PhotoPlusFrame.setPixmap(pixmap)

    # 프레임 컬러 선택 버튼
    def Press_BasicFrame1(self):
        self.Frame_Color_Id = "#FFFFFF"
        self.make_Frame_Img(1)

    def Press_BasicFrame2(self):
        self.Frame_Color_Id = "#D2D2FF"
        self.make_Frame_Img(2)

    def Press_BasicFrame3(self):
        self.Frame_Color_Id = "#32F1FF"
        self.make_Frame_Img(3)

    def Press_BasicFrame4(self):
        self.Frame_Color_Id = "#FFD4DF"
        self.make_Frame_Img(4)

    def Press_BasicFrame5(self):
        self.Frame_Color_Id = "#FAFAA0"
        self.make_Frame_Img(5)

    def Press_BasicFrame6(self):
        self.Frame_Color_Id = "#957745"
        self.make_Frame_Img(6)

    def Press_BasicFrame7(self):
        self.Frame_Color_Id = "#8c8c8c"
        self.make_Frame_Img(7)

    def Press_BasicFrame8(self):
        self.Frame_Color_Id = "#94EB3E"
        self.make_Frame_Img(8)

    # 프린트 버튼
    def Press_Printing(self):
        print("print")
        self.stack.setCurrentIndex(5)

        # -------------------------- 6번째 인쇄중 출력 페이지 ------------------------------
        # 이곳에는 프린트가 출력이 완료되는 신호를 받는다면 다음 장면으로 넘겨준다
        print("Now Printing")
        time.sleep(4)

        # 임시로 1초후 넘어가게 일단은 구현
        time.sleep(0.1)
        self.stack.setCurrentIndex(6)

        # -------------------------- 7번째 인쇄 완료 페이지 --------------------------------
        self.initImgs()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")