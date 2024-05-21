from PyQt5.QtWidgets import QMainWindow
from DumbPart import TableWorker
from CleverPart import SmartAss
from templates.Smart_time_table import Ui_SmartTimeTable
from TimeTable import TimeTable
from PyQt5.QtWidgets import QDialog
from templates.timetable_view import Ui_Form
from PyQt5.QtWidgets import QTableWidgetItem
from InfoEditingWindow import InfoEditingWindow

resultTable = []


class MainWindow(QMainWindow, Ui_SmartTimeTable):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_open_tables.clicked.connect(self.show_timetable)
        self.button_start.clicked.connect(self.working)
        self.button_file_output.clicked.connect(self.saving)
        self.button_change_tables.clicked.connect(self.editingInfo)
        self.infoTable = []
        self.table = []
        self.timetable = TimeTable()
        self.timetable_view = TimetableView()
        self.infoEditingWindow = InfoEditingWindow()

    def show_timetable(self):
        self.timetable.exec_()
        self.label_status_output.setText(self.timetable.status)

    def working(self):
        if self.timetable.table != [] and self.timetable.infoTable != []:
            global resultTable
            print("Start working")
            nerd = SmartAss()
            weights = nerd.find_weights(self.timetable.table)
            print(weights)
            resultTable = nerd.createNewTable(self.timetable.infoTable, weights)
            print(self.timetable.infoTable)
            self.timetable_view.load_result()
            self.label_status_output.setText("Расписание оптимизировано, но не сохранено")
            print("End working")
        else:
            self.label_status_output.setText("Расписание ещё не загружено")

    def saving(self):
        self.timetable_view.exec_()
        self.label_status_output.setText(self.timetable_view.status)

    def editingInfo(self):
        self.infoEditingWindow.exec_()


class TimetableView(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.back_to_main_window)
        self.pushButton_save_in_file.clicked.connect(self.save_in_file)
        self.status = "Расписание оптимизировано, но не сохранено"

    def load_result(self):
        global resultTable
        timetable = resultTable
        for i in range(6):
            for j in range(6):
                item = QTableWidgetItem()
                item.setText(timetable[i][j])
                self.tableWidget.setItem(i, j, item)

    def back_to_main_window(self):
        self.close()

    def save_in_file(self):
        worker = TableWorker()
        global resultTable
        worker.save_table(resultTable, "result.xlsx")
        self.status = "Расписание оптимизировано и сохранено"
        print("saving completed")