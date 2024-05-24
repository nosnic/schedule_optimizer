from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from templates.timetable import Ui_Form
from app.data_part import TableWorker
from PyQt5 import QtCore

class TimeTable(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table = []
        self.infoTable = []
        self.pushButton_load_from_file.clicked.connect(self.load_from_file)
        self.pushButton_back.clicked.connect(self.back_to_main_window)
        self.pushButton_save.clicked.connect(self.save_data)
        self.status = "Входное расписание не сохранено"
        self.saving_lessons = []

    def load_from_file(self):
        print("Start loading")
        worker = TableWorker()
        table = worker.read_table("data/table1.xlsx", "data/classes.json")
        infoTable = worker.readonly_table("data/table1.xlsx")
        for i in range(6):
            for j in range(6):
                item = QTableWidgetItem(infoTable[i][j])
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.tableWidget.setItem(i, j, item)
        print("Loading complete")

    def back_to_main_window(self):
        self.close()

    def save_data(self):
        worker = TableWorker()
        timetable_tmp = []
        for i in range(6):
            timetable_tmp.append([])
            for j in range(6):
                if self.tableWidget.item(i, j).checkState() == QtCore.Qt.Checked:
                    self.saving_lessons.append([i, j])
                timetable_tmp[i].append(self.tableWidget.item(i, j).text().strip())
        result = worker.create_info_table(timetable_tmp, "data/classes.json", self.saving_lessons)
        if isinstance(result, str):
            self.status = result + " не найден в информации по предметам"
        else:
            self.infoTable = timetable_tmp
            self.table = result
            self.status = "Входное расписание сохранено"
            print("Saving completed")
