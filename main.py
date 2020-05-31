# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QTableWidgetItem

boxes = []
start_labels = []
end_labels = []
from PyQt5 import QtCore, QtGui, QtWidgets

import MainCode
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowTitle("MEMORY")
        Form.resize(1000, 750)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(680, 100, 300, 600))
        self.scrollArea.setMinimumSize(QtCore.QSize(100, 100))
        self.groupBox = QtWidgets.QGroupBox()
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.layout = QtWidgets.QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.layout)
        self.scrollArea.show()
        self.holeName_text = QtWidgets.QLineEdit(Form)
        self.holeName_text.setGeometry(QtCore.QRect(30, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.holeName_text.setFont(font)
        self.holeName_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.holeName_text.setAlignment(QtCore.Qt.AlignCenter)
        self.holeName_text.setObjectName("holeName_text")
        self.holeStart_text = QtWidgets.QLineEdit(Form)
        self.holeStart_text.setGeometry(QtCore.QRect(200, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.holeStart_text.setFont(font)
        self.holeStart_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.holeStart_text.setAlignment(QtCore.Qt.AlignCenter)
        self.holeStart_text.setObjectName("holeStart_text")
        self.label_layout_title = QtWidgets.QPushButton(Form)
        self.label_layout_title.setGeometry(QtCore.QRect(690, 40, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_layout_title.setFont(font)
        self.label_layout_title.clicked.connect(lambda : self.first_layout(Form))
        self.label_layout_title.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.label_layout_title.setObjectName("label_layout_title")
        self.refresh_btn = QtWidgets.QPushButton(Form)
        self.refresh_btn.clicked.connect(lambda : self.update_memory(Form))
        self.refresh_btn.setGeometry(QtCore.QRect(860, 30, 61, 61))
        self.refresh_btn.setAutoFillBackground(True)
        self.refresh_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466; \n"
" ")
        self.refresh_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/refresh.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon)
        self.refresh_btn.setIconSize(QtCore.QSize(65, 167))
        self.refresh_btn.setCheckable(True)
        self.refresh_btn.setChecked(False)
        self.refresh_btn.setAutoRepeat(False)
        self.refresh_btn.setAutoExclusive(False)
        self.refresh_btn.setAutoDefault(False)
        self.refresh_btn.setDefault(False)
        self.refresh_btn.setFlat(False)
        self.refresh_btn.setObjectName("refresh_btn")
        self.memorySize_text = QtWidgets.QLineEdit(Form)
        self.memorySize_text.setGeometry(QtCore.QRect(210, 50, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.memorySize_text.setFont(font)
        self.memorySize_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.memorySize_text.setAlignment(QtCore.Qt.AlignCenter)
        self.memorySize_text.setObjectName("memorySize_text")
        self.memorySize_btn = QtWidgets.QPushButton(Form)
        self.memorySize_btn.setGeometry(QtCore.QRect(540, 50, 121, 31))
        self.memorySize_btn.clicked.connect(self.memorySize_click)
        self.memorySize_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.memorySize_btn.setObjectName("memorySize_btn")
        self.holeInfo_btn = QtWidgets.QPushButton(Form)
        self.holeInfo_btn.clicked.connect(self.enter_holes)
        self.holeInfo_btn.setGeometry(QtCore.QRect(540, 170, 121, 31))
        self.holeInfo_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.holeInfo_btn.setObjectName("holeInfo_btn")
        self.holeSize_text = QtWidgets.QLineEdit(Form)
        self.holeSize_text.setGeometry(QtCore.QRect(370, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.holeSize_text.setFont(font)
        self.holeSize_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.holeSize_text.setAlignment(QtCore.Qt.AlignCenter)
        self.holeSize_text.setObjectName("holeSize_text")
        self.tableprocess_btn = QtWidgets.QPushButton(Form)
        self.tableprocess_btn.clicked.connect(self.chosenProcess_click)
        self.tableprocess_btn.setGeometry(QtCore.QRect(300, 470, 200, 50))
        self.tableprocess_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                        " border: 2px solid ;\n"
                                        " border-radius: 10px;\n"
                                        "border-color:#7e7ebd;\n"
                                        "color: #444466;  ")
        self.tableprocess_btn.setObjectName("tableprocess_btn")
        self.tableprocess_text = QtWidgets.QLineEdit(Form)
        self.tableprocess_text.setGeometry(QtCore.QRect(40, 470, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableprocess_text.setFont(font)
        self.tableprocess_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                         " border: 2px solid ;\n"
                                         " border-radius: 10px;\n"
                                         "border-color:#7e7ebd;\n"
                                         "color: #444466;  ")
        self.tableprocess_text.setAlignment(QtCore.Qt.AlignCenter)
        self.tableprocess_text.setObjectName("tableprocess_text")
        self.segTable = QtWidgets.QTableWidget(Form)
        self.segTable.setGeometry(QtCore.QRect(30, 570, 331, 161))
        self.segTable.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.segTable.setObjectName("segTable")
        self.segTable.setColumnCount(3)
        self.segTable.setRowCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.segTable.setHorizontalHeaderItem(2, item)
        self.processNameSegNo_btn = QtWidgets.QPushButton(Form)
        self.processNameSegNo_btn.clicked.connect(self.process_create)
        self.processNameSegNo_btn.setGeometry(QtCore.QRect(540, 270, 121, 31))
        self.processNameSegNo_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.processNameSegNo_btn.setObjectName("processNameSegNo_btn")
        self.processName_text = QtWidgets.QLineEdit(Form)
        self.processName_text.setGeometry(QtCore.QRect(30, 270, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.processName_text.setFont(font)
        self.processName_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.processName_text.setAlignment(QtCore.Qt.AlignCenter)
        self.processName_text.setObjectName("processName_text")
        self.SegNo_text = QtWidgets.QLineEdit(Form)
        self.SegNo_text.setGeometry(QtCore.QRect(290, 270, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SegNo_text.setFont(font)
        self.SegNo_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.SegNo_text.setAlignment(QtCore.Qt.AlignCenter)
        self.SegNo_text.setObjectName("SegNo_text")
        self.FirstFit_btn = QtWidgets.QPushButton(Form)
        self.FirstFit_btn.clicked.connect(self.first_fit_onclick)
        self.FirstFit_btn.setGeometry(QtCore.QRect(80, 420, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.FirstFit_btn.setFont(font)
        self.FirstFit_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.FirstFit_btn.setObjectName("FirstFit_btn")
        self.SegName_text = QtWidgets.QLineEdit(Form)
        self.SegName_text.setGeometry(QtCore.QRect(30, 360, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SegName_text.setFont(font)
        self.SegName_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.SegName_text.setAlignment(QtCore.Qt.AlignCenter)
        self.SegName_text.setObjectName("SegName_text")
        self.SegSize_text = QtWidgets.QLineEdit(Form)
        self.SegSize_text.setGeometry(QtCore.QRect(290, 360, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SegSize_text.setFont(font)
        self.SegSize_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.SegSize_text.setAlignment(QtCore.Qt.AlignCenter)
        self.SegSize_text.setObjectName("SegSize_text")
        self.SegInfo_btn = QtWidgets.QPushButton(Form)
        self.SegInfo_btn.clicked.connect(self.segment_create)
        self.SegInfo_btn.setGeometry(QtCore.QRect(540, 360, 121, 31))
        self.SegInfo_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.SegInfo_btn.setObjectName("SegInfo_btn")
        self.label_hole = QtWidgets.QLabel(Form)
        self.label_hole.setGeometry(QtCore.QRect(30, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_hole.setFont(font)
        self.label_hole.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.label_hole.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hole.setObjectName("label_hole")
        self.label_Process_2 = QtWidgets.QLabel(Form)
        self.label_Process_2.setGeometry(QtCore.QRect(30, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Process_2.setFont(font)
        self.label_Process_2.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.label_Process_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Process_2.setObjectName("label_Process_2")
        self.bestFit_btn = QtWidgets.QPushButton(Form)
        self.bestFit_btn.setGeometry(QtCore.QRect(340, 420, 191, 31))
        font = QtGui.QFont()
        self.bestFit_btn.clicked.connect(self.bestFit_onclick)
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bestFit_btn.setFont(font)
        self.bestFit_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.bestFit_btn.setObjectName("bestFit_btn")
        self.label_segtable = QtWidgets.QLabel(Form)
        self.label_segtable.setGeometry(QtCore.QRect(30, 530, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_segtable.setFont(font)
        self.label_segtable.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.label_segtable.setAlignment(QtCore.Qt.AlignCenter)
        self.label_segtable.setObjectName("label_segtable")
        self.NewAllocation_btn = QtWidgets.QPushButton(Form)
        self.NewAllocation_btn.clicked.connect(self.NewAllocation_click)
        self.NewAllocation_btn.setGeometry(QtCore.QRect(10, 20, 160, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NewAllocation_btn.setFont(font)
        self.NewAllocation_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ; ")
        self.NewAllocation_btn.setObjectName("NewAllocation_btn")
        self.NewProcess_btn = QtWidgets.QPushButton(Form)
        self.NewProcess_btn.clicked.connect(self.newpro)
        self.NewProcess_btn.setGeometry(QtCore.QRect(30, 220, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NewProcess_btn.setFont(font)
        self.NewProcess_btn.setStyleSheet("background-color: rgb(238, 238, 238);\n"
" border: 2px solid ;\n"
" border-radius: 10px;\n"
"border-color:#7e7ebd;\n"
"color: #444466;  ")
        self.NewProcess_btn.setObjectName("NewProcess_btn")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.holeName_text.setPlaceholderText(_translate("Form", "Enter Hole Name"))
        self.holeStart_text.setPlaceholderText(_translate("Form", "Enter Strat Address"))
        self.label_layout_title.setText(_translate("Form", "Memory Layout"))
        self.memorySize_text.setPlaceholderText(_translate("Form", "  Enter Number Memory Size"))
        self.memorySize_btn.setText(_translate("Form", "Enter"))
        self.holeInfo_btn.setText(_translate("Form", "Enter"))
        self.holeSize_text.setPlaceholderText(_translate("Form", "Enter Hole Size"))
        item = self.segTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Segement Name"))
        item = self.segTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Limit"))
        item = self.segTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Base"))
        self.processNameSegNo_btn.setText(_translate("Form", "Enter"))
        self.tableprocess_text.setPlaceholderText(_translate("Form", "  Enter Process Name"))
        self.processName_text.setPlaceholderText(_translate("Form", "  Enter Process Name"))
        self.SegNo_text.setPlaceholderText(_translate("Form", "  Enter Segment Number "))
        self.FirstFit_btn.setText(_translate("Form", "First Fit"))
        self.SegName_text.setPlaceholderText(_translate("Form", "  Enter Segment Name"))
        self.SegSize_text.setPlaceholderText(_translate("Form", "  Enter Segment Size "))
        self.SegInfo_btn.setText(_translate("Form", "Enter"))
        self.tableprocess_btn.setText(_translate("Form", "Enter"))
        self.label_hole.setText(_translate("Form", "Hole"))
        self.label_Process_2.setText(_translate("Form", "Segement"))
        self.bestFit_btn.setText(_translate("Form", "Best Fit"))
        self.label_segtable.setText(_translate("Form", " Segment Table"))
        self.NewAllocation_btn.setText(_translate("Form", "New Allocation"))
        self.NewProcess_btn.setText(_translate("Form", "New Process"))

    def memorySize_click(self):
        MainCode.setMemorysize(int(self.memorySize_text.text()))

    def NewAllocation_click(self):
        MainCode.new_allocation()
        self.memorySize_text.clear()


    def process_create(self):
        MainCode.process_creation(self.processName_text.text(), int(self.SegNo_text.text()), MainCode.process_segments)

    def segment_create(self):
        print("Hi from segment")
        MainCode.segments_creation(self.SegName_text.text(), int(self.SegSize_text.text()), self.processName_text.text())


    def enter_holes(self):
        MainCode.holes_entry(self.holeName_text.text(), int(self.holeStart_text.text()), int(self.holeSize_text.text()))
        self.holeName_text.clear()
        self.holeSize_text.clear()
        self.holeStart_text.clear()

    def newpro(self):
        self.processName_text.clear()
        self.SegNo_text.clear()
    def first_fit_onclick(self):
        error = MainCode.first_fit()
        if error == 1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("There is not enough Holes size for one of the Segments")
            msg.setWindowTitle("Error Message")
            msg.setStandardButtons(QtWidgets.QMessageBox.Close)
            msg.exec()
            print("error")


    def bestFit_onclick(self):
        error = MainCode.best_fit()
        if error == 1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("There is not enough Holes size for one of the Segments")
            msg.setWindowTitle("Error Message")
            msg.setStandardButtons(QtWidgets.QMessageBox.Close)
            msg.exec()
            print("error")


    def update_memory(self, Form):
        j = 0
        name = "memory_btn"
        fn_name = "on_click"
        global boxes
        global start_labels
        global end_labels
        if len(boxes) != 0:
            for i in range(len(boxes)):
                boxes[i].hide()
            for i in range(len(start_labels)):
                start_labels[i].hide()
            for i in range(len(end_labels)):
                end_labels[i].hide()
        boxes.clear()
        start_labels.clear()
        end_labels.clear()
        i = 0
        current = MainCode.Memory
        for h in range(len(current)):
            i = i + 1
            name = name + str(i)
            fn_name = fn_name + str(i)
            print(name)
            print(fn_name)
            self.name = QtWidgets.QCheckBox(Form)
            self.name.show()
            self.name.setGeometry(QtCore.QRect(680, 100 + j, 200, 90))
            self.name.setStyleSheet(" background-color: rgb(238, 238, 238);\n "
                                    " border: 2px solid ;\n"
                                    " border-radius: 1px;\n"
                                    "border-color:#7e7ebd;\n"
                                    "color:  dark blue;\n"
                                    "font-size: 18px;\n"
                                    "font-weight: Bold;")
            self.name.setText(current[h].pid)
            self.name.setCheckable(True)
            boxes.append(self.name)

            self.name.setCheckState(QtCore.Qt.Unchecked)
            self.start_label = QtWidgets.QLabel(Form)
            self.start_label.show()
            self.start_label.setGeometry(QtCore.QRect(685, 105 + j, 100, 20))
            font = QtGui.QFont()
            self.start_label.setFont(font)
            self.start_label.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                           "color: dark blue;\n"
                                           "font-size: 18px;\n"
                                           "font-weight: Bold;"
                                           "")
            self.start_label.setObjectName("label")
            self.start_label.setText(str(current[h].start))
            start_labels.append(self.start_label)
            self.end_label = QtWidgets.QLabel(Form)
            self.end_label.setGeometry(QtCore.QRect(685, 165 + j, 100, 20))
            self.end_label.show()

            font = QtGui.QFont()
            self.end_label.setFont(font)
            self.end_label.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                         "color: dark blue;\n"
                                         "font-size: 18px;\n"
                                         "font-weight: Bold;"
                                         "")
            self.end_label.setObjectName("label")
            if h == len(current)-1:
                self.end_label.setText(str(MainCode.memory_size))
            else:
                self.end_label.setText(str(current[h+1].start))
            end_labels.append(self.end_label)
            self.layout.addWidget(self.start_label)
            self.layout.addWidget(self.name)
            self.layout.addWidget(self.end_label)
            j = j + 90
            print(h)

        print(boxes)
        self.startcheck = QtWidgets.QPushButton(Form)
        self.startcheck.show()
        self.startcheck.setGeometry(QtCore.QRect(400, 600, 200, 50))
        font = QtGui.QFont()
        self.startcheck.setFont(font)
        self.startcheck.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                      " border: 2px solid ;\n"
                                      " border-radius: 10px;\n"
                                      "border-color:#7e7ebd;\n"
                                      "color: #444466;\n  "
                                      "font-size: 18px;\n"
                                      "font-weight:Bold;")
        self.startcheck.setObjectName("startcheck")
        self.startcheck.setText("Start Check")
        self.startcheck.clicked.connect(self.check)
        #print(MainCode.Memory[1].pid)



    def first_layout(self, Form):
        MainCode.memory_first_allocation()
        j = 0
        name = "memory_btn"
        fn_name = "on_click"
        global boxes
        global start_labels
        global end_labels
        if len(boxes) != 0:
            for i in range(len(boxes)):
                boxes[i].hide()
            for i in range(len(start_labels)):
                start_labels[i].hide()
            for i in range(len(end_labels)):
                end_labels[i].hide()
        boxes.clear()
        start_labels.clear()
        end_labels.clear()
        i = 0
        current = MainCode.Memory
        for item in current:
            i = i + 1
            name = name + str(i)
            fn_name = fn_name + str(i)
            self.name = QtWidgets.QCheckBox(Form)
            self.name.show()
            self.name.setGeometry(QtCore.QRect(680, 100 + j, 200, 90))
            self.name.setStyleSheet(" background-color: rgb(238, 238, 238);\n "
                                    "color:  dark blue;\n"
                                    "font-size: 18px;\n"
                                    "font-weight: Bold;")

            self.name.setText(item.pid)
            self.name.setCheckable(True)
            boxes.append(self.name)

            self.name.setCheckState(QtCore.Qt.Unchecked)
            self.start_label = QtWidgets.QLabel(Form)

            self.start_label.show()
            self.start_label.setGeometry(QtCore.QRect(685, 105 + j, 200, 90))
            font = QtGui.QFont()
            self.start_label.setFont(font)
            self.start_label.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                           "color: dark blue;\n"
                                           "font-size: 18px;\n"
                                           "font-weight: Bold;"
                                           "")
            self.start_label.setObjectName("label")

            self.start_label.setText(str(item.start))
            start_labels.append(self.start_label)
            self.end_label = QtWidgets.QLabel(Form)
            self.end_label.setGeometry(QtCore.QRect(685, 165 + j, 100, 90))
            self.end_label.show()
            font = QtGui.QFont()
            self.end_label.setFont(font)
            self.end_label.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                         "color: dark blue;\n"
                                         "font-size: 18px;\n"
                                         "font-weight: Bold;"
                                         "")
            self.end_label.setObjectName("label")
            self.end_label.setText(str(item.start + item.size))
            end_labels.append(self.end_label)
            self.layout.addWidget(self.start_label)
            self.layout.addWidget(self.name)
            self.layout.addWidget(self.end_label)
            j = j + 90
        print(boxes)

        self.startcheck = QtWidgets.QPushButton(Form)
        self.startcheck.show()
        self.startcheck.setGeometry(QtCore.QRect(400, 600, 200, 50))
        font = QtGui.QFont()
        self.startcheck.setFont(font)
        self.startcheck.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                      " border: 2px solid ;\n"
                                      " border-radius: 10px;\n"
                                      "border-color:#7e7ebd;\n"
                                      "color: #444466;\n  "
                                      "font-size: 18px;\n"
                                      "font-weight:Bold;")
        self.startcheck.setObjectName("startcheck")
        self.startcheck.setText("Start Check")
        self.startcheck.clicked.connect(self.check)




    def check(self):
        global boxes
        segment_changed = []
        changed = []
        for i in range(len(boxes)):
                if boxes[i].checkState() == QtCore.Qt.Checked:
                        name = boxes[i].text()
                        #boxes[i].setText("Hole")
                        boxes[i].setCheckState(QtCore.Qt.Unchecked)
                        changed.append(i)
                        print(name)
                        if name[0:3] == "seg":
                            segment_changed.append(name[9:])
        if len(changed) != 0:
            MainCode.update_memory_after_check(changed, segment_changed)

        # segment table

    def show_segmentTable(self):
        s = 0
        length = len(MainCode.Process_Segments_Bases)
        while s < length:
            self.segTable.setItem(s, 0, QTableWidgetItem(MainCode.Process_Segments_Names[s]))
            self.segTable.setItem(s, 1, QTableWidgetItem(str(MainCode.Process_Segments_Limits[s])))
            self.segTable.setItem(s, 2, QTableWidgetItem(str(MainCode.Process_Segments_Bases[s])))
            s += 1
        MainCode.Process_Segments_Names = []
        MainCode.Process_Segments_Limits = []
        MainCode.Process_Segments_Bases = []
        print("show_segmentTable")

    def chosenProcess_click(self):
        MainCode.chosen_process(self.tableprocess_text.text())
        MainCode.segments_table()
        self.show_segmentTable()
        print("chosenProcess_click")

import img
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())