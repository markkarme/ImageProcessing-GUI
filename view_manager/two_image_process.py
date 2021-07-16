from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from views import two_image_view
import cv2
from skimage import exposure
class TowImage(QtWidgets.QWidget,two_image_view.Ui_Form):
    def __init__(self):
        super(TowImage, self).__init__()
        self.setupUi(self)
        self.select_first_image_btn.clicked.connect(self.get_image1_path)
        self.select_second_image_btn.clicked.connect(self.get_image2_path)
        self.result_btn.clicked.connect(self.do_operation)
        self._image1_path = ""
        self._image2_path = ""
    def get_image1_path(self):
        self._image1_path,_ = QFileDialog.getOpenFileName(self,"open file")
        self.first_img_lbl.setPixmap(QtGui.QPixmap(self._image1_path))
    def get_image2_path(self):
        self._image2_path,_ = QFileDialog.getOpenFileName(self,"open file")
        self.second_img_lbl.setPixmap(QtGui.QPixmap(self._image2_path))
    def do_operation(self):
        image1 = cv2.imread(self._image1_path,1)
        image2 = cv2.imread(self._image2_path,1)
        image1 = cv2.resize(image1 ,(480,240))
        image2 = cv2.resize(image2 ,(480,240))
        operation = self.choose_operation_com.currentText()
        if operation == "+":
            image3 = image1 + image2
        elif operation == "-":
            image3 = image1 - image2
        elif operation == "*":
            image3 = image1 * image2
        elif operation == "/":
            image3 = image1 / image2
        elif operation == "XOR":
            image3 = cv2.bitwise_xor(image1, image2)
        elif operation == "OR":
            image3 = cv2.bitwise_or(image1, image2)
        elif operation == "AND":
            image3 = cv2.bitwise_and(image1, image2)
        elif operation == "NOT":
            image3 = cv2.bitwise_not(image1, image2)
        elif operation == "Diff":
            image3 = cv2.absdiff(image1, image2)
        elif operation == "Max":
            image3 = cv2.max(image1, image2)
        elif operation == "Min":
            image3 = cv2.min(image1, image2)
        elif operation == "Histogram Matching":
            src = cv2.imread(self._image1_path,1)
            ref = cv2.imread(self._image2_path,1)
            image3 = exposure.match_histograms(src, ref, multichannel=True)
        image = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0],QtGui.QImage.Format_RGB888)
        self.result_img_lbl.setPixmap(QtGui.QPixmap.fromImage(image))



def __Test__():
    app = QtWidgets.QApplication([])
    m = TowImage()
    m.show()
    app.exec_()
if __name__ == "__main__":
    __Test__()
