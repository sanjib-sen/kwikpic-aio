# sksenonline@gmail.com


from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
from urllib.parse import unquote
import os
import threading
import sys
import cv2

if getattr(sys, 'frozen', False):
    logo = os.path.join(sys._MEIPASS, 'logo.png')
else:
    logo = "logo/logo.png"


QUALITY_PERCENTAGE = 90
watermark_positions = ["Bottom Right", "Bottom Left", "Top Left", "Top Right"]
watermark_types = ["Image", "Text"]


class Ui_Kwikpic(object):
    def setupUi(self, Kwikpic):
        Kwikpic.setObjectName("Kwikpic")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Kwikpic.setWindowIcon(icon)
        Kwikpic.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Kwikpic.sizePolicy().hasHeightForWidth())
        Kwikpic.setSizePolicy(sizePolicy)
        Kwikpic.setMinimumSize(QtCore.QSize(800, 600))
        Kwikpic.setMaximumSize(QtCore.QSize(800, 600))
        Kwikpic.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Kwikpic)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 591))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.watermark = QtWidgets.QWidget()
        self.watermark.setObjectName("watermark")
        self.watermark_src = QtWidgets.QLineEdit(self.watermark)
        self.watermark_src.setGeometry(QtCore.QRect(160, 150, 131, 21))
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.watermark_size.sizePolicy().hasHeightForWidth())
        self.watermark_size.setSizePolicy(sizePolicy)
        self.watermark_size.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.watermark_size.setFont(font)
        self.watermark_size.setObjectName("watermark_size")
        self.label_9 = QtWidgets.QLabel(self.watermark)
        self.label_9.setGeometry(QtCore.QRect(160, 129, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.watermark_submit = QtWidgets.QPushButton(self.watermark)
        self.watermark_submit.setGeometry(QtCore.QRect(320, 360, 141, 31))
        self.watermark_submit.setObjectName("watermark_submit")
        self.label_14 = QtWidgets.QLabel(self.watermark)
        self.label_14.setGeometry(QtCore.QRect(560, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(self.watermark)
        self.label_12.setGeometry(QtCore.QRect(220, 20, 301, 131))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(logo))
        self.label_12.setObjectName("label_12")
        self.watermark_browse_src = QtWidgets.QPushButton(self.watermark)
        self.watermark_browse_src.setGeometry(QtCore.QRect(290, 150, 71, 21))
        self.watermark_browse_src.setObjectName("watermark_browse_src")
        self.watermark_type_combo = QtWidgets.QComboBox(self.watermark)
        self.watermark_type_combo.setGeometry(QtCore.QRect(310, 230, 81, 22))
        self.watermark_type_combo.setObjectName("watermark_type_combo")
        self.watermark_cropped_src_or_text = QtWidgets.QLineEdit(
            self.watermark)
        self.watermark_cropped_src_or_text.setGeometry(
            QtCore.QRect(160, 280, 261, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.watermark_cropped_src_or_text.setFont(font)
        self.watermark_cropped_src_or_text.setObjectName(
            "watermark_cropped_src_or_text")
        self.watermark_cropped_src_browse = QtWidgets.QPushButton(
            self.watermark)
        self.watermark_cropped_src_browse.setGeometry(
            QtCore.QRect(430, 280, 61, 21))
        self.watermark_cropped_src_browse.setObjectName(
            "watermark_cropped_src_browse")
        self.label_23 = QtWidgets.QLabel(self.watermark)
        self.label_23.setGeometry(QtCore.QRect(320, 190, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
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
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
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
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
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
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.watermark_type_label = QtWidgets.QLabel(self.watermark)
        self.watermark_type_label.setGeometry(QtCore.QRect(160, 260, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.watermark_type_label.setFont(font)
        self.watermark_type_label.setObjectName("watermark_type_label")
        self.label_28 = QtWidgets.QLabel(self.watermark)
        self.label_28.setGeometry(QtCore.QRect(180, 320, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.watermark_optimize_checkbox = QtWidgets.QCheckBox(self.watermark)
        self.watermark_optimize_checkbox.setGeometry(
            QtCore.QRect(160, 320, 21, 21))
        self.watermark_optimize_checkbox.setText("")
        self.watermark_optimize_checkbox.setObjectName(
            "watermark_optimize_checkbox")
        self.watermark_progress = QtWidgets.QLabel(self.watermark)
        self.watermark_progress.setGeometry(QtCore.QRect(160, 400, 441, 121))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.watermark_progress.setFont(font)
        self.watermark_progress.setObjectName("watermark_progress")
        self.watermark_browse_destination = QtWidgets.QPushButton(
            self.watermark)
        self.watermark_browse_destination.setGeometry(
            QtCore.QRect(520, 150, 71, 21))
        self.watermark_browse_destination.setObjectName(
            "watermark_browse_destination")
        self.label_13 = QtWidgets.QLabel(self.watermark)
        self.label_13.setGeometry(QtCore.QRect(390, 129, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.watermark_destination = QtWidgets.QLineEdit(self.watermark)
        self.watermark_destination.setGeometry(QtCore.QRect(390, 150, 131, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.watermark_destination.setFont(font)
        self.watermark_destination.setObjectName("watermark_destination")
        self.tabWidget.addTab(self.watermark, "")
        self.optimize = QtWidgets.QWidget()
        self.optimize.setObjectName("optimize")
        self.optimize_submit = QtWidgets.QPushButton(self.optimize)
        self.optimize_submit.setGeometry(QtCore.QRect(340, 230, 111, 31))
        self.optimize_submit.setObjectName("optimize_submit")
        self.optimize_src = QtWidgets.QLineEdit(self.optimize)
        self.optimize_src.setGeometry(QtCore.QRect(170, 190, 141, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.optimize_src.setFont(font)
        self.optimize_src.setText("")
        self.optimize_src.setObjectName("optimize_src")
        self.optimize_destination = QtWidgets.QLineEdit(self.optimize)
        self.optimize_destination.setGeometry(QtCore.QRect(400, 190, 141, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.optimize_destination.setFont(font)
        self.optimize_destination.setObjectName("optimize_destination")
        self.label_16 = QtWidgets.QLabel(self.optimize)
        self.label_16.setGeometry(QtCore.QRect(220, 50, 301, 131))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(logo))
        self.label_16.setObjectName("label_16")
        self.optimize_browse_src = QtWidgets.QPushButton(self.optimize)
        self.optimize_browse_src.setGeometry(QtCore.QRect(310, 190, 71, 21))
        self.optimize_browse_src.setObjectName("optimize_browse_src")
        self.optimize_browse_destination = QtWidgets.QPushButton(self.optimize)
        self.optimize_browse_destination.setGeometry(
            QtCore.QRect(540, 190, 71, 21))
        self.optimize_browse_destination.setObjectName(
            "optimize_browse_destination")
        self.label_10 = QtWidgets.QLabel(self.optimize)
        self.label_10.setGeometry(QtCore.QRect(170, 170, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.optimize)
        self.label_11.setGeometry(QtCore.QRect(400, 170, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.optimize_progress = QtWidgets.QLabel(self.optimize)
        self.optimize_progress.setGeometry(QtCore.QRect(170, 330, 481, 141))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.optimize_progress.setFont(font)
        self.optimize_progress.setObjectName("optimize_progress")
        self.tabWidget.addTab(self.optimize, "")
        self.rename = QtWidgets.QWidget()
        self.rename.setObjectName("rename")
        self.rename_src = QtWidgets.QLineEdit(self.rename)
        self.rename_src.setGeometry(QtCore.QRect(170, 190, 141, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rename_src.setFont(font)
        self.rename_src.setObjectName("rename_src")
        self.rename_submit = QtWidgets.QPushButton(self.rename)
        self.rename_submit.setGeometry(QtCore.QRect(340, 230, 111, 31))
        self.rename_submit.setObjectName("rename_submit")
        self.label_15 = QtWidgets.QLabel(self.rename)
        self.label_15.setGeometry(QtCore.QRect(220, 50, 301, 131))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(logo))
        self.label_15.setObjectName("label_15")
        self.rename_browse_src = QtWidgets.QPushButton(self.rename)
        self.rename_browse_src.setGeometry(QtCore.QRect(310, 190, 71, 21))
        self.rename_browse_src.setObjectName("rename_browse_src")
        self.label_20 = QtWidgets.QLabel(self.rename)
        self.label_20.setGeometry(QtCore.QRect(170, 170, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.rename_progress = QtWidgets.QLabel(self.rename)
        self.rename_progress.setGeometry(QtCore.QRect(170, 330, 481, 141))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.rename_progress.setFont(font)
        self.rename_progress.setObjectName("rename_progress")
        self.rename_browse_destination = QtWidgets.QPushButton(self.rename)
        self.rename_browse_destination.setGeometry(
            QtCore.QRect(540, 190, 71, 21))
        self.rename_browse_destination.setObjectName(
            "rename_browse_destination")
        self.rename_destination = QtWidgets.QLineEdit(self.rename)
        self.rename_destination.setGeometry(QtCore.QRect(400, 190, 141, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rename_destination.setFont(font)
        self.rename_destination.setObjectName("rename_destination")
        self.label_21 = QtWidgets.QLabel(self.rename)
        self.label_21.setGeometry(QtCore.QRect(400, 170, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.tabWidget.addTab(self.rename, "")
        self.copy = QtWidgets.QWidget()
        self.copy.setObjectName("copy")
        self.copy_submit = QtWidgets.QPushButton(self.copy)
        self.copy_submit.setGeometry(QtCore.QRect(320, 270, 91, 31))
        self.copy_submit.setObjectName("copy_submit")
        self.copy_src_textFile = QtWidgets.QLineEdit(self.copy)
        self.copy_src_textFile.setGeometry(QtCore.QRect(170, 230, 391, 21))
        self.copy_src_textFile.setObjectName("copy_src_textFile")
        self.label_17 = QtWidgets.QLabel(self.copy)
        self.label_17.setGeometry(QtCore.QRect(220, 50, 301, 131))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(logo))
        self.label_17.setObjectName("label_17")
        self.copy_browse_src_textFile = QtWidgets.QPushButton(self.copy)
        self.copy_browse_src_textFile.setGeometry(
            QtCore.QRect(560, 230, 81, 21))
        self.copy_browse_src_textFile.setObjectName("copy_browse_src_textFile")
        self.copy_destination_folder = QtWidgets.QLineEdit(self.copy)
        self.copy_destination_folder.setGeometry(
            QtCore.QRect(420, 180, 141, 21))
        self.copy_destination_folder.setObjectName("copy_destination_folder")
        self.copy_browse_destination_folder = QtWidgets.QPushButton(self.copy)
        self.copy_browse_destination_folder.setGeometry(
            QtCore.QRect(560, 180, 81, 21))
        self.copy_browse_destination_folder.setObjectName(
            "copy_browse_destination_folder")
        self.label_29 = QtWidgets.QLabel(self.copy)
        self.label_29.setGeometry(QtCore.QRect(170, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.copy)
        self.label_30.setGeometry(QtCore.QRect(420, 160, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.copy_progress = QtWidgets.QLabel(self.copy)
        self.copy_progress.setGeometry(QtCore.QRect(170, 360, 471, 131))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.copy_progress.setFont(font)
        self.copy_progress.setObjectName("copy_progress")
        self.copy_browse_src_folder = QtWidgets.QPushButton(self.copy)
        self.copy_browse_src_folder.setGeometry(QtCore.QRect(320, 180, 71, 21))
        self.copy_browse_src_folder.setObjectName("copy_browse_src_folder")
        self.label_31 = QtWidgets.QLabel(self.copy)
        self.label_31.setGeometry(QtCore.QRect(170, 160, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.copy_src_folder = QtWidgets.QLineEdit(self.copy)
        self.copy_src_folder.setGeometry(QtCore.QRect(170, 180, 151, 21))
        self.copy_src_folder.setObjectName("copy_src_folder")
        self.tabWidget.addTab(self.copy, "")
        self.statusbar = QtWidgets.QStatusBar(Kwikpic)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(Kwikpic)
        # self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Kwikpic)

    def retranslateUi(self, Kwikpic):
        _translate = QtCore.QCoreApplication.translate
        Kwikpic.setWindowTitle(_translate("Kwikpic", "Kwikpic"))
        self.label_9.setText(_translate("Kwikpic", "Source Folder"))
        self.watermark_submit.setText(_translate("Kwikpic", "Add Watermark"))
        self.label_14.setText(_translate("Kwikpic", "(in pts)"))
        self.watermark_browse_src.setText(_translate("Kwikpic", "Browse"))
        self.watermark_cropped_src_browse.setText(
            _translate("Kwikpic", "Browse"))
        self.label_23.setText(_translate(
            "Kwikpic", "<html><head/><body><p><span style=\" font-size:11pt; color:#0f80ff;\">Watermark Details</span></p></body></html>"))
        self.label_24.setText(_translate("Kwikpic", "Size"))
        self.label_25.setText(_translate("Kwikpic", "Position"))
        self.label_26.setText(_translate("Kwikpic", "Type"))
        self.watermark_type_label.setText(_translate("Kwikpic", "Image"))
        self.label_28.setText(_translate("Kwikpic", "Optimize Images as well"))
        self.watermark_progress.setText(_translate(
            "Kwikpic", "Click \"Add Watermark\" to continue..."))
        self.watermark_browse_destination.setText(
            _translate("Kwikpic", "Browse"))
        self.label_13.setText(_translate("Kwikpic", "Destination Folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.watermark), _translate("Kwikpic", "Watermark"))
        self.optimize_submit.setText(_translate("Kwikpic", "Optimize Images"))
        self.optimize_browse_src.setText(_translate("Kwikpic", "Browse"))
        self.optimize_browse_destination.setText(
            _translate("Kwikpic", "Browse"))
        self.label_10.setText(_translate("Kwikpic", "Source Folder"))
        self.label_11.setText(_translate("Kwikpic", "Destination Folder"))
        self.optimize_progress.setText(_translate(
            "Kwikpic", "Click \"Optimize\" to continue..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.optimize), _translate("Kwikpic", "Optimize"))
        self.rename_submit.setText(_translate("Kwikpic", "Rename Files"))
        self.rename_browse_src.setText(_translate("Kwikpic", "Browse"))
        self.label_20.setText(_translate("Kwikpic", "Source Folder"))
        self.rename_progress.setText(_translate(
            "Kwikpic", "Click \"Rename Files\" to continue"))
        self.rename_browse_destination.setText(_translate("Kwikpic", "Browse"))
        self.label_21.setText(_translate("Kwikpic", "Destination Folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.rename), _translate("Kwikpic", "Rename"))
        self.copy_submit.setText(_translate("Kwikpic", "Copy"))
        self.copy_browse_src_textFile.setText(_translate("Kwikpic", "Browse"))
        self.copy_browse_destination_folder.setText(
            _translate("Kwikpic", "Browse"))
        self.label_29.setText(_translate("Kwikpic", "Text File"))
        self.label_30.setText(_translate("Kwikpic", "Destination Folder"))
        self.copy_progress.setText(_translate(
            "Kwikpic", "Click on \"Copy\" to continue..."))
        self.copy_browse_src_folder.setText(_translate("Kwikpic", "Browse"))
        self.label_31.setText(_translate("Kwikpic", "Source Folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.copy), _translate("Kwikpic", "Copy"))

        # RENAME PROCESS
        self.rename_browse_src.clicked.connect(self.renameSelectSourceFolder)
        self.rename_browse_destination.clicked.connect(
            self.renameSelectDestinationFolder)
        self.rename_submit.clicked.connect(self.renameProcessThread)

        # OPTIMIZE PROCESS
        self.optimize_browse_src.clicked.connect(
            self.optimizeSelectSourceFolder)
        self.optimize_browse_destination.clicked.connect(
            self.optimizeSelectDestFolder)
        self.optimize_submit.clicked.connect(self.optimizeProcessThread)

        # COPY PROCESS
        self.copy_browse_src_folder.clicked.connect(
            self.copySelectSourceFolder)
        self.copy_browse_src_textFile.clicked.connect(
            self.copySelectSourceTextFile)
        self.copy_browse_destination_folder.clicked.connect(
            self.copySelectDestFolder)
        self.copy_submit.clicked.connect(self.copyProcessThread)

        # WATERMARK PROCESS
        self.watermark_browse_src.clicked.connect(
            self.watermarkSelectSourceFolder)
        self.watermark_browse_destination.clicked.connect(
            self.watermarkSelectDestinationFolder)
        self.watermark_cropped_src_browse.clicked.connect(
            self.watermarkSelectWatermarkImage)
        self.watermark_submit.clicked.connect(self.watermarkProcessThread)
        self.watermark_optimize_checkbox.setChecked(True)
        self.watermark_position.addItems(watermark_positions)
        self.watermark_type_combo.addItems(watermark_types)
        self.watermark_type_combo.currentTextChanged.connect(
            self.watermarkTypeChanges)
        self.watermark_size.setText("11")

    '''
    -------------------------------------------------------------------------------------------------
    RENAME FILES
    ------------------------------------------------------------------------------------------------
    '''

    def renameSelectSourceFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Source Folder")
        self.rename_src.setText(folder)

    def renameSelectDestinationFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Destination Folder")
        self.rename_destination.setText(folder)

    def renameProcessThread(self):
        if self.rename_src.text() == None or self.rename_src.text() == "":
            self.rename_progress.setText("Please Select a Source Folder.")
            return
        if self.rename_destination.text() == None or self.rename_destination.text() == "":
            self.rename_progress.setText(
                "Please Select a Destination Folder.")
            return
        if isDestInSrc(self.rename_src.text(), self.rename_destination.text()):
            self.rename_progress.setText(
                "Destination folder can not be inside the Source Folder")
            return
        x = threading.Thread(target=self.renameProcess)
        x.start()

    def renameProcess(self, givenPath=None, givenDestination=None):
        UNKNOWN_DIR = None
        if not givenPath:
            UNKNOWN_DIR = self.rename_src.text()
        else:
            UNKNOWN_DIR = givenPath
        path = UNKNOWN_DIR
        self.rename_progress.setText("Renaming... Please wait...")
        try:
            currentPath = path
            filesList = os.listdir(currentPath)
            newDir = None
            if not givenDestination:
                newDir = self.rename_destination.text()+"/"
            else:
                newDir = givenDestination+"/"

            for item in filesList:
                try:
                    if os.path.isfile(os.path.join(currentPath, item)):

                        filteredName = unquote(item.rsplit("@", 1)[-1])
                        shutil.copyfile(os.path.join(
                            currentPath, item), os.path.join(newDir, filteredName))
                    else:
                        if not os.path.exists(os.path.join(newDir, item)):
                            os.mkdir(os.path.join(newDir, item))
                        givenPath = os.path.join(currentPath, item)
                        givenDestination = os.path.join(newDir, item)
                        self.renameProcess(givenPath, givenDestination)
                except Exception as e:
                    pass
        except Exception as e:
            self.rename_progress.setText("Error occurred:", e)
        self.rename_progress.setText("Rename and copy done.")

    '''
    -------------------------------------------------------------------------------------------------
    OPTIMIZE IMAGES
    ------------------------------------------------------------------------------------------------
    '''

    def optimizeSelectSourceFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Source Folder")
        self.optimize_src.setText(folder)

    def optimizeSelectDestFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Destination Folder")
        self.optimize_destination.setText(folder)

    def optimizeProcessThread(self):
        if self.optimize_src.text() == None or self.optimize_src.text() == "":
            self.optimize_progress.setText("Please Select a Source Folder.")
            return
        if self.optimize_destination.text() == None or self.optimize_destination.text() == "":
            self.optimize_progress.setText(
                "Please Select a Destination Folder.")
            return
        if isDestInSrc(self.optimize_src.text(), self.optimize_destination.text()):
            self.optimize_progress.setText(
                "Destination folder can not be inside the Source Folder")
            return
        x = threading.Thread(target=self.optimizeProcess)
        x.start()

    def optimizeProcess(self):
        UNKNOWN_DIR = self.optimize_src.text()
        COMPRESS_DIR = self.optimize_destination.text()+"/"
        if not os.path.exists(COMPRESS_DIR):
            os.mkdir(COMPRESS_DIR)
        count = fileCount(UNKNOWN_DIR)
        curr_count = 0

        for path, _, files in os.walk(UNKNOWN_DIR):

            for img_name in files:

                img_path = os.path.join(path, img_name)

                img_rel_path = os.path.relpath(img_path, UNKNOWN_DIR)

                img_name = os.path.basename(img_path)
                try:
                    img = cv2.imread(img_path)
                except:
                    continue

                if img is not None:
                    self.optimize_progress.setText(
                        str(str(curr_count)+" out of "+str(count)+" images optimized"))
                    scale_percent = 60
                    shape = img.shape
                    if shape[0] > shape[1]:
                        if shape[0] <= 2160:
                            scale_percent = 100
                        else:
                            scale_percent = 216000 / shape[0]
                    else:
                        if shape[1] <= 2160:
                            scale_percent = 100
                        else:
                            scale_percent = 216000 / shape[1]
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)

                    resized = cv2.resize(
                        img, dim, interpolation=cv2.INTER_AREA)
                    dir_name = os.path.dirname(img_rel_path)
                    if not os.path.exists(COMPRESS_DIR+dir_name) and not COMPRESS_DIR+dir_name == "":
                        os.makedirs(COMPRESS_DIR+dir_name)
                    img_rel_path = img_rel_path.rsplit(".", 1)[0]+".jpg"
                    cv2.imwrite(COMPRESS_DIR+img_rel_path, resized,
                                [int(cv2.IMWRITE_JPEG_QUALITY), QUALITY_PERCENTAGE])
                    curr_count += 1

        self.optimize_progress.setText(
            "Complete. "+str(count)+" images optimized")

    '''
    -------------------------------------------------------------------------------------------------
    COPY IMAGES
    ------------------------------------------------------------------------------------------------
    '''

    def copySelectSourceFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Source Folder")
        self.copy_src_folder.setText(folder)

    def copySelectSourceTextFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(
            Form, "Choose the Text File")
        self.copy_src_textFile.setText(file[0].toString()[7:])

    def copySelectDestFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Destination Folder")
        self.copy_destination_folder.setText(folder)

    def copyProcessThread(self):
        if self.copy_src_folder.text() == None or self.copy_src_folder.text() == "":
            self.copy_progress.setText("Please Select a Source Folder.")
            return
        if self.copy_src_textFile.text() == None or self.copy_src_textFile.text() == "":
            self.copy_progress.setText("Please Select a Text file.")
            return
        if self.copy_destination_folder.text() == None or self.copy_destination_folder.text() == "":
            self.copy_progress.setText("Please Select a Destination Folder.")
            return
        if isDestInSrc(self.copy_src_folder.text(), self.copy_destination_folder.text()):
            self.copy_progress.setText(
                "Destination folder can not be inside the Source Folder")
            return
        x = threading.Thread(target=self.copyProcess)
        x.start()

    def copyProcess(self):
        file_names = open(self.copy_src_textFile, "r").read().splitlines()
        copy_completed = []
        for root, dirs, files in os.walk(self.copy_src_folder):
            for file in files:
                if file in file_names and file not in copy_completed:
                    path_file = os.path.join(root, file)
                    shutil.copy2(path_file, self.copy_destination_folder+"/")
                    copy_completed.append(file)
                    self.copy_progress.setText(
                        f'Copying... {len(copy_completed)} out of {len(file_names)} files copied')
        self.copy_progress.setText(
            f"Copy Completed. Total {len(file_names)} files copied.")

    '''
    -------------------------------------------------------------------------------------------------
    ADD WATERMARK
    ------------------------------------------------------------------------------------------------
    '''

    def watermarkSelectSourceFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Source Folder of Images")
        self.watermark_src.setText(folder)

    def watermarkSelectDestinationFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Destination Folder of Images")
        self.watermark_destination.setText(folder)

    def watermarkTypeChanges(self):
        current_type = self.watermark_type_combo.currentText()
        self.watermark_type_label.setText(current_type)
        if current_type == "Text":
            self.watermark_cropped_src_browse.hide()
        else:
            self.watermark_cropped_src_browse.show()

    def watermarkSelectWatermarkImage(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(
            Form, "Select the Watermark Image")
        self.watermark_cropped_src_or_text.setText(file[0].toString()[7:])

    def watermarkProcessThread(self):
        if self.watermark_src.text() == None or self.watermark_src.text() == "":
            self.watermark_progress.setText("Please Select a Source Folder.")
            return
        if self.watermark_destination.text() == None or self.watermark_destination.text() == "":
            self.watermark_progress.setText(
                "Please Select a Destination Folder.")
            return
        if self.watermark_cropped_src_or_text.text() == None or self.watermark_cropped_src_or_text.text() == "":
            self.watermark_progress.setText(
                "Please Select an Image or Write Texts")
            return
        if self.watermark_type_combo.currentText() == "Text" and int(self.watermark_size.text()) > 29:
            self.watermark_progress.setText(
                "The maximum font size for Text is 29 pts")
            return
        if self.watermark_type_combo.currentText() == "Image" and int(self.watermark_size.text()) > 17:
            self.watermark_progress.setText(
                "The maximum font size for Image is 17 pts")
            return
        if isDestInSrc(self.watermark_src.text(), self.watermark_destination.text()):
            self.watermark_progress.setText(
                "Destination folder can not be inside the Source Folder")
            return

        x = threading.Thread(target=self.watermarkProcess)
        x.start()

    def watermarkProcess(self):
        if os.path.exists(os.getcwd()+"/temp"):
            shutil.rmtree(os.getcwd()+"/temp")
        watermark_type = self.watermark_type_combo.currentText()
        destination = self.watermark_destination.text()
        if self.watermark_optimize_checkbox.isChecked():
            destination = os.getcwd()+"/temp"
        if not os.path.exists(destination):
            os.mkdir(destination)

        exts = ['.bmp', '.dib', '.jpeg', '.jpg', '.jp2', '.png', '.webp',
                '.pbm', '.pgm', '.ppm', '.pxm', '.pnm', '.pfm', '.sr', '.ras',
                '.tiff', '.tif', '.exr', '.hdr', '.pic']

        image_count = fileCount(self.watermark_src.text())

        watermark_completed = []
        for root, dirs, files in os.walk(self.watermark_src.text()):
            for file in files:
                if file.endswith(tuple(exts)) and file.split(".")[-1] not in watermark_completed:
                    path_file = os.path.join(root, file)

                    if (watermark_type == "Text"):
                        add_text_watermark(path_file, self.watermark_cropped_src_or_text.text(),
                                           size=int(self.watermark_size.text()), directory=destination,
                                           text_position=self.watermark_position.currentText()
                                           )
                    else:
                        add_image_watermark(path_file, self.watermark_cropped_src_or_text.text(),
                                            size=int(self.watermark_size.text()), directory=destination,
                                            watermark_position=self.watermark_position.currentText()
                                            )
                    watermark_completed.append(file.rsplit(".", 1)[0])
                    self.watermark_progress.setText(
                        f'Adding Watermarks... {len(watermark_completed)} out of {image_count} images have been watermarked.')
        self.watermark_progress.setText(
            f"Watermarking Completed. Total {image_count} Images Watermarked.")
        if self.watermark_optimize_checkbox.isChecked():
            self.justOptimize()

    def justOptimize(self):
        UNKNOWN_DIR = os.getcwd()+"/temp/"
        COMPRESS_DIR = self.watermark_destination.text()+"/"
        print(COMPRESS_DIR)
        self.watermark_progress.setText("Optimizing...")
        count = fileCount(UNKNOWN_DIR)
        curr_count = 0
        for path, _, files in os.walk(UNKNOWN_DIR):
            for img_name in files:
                curr_count += 1
                self.watermark_progress.setText(
                    str(str(curr_count)+" out of "+str(count)+" images optimized"))
                img_path = os.path.join(path, img_name)
                img_rel_path = os.path.relpath(img_path, UNKNOWN_DIR)
                img_name = os.path.basename(img_path)
                try:
                    img = cv2.imread(img_path)
                except:
                    continue
                if img is not None:
                    self.watermark_progress.setText(
                        str(str(curr_count)+" out of "+str(count)+" images optimized"))
                    scale_percent = 60
                    shape = img.shape
                    if shape[0] > shape[1]:
                        if shape[0] <= 2160:
                            scale_percent = 100
                        else:
                            scale_percent = 216000 / shape[0]
                    else:
                        if shape[1] <= 2160:
                            scale_percent = 100
                        else:
                            scale_percent = 216000 / shape[1]
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    resized = cv2.resize(
                        img, dim, interpolation=cv2.INTER_AREA)
                    dir_name = os.path.dirname(img_rel_path)
                    if not os.path.exists(COMPRESS_DIR+dir_name) and not COMPRESS_DIR+dir_name == "":
                        os.makedirs(COMPRESS_DIR+dir_name)
                    img_rel_path = img_rel_path.rsplit(".", 1)[0]+".jpg"
                    cv2.imwrite(COMPRESS_DIR+img_rel_path, resized,
                                [int(cv2.IMWRITE_JPEG_QUALITY), QUALITY_PERCENTAGE])
        shutil.rmtree(UNKNOWN_DIR)
        self.watermark_progress.setText(
            "Completed. "+str(count)+" images watermarked and optimized")


def isDestInSrc(src, dest):
    '''
    Not Allowed Example:
    src = /sanjib/pics
    dest = /sanjib/pics/rename
    '''
    srcList = src.split("/")
    destList = dest.split("/")
    i = 0
    while i < min(len(srcList), len(destList)):
        if (len(srcList) == 0 or len(destList) == 0):
            break
        if srcList[i] == destList[i]:
            del srcList[i]
            del destList[i]
            i -= 1
        else:
            return False
        i += 1
    return True


def fileCount(folder):
    "count the number of files in a directory"
    exts = ['.bmp', '.dib', '.jpeg', '.jpg', '.jp2', '.png', '.webp',
            '.pbm', '.pgm', '.ppm', '.pxm', '.pnm', '.pfm', '.sr', '.ras',
            '.tiff', '.tif', '.exr', '.hdr', '.pic', '.ico']
    count = 0

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            if path.lower().endswith(tuple(exts)):
                count += 1
        elif os.path.isdir(path):
            count += fileCount(path)
    return count


def add_text_watermark(image_path, text, size=11, directory="", text_position="bottom-right"):
    text_position = text_position.lower().replace(" ", "-")
    if size == 31:
        size = 31.05
    image = Image.open(image_path)
    w, h = image.size
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)
    fontsize = int(max(w, h)/(31-size))
    font = ImageFont.truetype("arial.ttf", fontsize)
    pos = text_position
    if pos == "bottom-right":
        position = (int(w-fontsize*len(text)*0.5), int(h-fontsize*1.5))
    elif pos == "bottom-left":
        position = (0, int(h-fontsize*1.5))
    elif pos == "top-left":
        position = (0, 0)
    elif pos == "top-right":
        position = (int(w-fontsize*len(text)*0.7), 0)
    draw.text(position, text, fill=(255, 255, 255), font=font)
    file_name = image_path.split("/")[-1]
    new_path = None
    if directory == "" or directory[-1] == "/" or directory[-1] == "\\":
        new_path = directory+file_name
    else:
        new_path = directory+"/"+file_name
    watermark_image.save(new_path, subsampling=0)


def add_image_watermark(destination_image_path, watermark_image_path, size=11, directory="", watermark_position="top-right"):
    watermark_position = watermark_position.lower().replace(" ", "-")
    if size == 19:
        size = 19.05
    copied_image = Image.open(destination_image_path)
    w, h = copied_image.size
    size = (int(w/(19-size)), int(h/(19-size)))
    crop_image = Image.open(watermark_image_path)
    crop_image = crop_image.resize(size, resample=Image.BICUBIC)

    pos = watermark_position
    if pos == "bottom-right":
        position = (int(w-size[0]), int(h-size[1]))
    elif pos == "bottom-left":
        position = (0, int(h-size[1]))
    elif pos == "top-left":
        position = (0, 0)
    elif pos == "top-right":
        position = (int(w-size[0]), 0)

    copied_image.paste(crop_image, position, crop_image)

    file_name = destination_image_path.split("/")[-1]
    new_path = None
    if directory == "" or directory[-1] == "/" or directory[-1] == "\\":
        new_path = directory+file_name
    else:
        new_path = directory+"/"+file_name
    copied_image.save(new_path, subsampling=0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Kwikpic()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
