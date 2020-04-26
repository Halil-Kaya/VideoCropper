

from PyQt5.QtWidgets import QFileDialog


from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
import sys
import os

class Ui_Form(object):
    def setupUi(self, Form):
        self.videoKapat = False
        self.videoDur = False
        self.bisi = 1


        Form.setObjectName("Form")
        Form.resize(586, 528)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-30, 0, 671, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 90, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 70, 90, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 70, 90, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 70, 90, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 130, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(90, 220, 71, 16))
        self.label_4.setObjectName("label_4")
        self.baslangic = QtWidgets.QTextEdit(self.frame)
        self.baslangic.setGeometry(QtCore.QRect(170, 220, 81, 20))
        self.baslangic.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(310, 220, 58, 16))
        self.label_5.setObjectName("label_5")
        self.bitis = QtWidgets.QTextEdit(self.frame)
        self.bitis.setGeometry(QtCore.QRect(360, 220, 111, 21))
        self.bitis.setObjectName("textEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 470, 131, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 440, 391, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 40, 191, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.grayRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.grayRadioBtn.setGeometry(QtCore.QRect(60, 340, 104, 21))
        self.grayRadioBtn.setObjectName("radioButton")
        self.hsvRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.hsvRadioBtn.setGeometry(QtCore.QRect(130, 340, 104, 21))
        self.hsvRadioBtn.setObjectName("radioButton_2")
        self.normalRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.normalRadioBtn.setGeometry(QtCore.QRect(190, 340, 104, 21))
        self.normalRadioBtn.setObjectName("radioButton_3")
        self.hlsRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.hlsRadioBtn.setGeometry(QtCore.QRect(280, 340, 61, 21))
        self.hlsRadioBtn.setObjectName("radioButton_4")
        self.labRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.labRadioBtn.setGeometry(QtCore.QRect(340, 340, 61, 21))
        self.labRadioBtn.setObjectName("radioButton_5")
        self.luvRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.luvRadioBtn.setGeometry(QtCore.QRect(410, 340, 61, 21))
        self.luvRadioBtn.setObjectName("radioButton_6")
        self.rgbRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.rgbRadioBtn.setGeometry(QtCore.QRect(470, 340, 61, 21))
        self.rgbRadioBtn.setObjectName("radioButton_7")
        self.yuvRadioBtn = QtWidgets.QRadioButton(self.frame)
        self.yuvRadioBtn.setGeometry(QtCore.QRect(530, 340, 61, 21))
        self.yuvRadioBtn.setObjectName("radioButton_8")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(250, 410, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Video Seç"))
        self.pushButton_2.setText(_translate("Form", "Play"))
        self.pushButton_3.setText(_translate("Form", "Pause"))
        self.pushButton_4.setText(_translate("Form", "Stop"))
        self.pushButton_5.setText(_translate("Form", "Videoyu Kaydet"))
        self.pushButton_6.setText(_translate("Form", "Videoyu Baslat"))

        self.pushButton.clicked.connect(self.VideoSec)
        self.pushButton_2.clicked.connect(self.Play)
        self.pushButton_3.clicked.connect(self.Pause)
        self.pushButton_4.clicked.connect(self.Stop)
        self.pushButton_5.clicked.connect(self.SaveVideo)
        self.pushButton_6.clicked.connect(self.PlayVideo)


        self.label.setText(_translate("Form", "Fps: "))
        self.label_2.setText(_translate("Form", "Video Süresi:"))
        self.label_3.setText(_translate("Form", "Toplam Frame:"))
        self.label_4.setText(_translate("Form", "Başlangıç: "))
        self.label_5.setText(_translate("Form", "Bitiş:"))




        self.grayRadioBtn.setText(_translate("Form", "GRAY"))
        self.hsvRadioBtn.setText(_translate("Form", "HSV"))
        self.normalRadioBtn.setText(_translate("Form", "NORMAL"))
        self.hlsRadioBtn.setText(_translate("Form", "HLS"))
        self.labRadioBtn.setText(_translate("Form", "LAB"))
        self.luvRadioBtn.setText(_translate("Form", "LUV"))
        self.rgbRadioBtn.setText(_translate("Form", "RGB"))
        self.yuvRadioBtn.setText(_translate("Form", "YUV"))
        self.label_6.setText(_translate("Form", "Video ismi"))

        self.normalRadioBtn.setChecked(True)


    def PlayVideo(self):
            self.videoKapat = False
            self.videoDur = False



            video = cv2.VideoCapture(self.dosyaPath[0])
            _translate = QtCore.QCoreApplication.translate
            self.fps = video.get(cv2.CAP_PROP_FPS)
            self.frameSayisi = video.get(cv2.CAP_PROP_FRAME_COUNT)
            self.vidonunSuresi = float(self.frameSayisi) / float(self.fps)

            labelFps = "Fps: " + str(self.fps)
            labelVideoSuresi = "Video Süresi: " + str(self.vidonunSuresi)
            labelToplamFrame = "Toplam Frame: " + str(self.frameSayisi)

            self.label.setText(_translate("Form", labelFps))
            self.label_2.setText(_translate("Form", labelVideoSuresi))
            self.label_3.setText(_translate("Form", labelToplamFrame))

            self.baslangic.setText("0")
            self.bitis.setText(str( int(self.vidonunSuresi) ))



            while True:

                if self.videoKapat == True:
                    break

                if self.videoDur == False:

                    deger, frame = video.read()

                    if deger == True:

                        if self.normalRadioBtn.isChecked():
                            pass
                        elif self.grayRadioBtn.isChecked():
                            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

                        elif self.hsvRadioBtn.isChecked():
                            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

                        elif self.hlsRadioBtn.isChecked():
                            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)

                        elif self.labRadioBtn.isChecked():
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

                        elif self.luvRadioBtn.isChecked():
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)

                        elif self.rgbRadioBtn.isChecked():
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                        elif self.yuvRadioBtn.isChecked():
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)


                        frame = cv2.resize(frame, (500, 350))

                        cv2.imshow("Video", frame)
                        cv2.moveWindow("Video", 20, 20)



                    else:
                        break

                cv2.waitKey(int(self.fps))




            video.release()
            cv2.destroyAllWindows()




    def Play(self):
        self.videoDur = False
        self.bisi = 30


    def VideoSec(self):
        self.dosyaPath = QFileDialog.getOpenFileName(None, "Dosya Aç", os.getenv("HOME"))
        print(self.dosyaPath)

    def Stop(self):
        self.videoKapat = True
        pass

    def Pause(self):
        self.videoDur = True
        pass

    def SaveVideo(self):
        print("save video")
        self.filePath = QFileDialog.getExistingDirectory(None, "Get Any File")




app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())