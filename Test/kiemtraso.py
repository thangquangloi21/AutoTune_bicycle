import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class SaveFileWithCustomExtension(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Export File with Custom Extension')
        self.setGeometry(100, 100, 400, 200)

        self.export_button = QPushButton('Export File', self)
        self.export_button.setGeometry(150, 80, 100, 40)
        self.export_button.clicked.connect(self.exportToFile)

    def exportToFile(self):
        merged_content = "This is the content to export to the file."
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog(self, 'Export File', '', 'Custom Files (*.tqECU);;All Files (*)', options=options)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            if not file_path.endswith(".tqECU"):
                file_path += ".tqECU"  # Thêm phần mở rộng nếu nó không tồn tại

            try:
                with open(file_path, 'w') as file:
                    file.write(merged_content)
                print(f'File exported to: {file_path}')
            except Exception as e:
                print(f'Error exporting file: {str(e)}')

def main():
    app = QApplication(sys.argv)
    window = SaveFileWithCustomExtension()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    merged_content = "This is the content to export to the file."
    main()
