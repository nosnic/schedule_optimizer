from PyQt5.QtWidgets import QDialog
from templates.InfoWindow import Ui_InfoWindow
import json


class InfoEditingWindow(QDialog, Ui_InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.back_to_main_window)
        self.pushButton_save.clicked.connect(self.create_lession)
        self.status = ""

    def back_to_main_window(self):
        self.close()

    def create_lession(self):
        with open("data/classes.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        lession = self.lineEdit_name.text()
        lessionInfo = {}
        lessionInfo["teacher"] = float(self.doubleSpinBox_prepod.value())
        lessionInfo["session"] = int(self.checkBox_session.isChecked())
        lessionInfo["profile"] = int(self.checkBox_profile.isChecked())
        lessionInfo["notable"] = int(self.checkBox_notable.isChecked())
        lessionInfo["lecture"] = int(self.checkBox_lection.isChecked())
        lessionInfo["practica"] = (lessionInfo["lecture"] + 1) % 2
        lessionInfo["dopsa"] = float(self.doubleSpinBox_dopsa.value())
        data[lession] = lessionInfo
        with open("data/classes.json", 'w', encoding='utf-8') as f:
            json.dump(data, f,
                      sort_keys=False,
                      indent=4,
                      ensure_ascii=False,
                      separators=(',', ': ')
                      )
