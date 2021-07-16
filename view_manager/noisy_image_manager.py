
from PyQt5 import QtWidgets, QtGui, QtCore, sip
from PyQt5.QtWidgets import QFileDialog
from numpy.core.fromnumeric import mean
from scipy.ndimage.measurements import median
from views import noisy_image_view
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from view_manager.arithmetic_operations import PointOperations
import cv2
from scipy.ndimage import generic_filter
from scipy import fftpack
from matplotlib.colors import LogNorm
from pylab import *

class NosiyImage(QtWidgets.QWidget,noisy_image_view.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choose_image_btn.clicked.connect(self.get_image_path)
        self.go_btn.clicked.connect(self.do_operation)
        self._image_path = ""
    def get_image_path(self):
        self._image_path,_ = QFileDialog.getOpenFileName(self,"open file")
        self.image_before_lbl.setPixmap(QtGui.QPixmap(self._image_path))
        
    def do_operation(self):
        image = cv2.imread(self._image_path,0)
        choose = self.operation_com.currentText()
        mask_size = self.mask_size_line.text()
        row = int(mask_size.split("*")[0])
        col = int(mask_size.split("*")[1])
        newImage = None
        if choose == "Neighbourhood operation Min Filter":
            newImage = generic_filter(image ,min , size=(row,col))
        elif choose == "Neighbourhood operation Max Filter":
            newImage = generic_filter(image ,max , size=(row,col))
        elif choose == "Neighbourhood operation Mean Filter":
            newImage = generic_filter(image ,mean , size=(row,col))
        elif choose == "Neighbourhood operation Median Filter":
            newImage = generic_filter(image ,median , size=(row,col))
        elif choose == "Smoothing Average operation":
            newImage = cv2.blur(image,(row,col))
        elif choose == "Smoothing Weighted Average operation":
            newImage = cv2.GaussianBlur(image,(row,col),sigmaY= 0 , sigmaX=0)
        elif choose == "Smoothing median filtering":
            newImage = cv2.medianBlur(image,row)
        elif choose == "laplacian filter":
            newImage = cv2.Laplacian(image,cv2.CV_8U,(row,col))
        elif choose == "outlier method":
            PointOperations.outlier_method(image,row)
            newImage = image
        elif choose == "image averaging":
            sum = 0
            for i in range(0,100):
                sum+=image
            newImage = sum/100
        elif choose == "Adaptive":
            PointOperations.Adaptive(image,row)
            newImage = image
        elif choose == "notch filter":
            img = cv2.imread(self._image_path,0)
            newImage = img
            img_fft = fftpack.fft2(img)
            plt.imshow(np.abs(img_fft), norm = LogNorm(200))
            plt.show()

        img = cv2.cvtColor(newImage, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(img.data, img.shape[1], img.shape[0],QtGui.QImage.Format_RGB888)
        self.image_after_lbl.setPixmap(QtGui.QPixmap.fromImage(img))
        

def __Test__():
    app = QtWidgets.QApplication([])
    m = NosiyImage
    m.show()
    app.exec_()
if __name__ =="__init__":
    __Test__()