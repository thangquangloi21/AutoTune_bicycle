import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class CSVViewer(QMainWindow):
    def __init__(self, filename):
        super().__init__()
        self.initUI()
        self.loadCSV(filename)

    def initUI(self):
        self.setWindowTitle("CSV Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout(self.centralWidget)

        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

    def loadCSV(self, filename):
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                self.tableWidget.setItem(row_idx, col_idx, item)

def main():
    app = QApplication(sys.argv)
    filename = "../APP/DATA/map1.csv"  # Thay đổi thành đường dẫn của tệp CSV của bạn
    viewer = CSVViewer(filename)
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
