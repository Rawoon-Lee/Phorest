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
import requests
import urllib.request
import json

stop_event = threading.Event()

class MainWindow(QMainWindow, Main_Ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.initImgs()

        # self.offset (몇번째 포즈를 받아올 것인지)
        self.offset_1 = 0
        self.offset_2 = 0
        self.offset_3 = 0
        self.offset_4 = 0
        self.offset_5 = 0
        self.offset_6 = 0
        self.ChooseBtnNum = 0

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
        # 프린팅이 완료됐는지를 판별하는 Flag
        self.Final_Flag = 0


        # frame color id 초기화
        self.Frame_Color_Id = "#FFFFFF"
        
        self.CurrentPhotoCnt = 0

        self.ShotPhoto_thread = threading.Thread(target=self.ShotPhoto)
        self.ShotPhoto_thread.setDaemon(True)
        self.RunCamera_thread = threading.Thread(target=self.Run_Camera)
        self.RunCamera_thread.setDaemon(True)
        self.lock = threading.Lock()
        
        # 카메라에서 시간초마다 사진을 찍게 하려면 별도 스레드에서 구현
        self.ShotPhoto_thread.start()
        self.RunCamera_thread.start()
        #stop_event.clear()

        self.show()

    def initImgs(self):
        self.offset_1 = 0
        self.offset_2 = 0
        self.offset_3 = 0
        self.offset_4 = 0
        self.offset_5 = 0
        self.offset_6 = 0
        self.ChooseBtnNum = 0

        # 이전에 이미지 라벨별로 저장했던 것들 초기화 해줘야함
        self.Photo1.clear()
        self.Photo2.clear()
        self.Photo3.clear()
        self.Photo4.clear()

        self.PoseImg_1.clear()
        self.PoseImg_2.clear()
        self.PoseImg_3.clear()
        self.PoseImg_4.clear()
        self.PoseImg_5.clear()

        self.Top_Big_Photo.clear()
        self.Label_Camera.clear()
        self.PhotoPlusFrame.clear()


    # 첫번째 화면에서는 어느 화면이던 클릭하면 두번째 화면으로 넘어간다
    def mousePressEvent(self, e):
        # 마우스 좌표 파악
        #print("Mouse Point : x={0},y={1}".format(e.x(), e.y()))
        if (self.stack.currentIndex() == 0):
            self.stack.setCurrentIndex(1)
            self.Btn1.setCheckable(True)
            self.Btn2.setCheckable(True)
            self.Btn3.setCheckable(True)
            self.Btn4.setCheckable(True)
            self.Btn5.setCheckable(True)
            self.Btn6.setCheckable(True)
            self.Btn1.setAutoExclusive(True)
            self.Btn2.setAutoExclusive(True)
            self.Btn3.setAutoExclusive(True)
            self.Btn4.setAutoExclusive(True)
            self.Btn5.setAutoExclusive(True)
            self.Btn6.setAutoExclusive(True)
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
        if (self.stack.currentIndex() == 6 and self.Final_Flag):
            self.Final_Flag = 0
            self.stack.setCurrentIndex(0)
            self.TopStack.setCurrentIndex(0)

    # ---------------------- 2. 인원 선택 칸 -----------------------
    # 두번째 화면에서는 각 버튼마다 이벤트 존재
    def RecommandPose(self):
        self.recommand_pose_flag = 1

        # 이미지 받아와서 띄워놓는 코드 작성
        # 이미지를 배열 형태 (json 형식) 으로 받아온다.

        limit = 5

        if self.ChooseBtnNum == 1:
            offset = self.offset_1
        elif self.ChooseBtnNum == 2:
            offset = self.offset_2
        elif self.ChooseBtnNum == 3:
            offset = self.offset_3
        elif self.ChooseBtnNum == 4:
            offset = self.offset_4
        elif self.ChooseBtnNum == 5:
            offset = self.offset_5
        elif self.ChooseBtnNum == 6:
            offset = self.offset_6


        params = {
            'limit' : limit,
            'offset' : offset,
            'human_count': self.ChooseBtnNum
        }
        #res = requests.post("https://i7a101.p.ssafy.io/api/download/photogroup/like", params=params)
        #print(res)
        #print(res.text)
        '''
        test = {'url':'http://t1.daumcdn.net/friends/prod/editor/dc8b3d02-a15a-4afa-a88b-989cf2a50476.jpg','url':'https://t1.daumcdn.net/cfile/tistory/24283C3858F778CA2E'}

        # 배열로 받아오면 이를 띄워줘야한다.
        pixmap = QPixmap(test[0]['url'])
        pixmap = pixmap.scaledToHeight(600)
        self.PoseImg_1.setPixmap(pixmap)

        pixmap = QPixmap(test[1]['url'])
        pixmap = pixmap.scaledToHeight(600)
        self.PoseImg_2.setPixmap(pixmap)
        '''

    # 좌우 버튼 누를때마다 백엔드에 계속 신호 보내줘야 한다.
    # 양 끝 일때 %5 == 0 이거나 %5 == 4이면 신호 보내주는 걸로 바꿔보자 그게 좀더 빠를듯
    # offset_n += 5의 형태
    def Press_RightBtn(self):
        nowIdx = self.PoseStack.currentIndex()
        nextIdx = nowIdx+1
        if(nextIdx == 5):
            nextIdx = 0
        self.PoseStack.setCurrentIndex(nextIdx)

    # 양 끝 일때 %5 == 0 이거나 %5 == 4이면 신호 보내주는 걸로 바꿔보자 그게 좀더 빠를듯
    # offset_n -= 5의 형태
    def Press_LeftBtn(self):
        nowIdx = self.PoseStack.currentIndex()
        nextIdx = nowIdx - 1
        if (nextIdx == -1):
            nextIdx = 4
        self.PoseStack.setCurrentIndex(nextIdx)

    def NextBottomButton_to_2(self):
        if (self.ChooseBtnNum != 0):
            self.stack.setCurrentIndex(2)

    def Press_Btn1(self):
        if self.ChooseBtnNum == 2:
            self.Btn2.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 3:
            self.Btn3.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 4:
            self.Btn4.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 5:
            self.Btn5.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 6:
            self.Btn6.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")

        self.ChooseBtnNum = 1

        self.Btn1.setStyleSheet("QPushButton{"
                                "color: #000000;"
                                "background-color: #FFE650;"
                                "padding: 12px;"
                                "border-bottom: 4px solid #FFC81E;"
                                "border-radius: 50%;"
                                "}")

        # 선택 후 첫번째 장 받아오고 다음 버튼 누를때마다 사진을 받아와?
        self.RecommandPose();
        self.PoseStack.setCurrentIndex(0)
        self.TopStack.setCurrentIndex(1)

    def Press_Btn2(self):
        if self.ChooseBtnNum == 1:
            self.Btn1.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 3:
            self.Btn3.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 4:
            self.Btn4.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 5:
            self.Btn5.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 6:
            self.Btn6.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")

        self.ChooseBtnNum = 2

        self.Btn2.setStyleSheet("QPushButton{"
                                "color: #000000;"
                                "background-color: #FFE650;"
                                "padding: 12px;"
                                "border-bottom: 4px solid #FFC81E;"
                                "border-radius: 50%;"
                                "}")

    def Press_Btn3(self):
        if self.ChooseBtnNum == 2:
            self.Btn2.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 1:
            self.Btn1.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 4:
            self.Btn4.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 5:
            self.Btn5.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 6:
            self.Btn6.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")

        self.ChooseBtnNum = 3

        self.Btn3.setStyleSheet("QPushButton{"
                                "color: #000000;"
                                "background-color: #FFE650;"
                                "padding: 12px;"
                                "border-bottom: 4px solid #FFC81E;"
                                "border-radius: 50%;"
                                "}")

    def Press_Btn4(self):
        if self.ChooseBtnNum == 2:
            self.Btn2.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 3:
            self.Btn3.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 1:
            self.Btn1.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 5:
            self.Btn5.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 6:
            self.Btn6.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")

        self.ChooseBtnNum = 4

        self.Btn4.setStyleSheet("QPushButton{"
                                "color: #000000;"
                                "background-color: #FFE650;"
                                "padding: 12px;"
                                "border-bottom: 4px solid #FFC81E;"
                                "border-radius: 50%;"
                                "}")

    def Press_Btn5(self):
        if self.ChooseBtnNum == 2:
            self.Btn2.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 3:
            self.Btn3.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 4:
            self.Btn4.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 1:
            self.Btn1.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 6:
            self.Btn6.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")

        self.ChooseBtnNum = 5

        self.Btn5.setStyleSheet("QPushButton{"
                                "color: #000000;"
                                "background-color: #FFE650;"
                                "padding: 12px;"
                                "border-bottom: 4px solid #FFC81E;"
                                "border-radius: 50%;"
                                "}")

    def Press_Btn6(self):
        if self.ChooseBtnNum == 2:
            self.Btn2.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 3:
            self.Btn3.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 4:
            self.Btn4.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 5:
            self.Btn5.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")
        elif self.ChooseBtnNum == 1:
            self.Btn1.setStyleSheet("QPushButton{"
                                    "color: #000000;"
                                    "background-color: #F8F8F8;"
                                    "padding: 12px;"
                                    "border-bottom: 4px solid #c8c8c8;"
                                    "border-radius: 50%;"
                                    "}")

        self.ChooseBtnNum = 6

        self.Btn6.setStyleSheet("QPushButton{"
                                "color: #000000;"
                                "background-color: #FFE650;"
                                "padding: 12px;"
                                "border-bottom: 4px solid #FFC81E;"
                                "border-radius: 50%;"
                                "}")



    # -------------------------- 3번째 촬영버튼 페이지 ------------------------------
    # 15초간의 타이머 작동
    def Press_PreparedBtn(self):
        self.CurrentPhotoCnt = 0
        
        # 먼저 촬영페이지의 넥스트 버튼 클릭 방지를 위해 Disable 처리
        self.NextBtn_3.setDisabled(True)
        self.NextBtn_3.hide()

        self.stack.setCurrentIndex(3)
        self.TopStack.setCurrentIndex(2)
        
        stop_event.set()

    def Run_Camera(self):
        while True:
            self.cap = cv2.VideoCapture(-1)
            # print("작동중?")
            #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            # print("width: {} height: {}".format(width,height))
            self.Label_Camera.resize(900, 600)

            while self.CurrentPhotoCnt < 4:
                stop_event.wait()
                ret, img = self.cap.read()
                if ret:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = cv2.flip(img, 1)
                    resize_img = cv2.resize(img, (900,600), interpolation=cv2.INTER_CUBIC)
                    h, w, c = resize_img.shape
                    qImg = QImage(resize_img.data, w, h, w * c, QImage.Format_RGB888)
                    Videopixmap = QPixmap.fromImage(qImg)
                    self.Label_Camera.setPixmap(Videopixmap)
                else:
                    print("cannot read camera")
                    break
            self.cap.release()

    # ----------------------------4번째 촬영 페이지---------------------------------
    def ShotPhoto(self):
        while True:
            stop_event.wait()
            # 타이머 작동
            self.StartTime = 5
            for num in range(1, 5):
                for i in range(self.StartTime, 0, -1):
                    self.Label_Timer.setText(str(i))
                    time.sleep(1)
                self.Label_Timer.setText("0")
                self.kimchi(num)
                self.CurrentPhotoCnt += 1

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
            stop_event.clear()
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

        # watermark
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
                      datemark)

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
        pass

        # 먼저 입력한 Frame_id를 서버에 보냄
        self.frame_id = self.Frame_Id.text()
        data = {
            'frame_id': self.frame_id
        }

        # 서버에 post 요청
        #res = requests.post("https://i7a101.p.ssafy.io/api/download", data=data)
        #print(res)
        # 리턴으로 res에 이미지 url을 담아서 보내줌
        #print(res.text)

        # 다운받을 이미지 url (res에서 받아오는 이미지 주소)
        # 일단 임시 url로 테스트
        url = "https://dispatch.cdnser.be/cms-content/uploads/2020/04/09/a26f4b7b-9769-49dd-aed3-b7067fbc5a8c.jpg"
        #url = res.text
        os.system("curl " + url + " > ./Frame/test.jpg")
        time.sleep(0.5)

        # 프레임이미지 리자이즈
        frame_img = Image.open('./Frame/test.jpg')
        frame_img = frame_img.resize((900,600))
        frame_img.save('./Frame/test.jpg')

        merged_img = Image.open('./photoDir/merged_img.png')
        merged_img = merged_img.resize((900,600))
        merged_img.save('./photoDir/new_merged_img.png')

        print ("됐나?")

        # 다운을 위한 시간 0.1s 추기


        # 받아온 사진을 사진과 합친다.
        FrameImg = Image.open('./Frame/test.jpg')
        img = Image.open('./photoDir/new_merged_img.png')
        FrameImg.paste(img, (0, 0), img)
        FrameImg = FrameImg.resize((900, 600))
        FrameImg.save('./FramePulsImg.png', 'PNG')
        pixmap = QPixmap('./FramePulsImg.png')
        self.PhotoPlusFrame.setPixmap(pixmap)


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
        self.TopStack.setCurrentIndex(0)
        self.stack.setCurrentIndex(6)
        print("print")
        # -------------------------- 6번째 인쇄중 출력 페이지 ------------------------------

        # 인쇄 하는 코드 넣기
        #os.system('lp -d epson -n {} ./FramePlusImg.png'.format(self.ChooseBtnNum))



        # 인쇄가 끝나면 업로드 코드 넣기
        '''
        img = open('./FramePulsImg.png','rb')
        files = {
            'image': img
        }

        data = {
            'human_count' : self.ChooseBtnNum
        }
        print(self.ChooseBtnNum)
        res = requests.post("http://i7a101.p.ssafy.io/api/upload/photogroup", files=files, data=data)
        
        # 여기서 받아온 res.text값을 바탕으로 qr코드를 작성
        
        '''
        print("성공")
        self.Final_Flag = 1
        self.initImgs()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
