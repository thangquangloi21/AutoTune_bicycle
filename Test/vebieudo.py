import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, \
    QTableWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, \
            QVBoxLayout, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.setFixedSize(1080, 720)
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

        # layout = QVBoxLayout(central_widget)
        # tableWidget = QTableWidget(14, 30)
        # layout.addWidget(tableWidget)
        # # tableWidget.setGeometry(400, 200)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())