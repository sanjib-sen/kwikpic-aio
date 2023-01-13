# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kwikpic.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kwikpic(object):
    def setupUi(self, Kwikpic):
        Kwikpic.setObjectName("Kwikpic")
        Kwikpic.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Kwikpic.sizePolicy().hasHeightForWidth())
        Kwikpic.setSizePolicy(sizePolicy)
        Kwikpic.setMinimumSize(QtCore.QSize(800, 600))
        Kwikpic.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../OneDrive/Documents/logo, favicon/Group 2015@LDPI.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Kwikpic.setWindowIcon(icon)
        Kwikpic.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Kwikpic)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.watermark = QtWidgets.QWidget()
        self.watermark.setObjectName("watermark")
        self.watermark_src = QtWidgets.QLineEdit(self.watermark)
        self.watermark_src.setGeometry(QtCore.QRect(160, 150, 381, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.watermark_src.setFont(font)
        self.watermark_src.setObjectName("watermark_src")
        self.watermark_position = QtWidgets.QComboBox(self.watermark)
        self.watermark_position.setGeometry(QtCore.QRect(160, 230, 121, 21))
        self.watermark_position.setEditable(False)
        self.watermark_position.setObjectName("watermark_position")
        self.watermark_size = QtWidgets.QLineEdit(self.watermark)
        self.watermark_size.setGeometry(QtCore.QRect(530, 280, 71, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watermark_size.sizePolicy().hasHeightForWidth())
        self.watermark_size.setSizePolicy(sizePolicy)
        self.watermark_size.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.watermark_size.setFont(font)
        self.watermark_size.setObjectName("watermark_size")
        self.label_9 = QtWidgets.QLabel(self.watermark)
        self.label_9.setGeometry(QtCore.QRect(160, 129, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.watermark_submit = QtWidgets.QPushButton(self.watermark)
        self.watermark_submit.setGeometry(QtCore.QRect(320, 360, 131, 21))
        self.watermark_submit.setObjectName("watermark_submit")
        self.label_14 = QtWidgets.QLabel(self.watermark)
        self.label_14.setGeometry(QtCore.QRect(560, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(self.watermark)
        self.label_12.setGeometry(QtCore.QRect(220, 20, 301, 131))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../../../Downloads/Primary_Logo.png"))
        self.label_12.setObjectName("label_12")
        self.watermark_browse_src = QtWidgets.QPushButton(self.watermark)
        self.watermark_browse_src.setGeometry(QtCore.QRect(550, 150, 71, 21))
        self.watermark_browse_src.setObjectName("watermark_browse_src")
        self.watermark_type_combo = QtWidgets.QComboBox(self.watermark)
        self.watermark_type_combo.setGeometry(QtCore.QRect(310, 230, 81, 22))
        self.watermark_type_combo.setObjectName("watermark_type_combo")
        self.watermark_type_text = QtWidgets.QLineEdit(self.watermark)
        self.watermark_type_text.setGeometry(QtCore.QRect(160, 280, 261, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.watermark_type_text.setFont(font)
        self.watermark_type_text.setObjectName("watermark_type_text")
        self.watermark_type_browse = QtWidgets.QPushButton(self.watermark)
        self.watermark_type_browse.setGeometry(QtCore.QRect(430, 280, 61, 21))
        self.watermark_type_browse.setObjectName("watermark_type_browse")
        self.label_23 = QtWidgets.QLabel(self.watermark)
        self.label_23.setGeometry(QtCore.QRect(320, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.watermark)
        self.label_24.setGeometry(QtCore.QRect(530, 260, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.watermark)
        self.label_25.setGeometry(QtCore.QRect(160, 210, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.watermark)
        self.label_26.setGeometry(QtCore.QRect(310, 210, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.watermark)
        self.label_27.setGeometry(QtCore.QRect(160, 260, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.watermark)
        self.label_28.setGeometry(QtCore.QRect(160, 320, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.checkBox = QtWidgets.QCheckBox(self.watermark)
        self.checkBox.setGeometry(QtCore.QRect(390, 320, 21, 21))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_13 = QtWidgets.QLabel(self.watermark)
        self.label_13.setGeometry(QtCore.QRect(160, 400, 441, 121))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.watermark, "")
        self.optimize = QtWidgets.QWidget()
        self.optimize.setObjectName("optimize")
        self.optimize_submit = QtWidgets.QPushButton(self.optimize)
        self.optimize_submit.setGeometry(QtCore.QRect(340, 280, 81, 21))
        self.optimize_submit.setObjectName("optimize_submit")
        self.optimize_src = QtWidgets.QLineEdit(self.optimize)
        self.optimize_src.setGeometry(QtCore.QRect(230, 210, 341, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.optimize_src.setFont(font)
        self.optimize_src.setText("")
        self.optimize_src.setObjectName("optimize_src")
        self.optimize_destination = QtWidgets.QLineEdit(self.optimize)
        self.optimize_destination.setGeometry(QtCore.QRect(230, 240, 341, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.optimize_destination.setFont(font)
        self.optimize_destination.setObjectName("optimize_destination")
        self.label_16 = QtWidgets.QLabel(self.optimize)
        self.label_16.setGeometry(QtCore.QRect(240, 50, 301, 131))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../../../Downloads/Primary_Logo.png"))
        self.label_16.setObjectName("label_16")
        self.optimize_browse_src = QtWidgets.QPushButton(self.optimize)
        self.optimize_browse_src.setGeometry(QtCore.QRect(580, 210, 71, 21))
        self.optimize_browse_src.setObjectName("optimize_browse_src")
        self.optimize_browse_destination = QtWidgets.QPushButton(self.optimize)
        self.optimize_browse_destination.setGeometry(QtCore.QRect(580, 240, 71, 21))
        self.optimize_browse_destination.setObjectName("optimize_browse_destination")
        self.label_10 = QtWidgets.QLabel(self.optimize)
        self.label_10.setGeometry(QtCore.QRect(140, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.optimize)
        self.label_11.setGeometry(QtCore.QRect(110, 240, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_19 = QtWidgets.QLabel(self.optimize)
        self.label_19.setGeometry(QtCore.QRect(110, 330, 541, 141))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.optimize, "")
        self.rename = QtWidgets.QWidget()
        self.rename.setObjectName("rename")
        self.rename_src = QtWidgets.QLineEdit(self.rename)
        self.rename_src.setGeometry(QtCore.QRect(230, 220, 341, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rename_src.setFont(font)
        self.rename_src.setObjectName("rename_src")
        self.rename_submit = QtWidgets.QPushButton(self.rename)
        self.rename_submit.setGeometry(QtCore.QRect(330, 260, 111, 21))
        self.rename_submit.setObjectName("rename_submit")
        self.label_15 = QtWidgets.QLabel(self.rename)
        self.label_15.setGeometry(QtCore.QRect(260, 60, 301, 131))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("../../../Downloads/Primary_Logo.png"))
        self.label_15.setObjectName("label_15")
        self.rename_browse_src = QtWidgets.QPushButton(self.rename)
        self.rename_browse_src.setGeometry(QtCore.QRect(580, 220, 71, 21))
        self.rename_browse_src.setObjectName("rename_browse_src")
        self.label_20 = QtWidgets.QLabel(self.rename)
        self.label_20.setGeometry(QtCore.QRect(140, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.rename)
        self.label_21.setGeometry(QtCore.QRect(140, 330, 511, 141))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.tabWidget.addTab(self.rename, "")
        self.copy = QtWidgets.QWidget()
        self.copy.setObjectName("copy")
        self.copy_submit = QtWidgets.QPushButton(self.copy)
        self.copy_submit.setGeometry(QtCore.QRect(340, 280, 81, 21))
        self.copy_submit.setObjectName("copy_submit")
        self.copy_src_textFile = QtWidgets.QLineEdit(self.copy)
        self.copy_src_textFile.setGeometry(QtCore.QRect(220, 220, 341, 21))
        self.copy_src_textFile.setObjectName("copy_src_textFile")
        self.label_17 = QtWidgets.QLabel(self.copy)
        self.label_17.setGeometry(QtCore.QRect(230, 60, 301, 131))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("../../../Downloads/Primary_Logo.png"))
        self.label_17.setObjectName("label_17")
        self.copy_browse_src_textFile = QtWidgets.QPushButton(self.copy)
        self.copy_browse_src_textFile.setGeometry(QtCore.QRect(570, 220, 71, 21))
        self.copy_browse_src_textFile.setObjectName("copy_browse_src_textFile")
        self.copy_src_folder = QtWidgets.QLineEdit(self.copy)
        self.copy_src_folder.setGeometry(QtCore.QRect(220, 250, 341, 21))
        self.copy_src_folder.setObjectName("copy_src_folder")
        self.copy_browse_src_folder = QtWidgets.QPushButton(self.copy)
        self.copy_browse_src_folder.setGeometry(QtCore.QRect(570, 250, 71, 21))
        self.copy_browse_src_folder.setObjectName("copy_browse_src_folder")
        self.label_29 = QtWidgets.QLabel(self.copy)
        self.label_29.setGeometry(QtCore.QRect(130, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.copy)
        self.label_30.setGeometry(QtCore.QRect(100, 250, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.copy)
        self.label_31.setGeometry(QtCore.QRect(110, 360, 531, 131))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.tabWidget.addTab(self.copy, "")
        Kwikpic.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Kwikpic)
        self.statusbar.setObjectName("statusbar")
        Kwikpic.setStatusBar(self.statusbar)

        self.retranslateUi(Kwikpic)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Kwikpic)

    def retranslateUi(self, Kwikpic):
        _translate = QtCore.QCoreApplication.translate
        Kwikpic.setWindowTitle(_translate("Kwikpic", "Kwikpic"))
        self.label_9.setText(_translate("Kwikpic", "Source Folder"))
        self.watermark_submit.setText(_translate("Kwikpic", "Add Watermark"))
        self.label_14.setText(_translate("Kwikpic", "(in pts)"))
        self.watermark_browse_src.setText(_translate("Kwikpic", "Browse"))
        self.watermark_type_browse.setText(_translate("Kwikpic", "Browse"))
        self.label_23.setText(_translate("Kwikpic", "<html><head/><body><p><span style=\" font-size:11pt; color:#0f80ff;\">Watermark Details</span></p></body></html>"))
        self.label_24.setText(_translate("Kwikpic", "Size"))
        self.label_25.setText(_translate("Kwikpic", "Position"))
        self.label_26.setText(_translate("Kwikpic", "Type"))
        self.label_27.setText(_translate("Kwikpic", "Image"))
        self.label_28.setText(_translate("Kwikpic", "Do you want to optimze the images as well?"))
        self.label_13.setText(_translate("Kwikpic", "Click \"Add Watermark\" to continue..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.watermark), _translate("Kwikpic", "Watermark"))
        self.optimize_submit.setText(_translate("Kwikpic", "Optimize"))
        self.optimize_browse_src.setText(_translate("Kwikpic", "Browse"))
        self.optimize_browse_destination.setText(_translate("Kwikpic", "Browse"))
        self.label_10.setText(_translate("Kwikpic", "Source Folder"))
        self.label_11.setText(_translate("Kwikpic", "Destination Folder"))
        self.label_19.setText(_translate("Kwikpic", "Click \"Optimize\" to continue..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optimize), _translate("Kwikpic", "Optimize"))
        self.rename_submit.setText(_translate("Kwikpic", "Rename Files"))
        self.rename_browse_src.setText(_translate("Kwikpic", "Browse"))
        self.label_20.setText(_translate("Kwikpic", "Source Folder"))
        self.label_21.setText(_translate("Kwikpic", "Source Folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rename), _translate("Kwikpic", "Rename"))
        self.copy_submit.setText(_translate("Kwikpic", "Copy"))
        self.copy_browse_src_textFile.setText(_translate("Kwikpic", "Browse"))
        self.copy_browse_src_folder.setText(_translate("Kwikpic", "Browse"))
        self.label_29.setText(_translate("Kwikpic", "Source Folder"))
        self.label_30.setText(_translate("Kwikpic", "Destination Folder"))
        self.label_31.setText(_translate("Kwikpic", "Click on \"Copy\" to continue..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.copy), _translate("Kwikpic", "Copy"))