import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        from working_thread import Working_thread
        super().__init__()

        self.Workingthread = Working_thread
        self.setFixedSize(550, 230)
        self.setWindowTitle("Auto Tune")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        data_txt = QLabel("Data:", central_widget)
        data_txt.setGeometry(10, 10, 79, 28)

        self.textbox_data = QLineEdit(central_widget)
        self.textbox_data.setGeometry(120, 10, 254, 28)
        self.textbox_data.setPlaceholderText(".csv")

        map_txt = QLabel("Input File.tqECU:", central_widget)
        map_txt.setGeometry(10, 50, 88, 28)

        self.textbox_map = QLineEdit(central_widget)
        self.textbox_map.setGeometry(120, 50, 254, 28)
        self.textbox_map.setPlaceholderText(".tqECU")

        data_open_btn = QPushButton("Open file", central_widget)
        data_open_btn.setGeometry(410, 10, 100, 30)

        map_open_btn = QPushButton("Open file", central_widget)
        map_open_btn.setGeometry(410, 50, 100, 30)

        tinh_btn = QPushButton("Tune", central_widget)
        tinh_btn.setGeometry(200, 150, 100, 30)

        self.map_box = QComboBox(central_widget)
        self.map_box.setGeometry(150, 100, 50, 25)
        self.map_box.addItem("map1")
        self.map_box.addItem("map2")
        self.map_box.addItem("map3")
        self.map_box.addItem("map4")
        self.map_box.setCurrentIndex(0)

        self.afr_box = QComboBox(central_widget)
        self.afr_box.setGeometry(400, 100, 50, 25)
        self.afr_box.addItem("12.3")
        self.afr_box.addItem("12.4")
        self.afr_box.addItem("12.5")
        self.afr_box.addItem("12.6")
        self.afr_box.addItem("12.7")
        self.afr_box.addItem("12.8")
        self.afr_box.setCurrentIndex(2)

        map_txt = QLabel("Map:", central_widget)
        map_txt.setGeometry(70, 100, 100, 30)

        afr_txt = QLabel("AFR:", central_widget)
        afr_txt.setGeometry(300, 100, 100, 30)

        # Kết nối sự kiện nhấn nút "Tính" với hàm calculate
        tinh_btn.clicked.connect(self.Tune)
        data_open_btn.clicked.connect(self.open_file_data)
        map_open_btn.clicked.connect(self.open_file_ecu)

    def Tune(self):
        try:
            # get data
            data = self.textbox_data.text()
            afr = self.afr_box.currentText()
            maps = f"DATA/{self.map_box.currentText()}.csv"
            print(maps)
            # Xử lý logic khi người dùng nhấn nút "Tính"
            self.Workingthread.xulydatas(self, data)
            self.Workingthread.working_tone(self, data1="DATA/data.csv", afrs=afr, Map=maps)
            self.Workingthread.output(self, maps)
            self.Workingthread.xuatfile(self)
            self.textbox_data.clear()
            self.textbox_map.clear()
        except Exception as error:
            QMessageBox.about(self, "Title", "ERROR : {}".format(error))
            print(error)

    def open_file_data(self):
        try:
            self.link_data = self.Workingthread.open_file_data(self)
            self.textbox_data.setText(self.link_data)
        except Exception as error:
            QMessageBox.about(self, "Title", "ERROR : {}".format(error))
            print(error)

    def open_file_ecu(self):
        try:
            link_ecu = self.Workingthread.open_file_map(self)
            self.textbox_map.setText(link_ecu)
            self.Workingthread.xuly_map(self, link_ecu)
        except Exception as error:
            QMessageBox.about(self, "Title", "ERROR : {}".format(error))
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
