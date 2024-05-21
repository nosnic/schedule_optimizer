from PyQt5.QtWidgets import QDialog
from templates.timetable import Ui_Form
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from DumbPart import TableWorker
from PyQt5 import QtCore, QtGui

class TimeTable(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table= []
        self.infoTable = []
        self.pushButton_load_from_file.clicked.connect(self.load_from_file)
        self.pushButton_back.clicked.connect(self.back_to_main_window)
        self.pushButton_save.clicked.connect(self.save_data)
        self.status = "Входное расписание не сохранено"
        self.saving_lessions = []


    def load_from_file(self):
        print("Start loading")
        worker = TableWorker()
        table = worker.read_table("table1.xlsx", "classes.json")
        infoTable = worker.readonly_table("table1.xlsx")
        for i in range(6):
            for j in range(6):
                item = QTableWidgetItem()
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setText(infoTable[i][j])
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.tableWidget.setItem(i, j, item)
        print("Loading complete")

    def back_to_main_window(self):
        self.close()

    def save_data(self):
        worker = TableWorker()
        timetableTmp = []
        for i in range(6):
            timetableTmp.append([])
            for j in range(6):
                if self.tableWidget.item(i, j).checkState() == 2 :
                    self.saving_lessions.append([i, j])
                timetableTmp[i].append(self.tableWidget.item(i, j).text().strip())
        result = worker.create_info_table(timetableTmp, "classes.json", self.saving_lessions)
        if str(type(result)) == "<class 'str'>":
            self.status = result + " не найден в информации по предметам"
        else:
            self.infoTable = timetableTmp
            self.table = result
            self.status = "Входное расписание сохранено"
            print("saving completed")