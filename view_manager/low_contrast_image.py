
from PyQt5 import QtWidgets, QtGui, QtCore, sip
from PyQt5.QtWidgets import QFileDialog
from views import low_contrast_view
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from view_manager.arithmetic_operations import PointOperations

import cv2
import matplotlib.pyplot as plt

class LowContrast(QtWidgets.QWidget,low_contrast_view.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.figure = plt.figure()
        self.figure2 = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas2 = FigureCanvas(self.figure2)
        self.choose_image_btn.clicked.connect(self.get_image_path)
        self._image_path = ""
        self.before_plt_layout.addWidget(self.canvas)
        self.after_plt_layout.addWidget(self.canvas2)
        
        self.do_btn.clicked.connect(self.do_operation)
        self.go_btn.clicked.connect(self.go_operation)
        self.op = None
        self.operation = ""
        self.low_cont_img = None
        self.const_line = None
    def do_operation(self):
        self.operation = self.operation_com.currentText()
        if self.operation == "Look-up table":
            if self.const_line != None:
                self.tools_layout.removeWidget(self.op)
                sip.delete(self.op)
                self.op = None
                self.tools_layout.removeWidget(self.const_line)
                sip.delete(self.const_line)
                self.const_line = None
            if self.op != None:
                self.tools_layout.removeWidget(self.op)
                sip.delete(self.op)
                self.op = None
            self.op = QtWidgets.QComboBox()
            ls = ["COLORMAP_AUTUMN","COLORMAP_BONE","COLORMAP_JET","COLORMAP_WINTER","COLORMAP_RAINBOW","COLORMAP_OCEAN "]
            self.op.addItems(ls)
            self.tools_layout.addWidget(self.op)
        elif self.operation == "Histogram Stretching":
            if self.op != None:
                self.tools_layout.removeWidget(self.op)
                sip.delete(self.op)
                self.op = None
            if self.const_line != None:
                self.tools_layout.removeWidget(self.const_line)
                sip.delete(self.const_line)
                self.const_line = None
            self.op = QtWidgets.QComboBox()
            self.const_line = QtWidgets.QLineEdit()
            self.op.addItems(["multiplication function","Gamma correction function","Stretching function"])
            self.tools_layout.addWidget(self.op)
            self.tools_layout.addWidget(self.const_line)
        elif self.operation == "Histogram Equalization":
            img = cv2.imread(self._image_path,0)
            newImg = cv2.equalizeHist(img)
            image = cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
            self.after_img_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
            self.display_plt(newImg)
    def go_operation(self):
        if self.operation == "Look-up table":
            img = cv2.imread(self._image_path,0)
            choice = self.op.currentIndex()
            newImg = cv2.applyColorMap(img,choice)
            image = cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
            self.after_img_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
            self.display_plt(newImg)
        elif self.operation == "Histogram Stretching":
            function = self.op.currentIndex()
            if function == 0:
                img = cv2.imread(self._image_path,0)
                rows,cols = img.shape
                PointOperations.low_constract_operation(img,rows,cols,"*",float(self.const_line.text()))
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
                self.after_img_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
                self.display_plt(img)
            elif function == 1:
                img = cv2.imread(self._image_path,0)
                rows,cols = img.shape
                PointOperations.low_constract_operation(img,rows,cols,"**",float(self.const_line.text()))
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
                self.after_img_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
                self.display_plt(img)
            elif function == 2:
                img = cv2.imread(self._image_path,0)
                rows,cols = img.shape
                pixels = self.const_line.text().split(" ")
                PointOperations.stretching_function(img,rows,cols,float(pixels[0]),float(pixels[1]))
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
                self.after_img_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
                self.display_plt(img)

            
    def display_plt(self,img):
        data = img.ravel()
        self.figure2.clear()
        ax = self.figure2.add_subplot(111)
        ax.hist(data)
        self.canvas2.draw()
    def get_image_path(self):
        self._image_path,_ = QFileDialog.getOpenFileName(self,"open file")
        self.before_img_lbl.setPixmap(QtGui.QPixmap(self._image_path))
        self.low_cont_img = cv2.imread(self._image_path,0)
        
        data = self.low_cont_img.ravel()
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.hist(data)
        self.canvas.draw()


def __Test__():
    app = QtWidgets.QApplication([])
    m = LowContrast()
    m.show()
    app.exec_()
if __name__ =="__init__":
    __Test__()