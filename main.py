from numpy.core.fromnumeric import mean
import qdarkstyle
from PyQt5 import QtWidgets,QtCore
from view_manager import ImageApp
from view_manager import TowImage
from view_manager import LowContrast
from view_manager import NosiyImage
def __Test__():
    app = QtWidgets.QApplication([])
    m = NosiyImage()
    m.show()
    app.exec_()
def __Test2__():
    app = QtWidgets.QApplication([])
    o = ImageApp()
    app.exec_()
if __name__ == "__main__":
    __Test2__()
   