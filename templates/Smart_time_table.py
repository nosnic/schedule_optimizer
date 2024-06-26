# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Smart_time_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SmartTimeTable(object):
    def setupUi(self, SmartTimeTable):
        SmartTimeTable.setObjectName("SmartTimeTable")
        SmartTimeTable.resize(442, 365)
        SmartTimeTable.setStyleSheet("background-color: rgb(74, 112, 139);")
        self.centralwidget = QtWidgets.QWidget(SmartTimeTable)
        self.centralwidget.setObjectName("centralwidget")
        self.button_open_tables = QtWidgets.QPushButton(self.centralwidget)
        self.button_open_tables.setGeometry(QtCore.QRect(10, 10, 421, 34))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/user/PycharmProjects/schedule_optimizer/img/timetable_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SmartTimeTable.setWindowIcon(icon)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.button_open_tables.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_open_tables.setFont(font)
        self.button_open_tables.setStyleSheet("background-color: rgb(108, 166, 205);\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 3 8px;")
        self.button_open_tables.setObjectName("button_open_tables")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(10, 130, 421, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.button_start.setFont(font)
        self.button_start.setStyleSheet("background-color: rgb(108, 166, 205);\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 3 8px;\n"
"")
        self.button_start.setObjectName("button_start")
        self.button_file_output = QtWidgets.QPushButton(self.centralwidget)
        self.button_file_output.setGeometry(QtCore.QRect(10, 190, 421, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.button_file_output.setFont(font)
        self.button_file_output.setStyleSheet("background-color: rgb(108, 166, 205);\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 3 8px;\n"
"\n"
"\n"
"")
        self.button_file_output.setObjectName("button_file_output")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(10, 250, 71, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 112, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_status.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("")
        self.label_status.setObjectName("label_status")
        self.label_status_output = QtWidgets.QLabel(self.centralwidget)
        self.label_status_output.setGeometry(QtCore.QRect(10, 270, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.label_status_output.setFont(font)
        self.label_status_output.setStyleSheet("")
        self.label_status_output.setText("")
        self.label_status_output.setObjectName("label_status_output")
        self.button_change_tables = QtWidgets.QPushButton(self.centralwidget)
        self.button_change_tables.setGeometry(QtCore.QRect(10, 70, 421, 34))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 166, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.button_change_tables.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_change_tables.setFont(font)
        self.button_change_tables.setStyleSheet("background-color: rgb(108, 166, 205);\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 3 8px;")
        self.button_change_tables.setObjectName("button_change_tables")
        SmartTimeTable.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SmartTimeTable)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 24))
        self.menubar.setObjectName("menubar")
        SmartTimeTable.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SmartTimeTable)
        self.statusbar.setObjectName("statusbar")
        SmartTimeTable.setStatusBar(self.statusbar)
        self.action_load_from_file = QtWidgets.QAction(SmartTimeTable)
        self.action_load_from_file.setObjectName("action_load_from_file")

        self.retranslateUi(SmartTimeTable)
        QtCore.QMetaObject.connectSlotsByName(SmartTimeTable)

    def retranslateUi(self, SmartTimeTable):
        _translate = QtCore.QCoreApplication.translate
        SmartTimeTable.setWindowTitle(_translate("SmartTimeTable", "Умное расписание"))
        self.button_open_tables.setText(_translate("SmartTimeTable", "Создать входное расписание"))
        self.button_start.setText(_translate("SmartTimeTable", "Оптимизировать расписание"))
        self.button_file_output.setText(_translate("SmartTimeTable", "Посмотреть оптимизированное расписание"))
        self.label_status.setText(_translate("SmartTimeTable", "Статус:"))
        self.button_change_tables.setText(_translate("SmartTimeTable", "Изменить информацию по предметам"))
        self.action_load_from_file.setText(_translate("SmartTimeTable", "Load from file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmartTimeTable = QtWidgets.QMainWindow()
    ui = Ui_SmartTimeTable()
    ui.setupUi(SmartTimeTable)
    SmartTimeTable.show()
    sys.exit(app.exec_())
