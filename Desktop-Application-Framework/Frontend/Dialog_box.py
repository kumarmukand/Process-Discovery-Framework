# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_box.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error_Label(object):
    def setupUi(self, Error_Label):
        Error_Label.setObjectName("Error_Label")
        Error_Label.resize(345, 99)
        self.empty_label = QtWidgets.QLabel(Error_Label)
        self.empty_label.setGeometry(QtCore.QRect(50, 30, 241, 31))
        self.empty_label.setObjectName("empty_label")

        self.retranslateUi(Error_Label)
        QtCore.QMetaObject.connectSlotsByName(Error_Label)

    def retranslateUi(self, Error_Label):
        _translate = QtCore.QCoreApplication.translate
        Error_Label.setWindowTitle(_translate("Error_Label", "Error!"))
        self.empty_label.setText(_translate("Error_Label", "Empty File,Please import another file!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error_Label = QtWidgets.QDialog()
    ui = Ui_Error_Label()
    ui.setupUi(Error_Label)
    Error_Label.show()
    sys.exit(app.exec_())

