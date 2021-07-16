# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/two_image_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(729, 415)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.first_img_lbl = QtWidgets.QLabel(Form)
        self.first_img_lbl.setMaximumSize(QtCore.QSize(500, 500))
        self.first_img_lbl.setScaledContents(True)
        self.first_img_lbl.setObjectName("first_img_lbl")
        self.verticalLayout.addWidget(self.first_img_lbl, 0, QtCore.Qt.AlignTop)
        self.select_first_image_btn = QtWidgets.QPushButton(Form)
        self.select_first_image_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.select_first_image_btn.setObjectName("select_first_image_btn")
        self.verticalLayout.addWidget(self.select_first_image_btn, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.second_img_lbl = QtWidgets.QLabel(Form)
        self.second_img_lbl.setMaximumSize(QtCore.QSize(500, 500))
        self.second_img_lbl.setScaledContents(True)
        self.second_img_lbl.setObjectName("second_img_lbl")
        self.verticalLayout_2.addWidget(self.second_img_lbl, 0, QtCore.Qt.AlignTop)
        self.select_second_image_btn = QtWidgets.QPushButton(Form)
        self.select_second_image_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.select_second_image_btn.setObjectName("select_second_image_btn")
        self.verticalLayout_2.addWidget(self.select_second_image_btn, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.result_img_lbl = QtWidgets.QLabel(Form)
        self.result_img_lbl.setMaximumSize(QtCore.QSize(500, 500))
        self.result_img_lbl.setScaledContents(True)
        self.result_img_lbl.setObjectName("result_img_lbl")
        self.verticalLayout_4.addWidget(self.result_img_lbl, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.choose_operation_com = QtWidgets.QComboBox(self.frame)
        self.choose_operation_com.setObjectName("choose_operation_com")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.choose_operation_com.addItem("")
        self.verticalLayout_3.addWidget(self.choose_operation_com)
        self.result_btn = QtWidgets.QPushButton(self.frame)
        self.result_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.result_btn.setObjectName("result_btn")
        self.verticalLayout_3.addWidget(self.result_btn)
        self.verticalLayout_4.addWidget(self.frame, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.first_img_lbl.setText(_translate("Form", "TextLabel"))
        self.select_first_image_btn.setText(_translate("Form", "Choose First Image"))
        self.second_img_lbl.setText(_translate("Form", "TextLabel"))
        self.select_second_image_btn.setText(_translate("Form", "Choose Second Image"))
        self.result_img_lbl.setText(_translate("Form", "TextLabel"))
        self.choose_operation_com.setItemText(0, _translate("Form", "+"))
        self.choose_operation_com.setItemText(1, _translate("Form", "-"))
        self.choose_operation_com.setItemText(2, _translate("Form", "*"))
        self.choose_operation_com.setItemText(3, _translate("Form", "/"))
        self.choose_operation_com.setItemText(4, _translate("Form", "XOR"))
        self.choose_operation_com.setItemText(5, _translate("Form", "OR"))
        self.choose_operation_com.setItemText(6, _translate("Form", "AND"))
        self.choose_operation_com.setItemText(7, _translate("Form", "NOT"))
        self.choose_operation_com.setItemText(8, _translate("Form", "Diff"))
        self.choose_operation_com.setItemText(9, _translate("Form", "Max"))
        self.choose_operation_com.setItemText(10, _translate("Form", "Min"))
        self.choose_operation_com.setItemText(11, _translate("Form", "Histogram Matching"))
        self.result_btn.setText(_translate("Form", "GO"))
