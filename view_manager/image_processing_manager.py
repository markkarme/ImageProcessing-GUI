from abc import get_cache_token
from PyQt5 import sip
from PyQt5.sip import delete
import cv2
import numpy as np
from PyQt5 import QtWidgets,QtCore,QtGui
# from  import Ui_MainWindow
from views import image_processing_view
from PyQt5.QtWidgets import QGraphicsDropShadowEffect,QSizeGrip,QFileDialog
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt,QPropertyAnimation
from view_manager.arithmetic_operations import PointOperations
from view_manager.two_image_process import TowImage
from view_manager.low_contrast_image import LowContrast
from view_manager.noisy_image_manager import NosiyImage
class ImageApp(image_processing_view.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # *******************set up UI**************** #
        self.setWindowTitle("Modern ui")
        QSizeGrip(self.size_grip)
        #close btn
        self.close_window_btn.clicked.connect(self.close)
        self.exit_btn.clicked.connect(self.close)
        #minmize btn
        self.minimize_window_btn.clicked.connect(self.showMinimized)
        #maxmim btn
        self.restore_btn.clicked.connect(self.restore_or_maxmize_window)
        self.header_frame.mouseMoveEvent = self.moveWindow
        self.open_close_slide_btn.clicked.connect(self.slide_left_menu)
        self.choose_image_btn.clicked.connect(self.get_image_path)
        self.OP_two_image_btn.clicked.connect(self.display_tow_image_page)
        self.OP_one_image_btn.clicked.connect(self.display_one_image_page)
        self.low_contrast_btn.clicked.connect(self.dislay_low_contrast_image_page)
        self.noisy_image_btn.clicked.connect(self.display_noisy_image_page)
        self.do_btn.clicked.connect(self.do_operation)
        self.go_btn.clicked.connect(self.go_operation)
        self.operation_com = ""
        self._operation = ""
        self._image_path = ""
        self.const_line = ""
        self.channel_com = ""
        self.main_profile_page = TowImage()
        self.two_layput.addWidget(self.main_profile_page)
        self.low = LowContrast()
        self.contras_layout.addWidget(self.low)
        self.noisy_page = NosiyImage()
        self.noisy_layout.addWidget(self.noisy_page)
        self.show()
    
    def display_one_image_page(self):
        self.stackedWidget.setCurrentIndex(1)
    def display_noisy_image_page(self):
        self.stackedWidget.setCurrentIndex(4)
    def display_tow_image_page(self):
        print("hi")
        self.stackedWidget.setCurrentIndex(0)
    def dislay_low_contrast_image_page(self):
        self.stackedWidget.setCurrentIndex(2)
    def get_image_path(self):
        self._image_path,_ = QFileDialog.getOpenFileName(self,"open file")
        self.before_lbl.setPixmap(QtGui.QPixmap(self._image_path))
        # self.after_lbl.setPixmap(QtGui.QPixmap(self._image_path))
    def do_operation(self):
        self._operation = self.choosen_operation_com.currentText()
        
        print(self._operation)
        if self._operation == "Arithmetic operations":
            if self.channel_com != "" :
                self.selected_layout.removeWidget(self.channel_com)
                sip.delete(self.channel_com)
                self.channel_com = ""
            if self.operation_com  == "":
                self.operation_com = QtWidgets.QComboBox()
                self.const_line = QtWidgets.QLineEdit()
                self.operation_com.addItems(["+","-","/","*","complement"])
                self.selected_layout.addWidget(self.operation_com)
                self.selected_layout.addWidget(self.const_line)
        elif self._operation == "Changing the image lighting color":
            if self.channel_com != "":
                self.selected_layout.removeWidget(self.channel_com)
                sip.delete(self.channel_com)
                self.channel_com = ""
            if self.operation_com  == "":
                self.operation_com = QtWidgets.QComboBox()
                self.const_line = QtWidgets.QLineEdit()
                self.operation_com.addItems(["+","-"])
                self.selected_layout.addWidget(self.operation_com)
                self.selected_layout.addWidget(self.const_line)
            if self.channel_com == "" :
                self.channel_com =QtWidgets.QComboBox()
                self.channel_com.addItems(["blue","green","red"])
                self.selected_layout.addWidget(self.channel_com)
        elif self._operation == "Swapping image channels":
            if self.channel_com != "":
                self.selected_layout.removeWidget(self.channel_com)
                sip.delete(self.channel_com)
                self.channel_com = ""
            self.get_channel_com(["swap Red with Green","swap Green with Blue","swap Blue with Red"])
        elif self._operation == "Eliminating color channels":
            choises = ["Eliminating Red","Eliminating Green","Eliminating Blue","Eliminating Red,Green","Eliminating Green,Blue","Eliminating Blue,Red"]
            if self.channel_com != "":
                self.selected_layout.removeWidget(self.channel_com)
                sip.delete(self.channel_com)
                self.channel_com = ""
            self.get_channel_com(choises)
        
    def get_channel_com(self,list):
        if self.operation_com != "":
            self.selected_layout.removeWidget(self.operation_com)
            sip.delete(self.operation_com)
            self.operation_com = ""
            self.selected_layout.removeWidget(self.const_line)
            sip.delete(self.const_line)
            self.const_line = ""
        if self.channel_com == "":
            self.channel_com =QtWidgets.QComboBox()
            self.channel_com.clear()
            self.channel_com.addItems(list)
            self.selected_layout.addWidget(self.channel_com)

                
            
    def go_operation(self):
        print(self._image_path)
        if self._operation == "Arithmetic operations":
            image = cv2.imread(self._image_path,0)
            rows , cols = image.shape #height , width
            PointOperations.arithmetic_operators(image,rows,cols,self.operation_com.currentText(),int(self.const_line.text()))
            # cv2.imshow("hello",image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
            self.after_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
        elif self._operation == "Changing the image lighting color":
            channel = self.channel_com.currentText()
            if channel == "blue":
                self.choose_channel(0)
            elif channel == "green":
                self.choose_channel(1)
            elif channel == "red":
                self.choose_channel(2)
        elif self._operation == "Swapping image channels":
            self.swapping_image_channels()
        elif self._operation == "Eliminating color channels":
            self.eliminating_color_channels()

    def eliminating_color_channels(self):
            channel = self.channel_com.currentText()
            image = cv2.imread(self._image_path,1)
            if channel == "Eliminating Red":
               image[:,:,2] = np.zeros([image.shape[0],image.shape[1]])
            elif channel == "Eliminating Blue":
                image[:,:,0] = np.zeros([image.shape[0],image.shape[1]])
            elif channel == "Eliminating Green":
                image[:,:,1] = np.zeros([image.shape[0],image.shape[1]])
            elif channel == "Eliminating Red,Green":
                image[:,:,1] = np.zeros([image.shape[0],image.shape[1]])
                image[:,:,2] = np.zeros([image.shape[0],image.shape[1]])
            elif channel == "Eliminating Green,Blue":
                image[:,:,1] = np.zeros([image.shape[0],image.shape[1]])
                image[:,:,0] = np.zeros([image.shape[0],image.shape[1]])
            elif channel == "Eliminating Blue,Red":
                image[:,:,0] = np.zeros([image.shape[0],image.shape[1]])
                image[:,:,2] = np.zeros([image.shape[0],image.shape[1]])
            
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
            self.after_lbl.setPixmap(QtGui.QPixmap.fromImage(image))

    def swapping_image_channels(self):
            channel = self.channel_com.currentText()
            image = cv2.imread(self._image_path,1)
            blue = image[:,:,0]
            green = image[:,:,1]
            red = image[:,:,2]
            if channel == "swap Red with Green":
                image[:,:,2] = green
            elif channel == "swap Green with Blue":
                image[:,:,1] = blue
            elif channel == "swap Blue with Red":
                image[:,:,0] = red
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
            self.after_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
    def choose_channel(self,channel_number):
        image = cv2.imread(self._image_path,1)
        blue = image[:,:,channel_number]
        blue_rows , blue_cols = blue.shape
        # print(image,blue_rows,blue_cols,self.operation_com.currentText(),int(self.const_line.text()))
        PointOperations.arithmetic_operators(blue,blue_rows,blue_cols,self.operation_com.currentText(),int(self.const_line.text()))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # cv2.imshow("hello",image)
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
        self.after_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
    def moveWindow(self,e):
        if self.isMaximized() == False:
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos()+e.globalPos()-self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
    def slide_left_menu(self):
        width = self.slide_menu_container.width()
        
        if width == 0:
            new_width = 220
            self.open_close_slide_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        else:
            new_width = 0
            self.open_close_slide_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))
        self.animation = QPropertyAnimation(self.slide_menu_container,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
    def restore_or_maxmize_window(self):
        if self.isMaximized():
            self.showNormal()
            #change icon
            self.restore_btn.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.restore_btn.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))
def test():
    app = QtWidgets.QApplication([])
    win_app = ImageApp()
    app.exec()

if __name__ =="__main__":
    test()