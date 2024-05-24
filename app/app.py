from PyQt5.QtWidgets import QMainWindow, QDialog, QTableWidgetItem
from app.data_part import TableWorker
from app.algorithm_part import SmartPart
from app.info_editing_window import InfoEditingWindow
from app.time_table import TimeTable
from templates.Smart_time_table import Ui_SmartTimeTable
from templates.timetable_view import Ui_Form


class MainWindow(QMainWindow, Ui_SmartTimeTable):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_open_tables.clicked.connect(self.show_timetable)
        self.button_start.clicked.connect(self.working)
        self.button_file_output.clicked.connect(self.saving)
        self.button_change_tables.clicked.connect(self.editing_info)
        self.timetable = TimeTable()
        self.timetable_view = TimetableView()
        self.info_editing_window = InfoEditingWindow()
        self.result_table = []

    def show_timetable(self):
        self.timetable.exec_()
        self.label_status_output.setText(self.timetable.status)

    def working(self):
        if self.timetable.table and self.timetable.infoTable:
            print("Start working")
            nerd = SmartPart()
            weights = nerd.find_weights(self.timetable.table)
            self.result_table = nerd.create_new_table(self.timetable.infoTable, weights)
            self.timetable_view.load_result(self.result_table)
            self.label_status_output.setText("Расписание оптимизировано, но не сохранено")
            print("End working")
        else:
            self.label_status_output.setText("Расписание ещё не загружено")

    def saving(self):
        self.timetable_view.set_timetable(self.result_table)
        self.timetable_view.exec_()
        self.label_status_output.setText(self.timetable_view.status)

    def editing_info(self):
        self.info_editing_window.exec_()


class TimetableView(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.back_to_main_window)
        self.pushButton_save_in_file.clicked.connect(self.save_in_file)
        self.status = "Расписание оптимизировано, но не сохранено"
        self.timetable = None

    def load_result(self, timetable):
        self.timetable = timetable
        for i in range(6):
            for j in range(6):
                item = QTableWidgetItem()
                item.setText(timetable[i][j])
                self.tableWidget.setItem(i, j, item)

    def set_timetable(self, timetable):
        self.timetable = timetable

    def back_to_main_window(self):
        self.close()

    def save_in_file(self):
        if self.timetable:
            worker = TableWorker()
            worker.save_table(self.timetable, "result.xlsx")
            self.status = "Расписание оптимизировано и сохранено"
            print("saving completed")
        else:
            print("No timetable to save")
