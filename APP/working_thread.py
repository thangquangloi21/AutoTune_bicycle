import csv
import math
import shutil

import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Working_thread():
    def __init__(self):
        super().__init__()
        ...

    # topview_file
    def open_file_data(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Open Data", "~", "Sound Files (*.csv)")
        # Kiểm tra xem người dùng đã chọn tệp hay chưa
        if filepath:
            print("Full URL của tệp đã chọn:", filepath)
            QMessageBox.about(self, "Thông Báo", "Đã đọc xong")
        else:
            QMessageBox.about(self, "Thông Báo", "Chưa có gì")
        return filepath
    def open_file_map(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Open Map", "~", "Sound Files (*.tqECU)")
        # Kiểm tra xem người dùng đã chọn tệp hay chưa
        if filepath:
            print("Full URL của tệp đã chọn:", filepath)
        return filepath

    def xuly_map(self, duong_dan_tep_tin_cu):
        try:
            # Đường dẫn mới với đuôi .txt
            duong_dan_tep_tin_moi = 'DATA/ecus.csv'
            # Sao chép nội dung của tệp tin gốc vào tệp tin mới
            shutil.copy(duong_dan_tep_tin_cu, duong_dan_tep_tin_moi)
            # Mở file CSV để đọc với delimiter là '&'
            with open('DATA/ecus.csv', mode='r', newline='') as file:
                csv_reader = csv.reader(file, delimiter='&')
                data = list(csv_reader)
            # Xóa
            dau = 13
            cuoi = 72
            du_lieu_can_lay = data[dau - 1:cuoi]
            # Luu vao
            with open('DATA/ecus.csv', mode='w', newline='') as file:
                # Tạo đối tượng ghi CSV
                csv_writer = csv.writer(file)
                # Ghi dữ liệu vào file CSV
                csv_writer.writerows(du_lieu_can_lay)
            with open('DATA/ecus.csv', mode='r', newline='') as file:
                csv_reader = csv.reader(file, delimiter=',')
                data = list(csv_reader)
            # map 1
            dau = 2
            cuoi = 15
            map1 = data[dau - 1:cuoi]
            # Xóa cột đầu tiên trong map1
            for i in range(len(map1)):
                map1[i] = map1[i][1:]

            df = pd.DataFrame(map1,
                              columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000',
                                       '5500', '6000', '6500',
                                       '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000',
                                       '11500',
                                       '12000', '12500',
                                       '13000', '13500', '14000', '14500', '15000'])
            df.index = ['100', '90', '80', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
            df.to_csv('DATA/map1.csv', index=True)
            # map 2
            dau = 17
            cuoi = 30
            map2 = data[dau - 1:cuoi]
            # Xóa cột đầu tiên trong map1
            for i in range(len(map2)):
                map2[i] = map2[i][1:]
            df = pd.DataFrame(map2,
                              columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000',
                                       '5500',
                                       '6000', '6500',
                                       '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000',
                                       '11500',
                                       '12000', '12500',
                                       '13000', '13500', '14000', '14500', '15000'])
            df.index = ['100', '90', '80', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
            df.to_csv('DATA/map2.csv', index=True)

            # map 3
            dau = 32
            cuoi = 45
            map3 = data[dau - 1:cuoi]
            # Xóa cột đầu tiên trong map1
            for i in range(len(map3)):
                map3[i] = map3[i][1:]
            df = pd.DataFrame(map3,
                              columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000',
                                       '5500',
                                       '6000', '6500',
                                       '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000',
                                       '11500',
                                       '12000', '12500',
                                       '13000', '13500', '14000', '14500', '15000'])
            df.index = ['100', '90', '80', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
            df.to_csv('DATA/map3.csv', index=True)

            # map 4
            dau = 47
            cuoi = 60
            map4 = data[dau - 1:cuoi]
            # Xóa cột đầu tiên trong map1
            for i in range(len(map4)):
                map4[i] = map4[i][1:]

            df = pd.DataFrame(map4,
                              columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000',
                                       '5500',
                                       '6000', '6500',
                                       '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000',
                                       '11500',
                                       '12000', '12500',
                                       '13000', '13500', '14000', '14500', '15000'])
            df.index = ['100', '90', '80', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
            df.to_csv('DATA/map4.csv', index=True)
            QMessageBox.about(self, "Thông Báo ECU", "Xong")
            return
        except Exception as error:
            QMessageBox.about(self, "Title", "ERROR : {}".format(error))
            print(f"inpur error: {error}")



    def working_tone(self, data1, afrs, Map):
        changed_values_count = 0  # Khởi tạo biến đếm
        # Lặp qua từng hàng trong bảng dữ liệu
        # bang = pd.read_excel(data1)
        bang = pd.read_csv(data1)
        # df = pd.read_csv(map)
        for index, row in bang.iterrows():
            # Trích xuất các giá trị từ các cột cụ thể
            tps = row['TP (%)']
            rpm = row['RPM']
            afr = row['Lambda (AFR)']
            # print(f"tp = {tps}, rpm = {rpm}, afr = {afr}")
            # tps = math.floor(tps)
            # rpm = int(round(rpm / 500) * 500)
            # print(f"lam tron rpm {rpm} tp: {tp}")
            df = pd.read_csv(Map, sep=',', header=None, skipinitialspace=True)
            # Lấy tất cả giá trị trong cột đầu tiên và hàng đầu tiên
            first_row = df.iloc[0, 1:].tolist()  # Lấy giá trị từ cột 2 trở đi (bỏ giá trị đầu tiên)
            first_column = df.iloc[1:, 0].tolist()  # Lấy giá trị từ hàng 2 trở đi (bỏ giá trị đầu tiên)
            for i in first_column:
                if tps == i:
                    for j in first_row:
                        if j == rpm:
                            try:
                                tp_index = first_column.index(tps) + 1
                            except Exception as error:

                                print(f"Không tìm thấy giá trị TP (%) = {tps} với lỗi :{error}")
                            try:
                                rpm_index = first_row.index(rpm) + 1
                            except Exception as error:
                                print(f"Không tìm thấy giá trị RPM = {rpm} với lỗi: {error}")
                            # Lấy giá trị tại vị trí đã tìm thấy
                            value = df.iloc[tp_index, rpm_index]
                            print(f"lúc đầu: {value}")
                            afr = float(afr)
                            afrs = float(afrs)
                            x = value * (afr / afrs)
                            x = round(x, 2)
                            if x != value:
                                changed_values_count += 1
                            # Thay thế giá trị tại vị trí đã tìm thấy bằng x
                            df.at[tp_index, rpm_index] = x
                            # Lưu DataFrame cập nhật vào tệp CSV
                            df.to_csv(Map, header=None, index=None)
                            print(
                                f"Giá trị tại TP (%) = {tps} và RPM = {rpm} đã được {round(x - value,2)} cập nhật thành: {x} với afr: {afr}")
        print(f"Tổng số giá trị đã thay đổi: {changed_values_count}")

    def output(self, map_out):
        df = pd.read_csv(map_out, header=None)
        output_txt_file_path = 'DATA/output.txt'
        # Xóa hàng đầu tiên và cột đầu tiên
        df = df.iloc[1:, 1:]
        # Lưu DataFrame vào tệp văn bản với delimiter mặc định (,) tạm thời
        txt_file_path = 'DATA/maps.csv'
        df.to_csv(txt_file_path, sep=',', index=False, header=False)
        # Đọc lại tệp văn bản và thay thế delimiter từ , sang &
        with open(txt_file_path, 'r') as file:
            content = file.read()
        content = content.replace(',', '&')
        # Lưu lại tệp văn bản với delimiter '&'
        with open(output_txt_file_path, 'w') as file:
            file.write(content)
        # thêm & vào đầu dòng
        # Đọc nội dung tệp văn bản
        with open(output_txt_file_path, 'r') as file:
            lines = file.readlines()
        # Thêm ký tự '&' vào đầu mỗi dòng nếu chưa có
        formatted_lines = []
        for line in lines:
            if not line.startswith('&'):
                line = '&' + line
            formatted_lines.append(line.strip())
        # Ghi lại nội dung đã cập nhật vào tệp văn bản
        with open(output_txt_file_path, 'w') as file:
            file.write('\n'.join(formatted_lines))
        # Đọc nội dung tệp văn bản
        with open(output_txt_file_path, 'r') as file:
            input_lines = file.readlines()
        # Tách chuỗi thành danh sách các số và xử lý từng phần tử
        formatted_numbers = []
        for line in input_lines:
            numbers = line.strip().split('&')  # Tách dòng thành các số bằng ký tự "&"
            formatted_parts = []
            for number in numbers:
                parts = number.strip().split('.')
                if len(parts) == 2 and len(parts[1]) == 1:
                    formatted_parts.append(f"{parts[0]}.{parts[1]}0")
                else:
                    formatted_parts.append(number)
            formatted_line = ' &'.join(formatted_parts)  # Ghép các số lại thành một dòng
            formatted_numbers.append(formatted_line)
        # Ghép danh sách các dòng đã được định dạng lại thành một chuỗi mới
        formatted_str = '\n'.join(formatted_numbers)
        with open(output_txt_file_path, 'w') as output_file:
            output_file.write(formatted_str)
        # Đọc nội dung tệp văn bản
        with open(output_txt_file_path, 'r') as file:
            lines = file.readlines()
        # Loại bỏ khoảng trắng ở đầu mỗi dòng
        formatted_lines = [line.lstrip() for line in lines]
        # Ghi lại nội dung đã cập nhật vào tệp văn bản
        with open(output_txt_file_path, 'w') as file:
            file.writelines(formatted_lines)
        # Đọc nội dung tệp văn bản
        with open(output_txt_file_path, 'r') as file:
            lines = file.readlines()
        # Thêm dấu cách vào cuối mỗi dòng
        formatted_lines = [line.rstrip() + ' ' for line in lines]
        # Ghi lại nội dung đã cập nhật vào tệp văn bản
        with open(output_txt_file_path, 'w') as file:
            file.writelines(formatted_lines)

    def xuatfile(self):
        # Đọc nội dung từ tệp văn bản thứ nhất
        file1_path = 'DATA/dau.txt'
        with open(file1_path, 'r') as file1:
            content1 = file1.read()

        # Đọc nội dung từ tệp văn bản thứ hai
        file2_path = 'DATA/output.txt'
        with open(file2_path, 'r') as file2:
            content2 = file2.read()

        # Ghép nội dung của các tệp vào nhau
        merged_content = content1 + content2

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
        # # Ghi nội dung đã ghép vào tệp mới
        # merged_file_path = 'mapok.tqECU'
        # with open(merged_file_path, 'w') as merged_file:
        #     merged_file.write(merged_content)


    def xulydatas(self, data):
        combined_values = {}
        bang = pd.read_csv(data)
        # df = pd.read_csv(map)
        for index, row in bang.iterrows():
            # Trích xuất các giá trị từ các cột cụ thể
            tps = row['TP (%)']
            rpm = row['RPM']
            afr = row['Lambda (AFR)']
            rpm = int(round(rpm / 500) * 500)
            if tps >= 17:
                tps = 10 * round(tps / 10)

            elif 1 <= tps <= 3:
                tps = 2

            elif 4 <= tps <= 6:
                tps = 5

            elif 7 <= tps <= 11:
                tps = 8

            elif 12 <= tps <= 16:
                tps = 14
            # print(f"tp = {tps}, rpm = {rpm}, afr = {afr}")
            # Tạo khóa duy nhất dựa trên x và y
            key = f'{tps}_{rpm}'
            # Kiểm tra xem khóa đã tồn tại trong từ điển chưa
            if key in combined_values:
                # Nếu đã tồn tại, thì cập nhật giá trị z của khóa đó
                combined_values[key][2] = afr
            else:
                # Nếu chưa tồn tại, thêm khóa mới vào từ điển
                combined_values[key] = [tps, rpm, afr]
        # Chuyển đổi từ điển thành danh sách để viết lại thành tệp CSV
        combined_data = list(combined_values.values())
        # Ghi lại vào tệp CSV sau khi gộp
        # Chuyển đổi từ điển thành danh sách để tạo DataFrame
        combined_data = list(combined_values.values())
        combined_df = pd.DataFrame(combined_data, columns=['TP (%)', 'RPM', 'Lambda (AFR)'])
        # Ghi lại vào tệp CSV sau khi gộp
        combined_df.to_csv('DATA/data.csv', index=False)