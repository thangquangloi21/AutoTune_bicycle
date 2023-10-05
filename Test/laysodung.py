import csv
import math

import pandas as pd

def xulydatas(data):
    combined_values = {}
    bang = pd.read_csv(data)
    # df = pd.read_csv(map)
    for index, row in bang.iterrows():
        # Trích xuất các giá trị từ các cột cụ thể
        tps = row['TP (%)']
        rpm = row['RPM']
        afr = row['Lambda (AFR)']
        rpm = int(round(rpm / 500) * 500)
        tps = math.floor(tps)
        print(f"tp = {tps}, rpm = {rpm}, afr = {afr}")
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
    combined_df.to_csv('out1.csv', index=False)
def working_tone(data1, afrs, Map):
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

                        # Tìm vị trí của tp và rpm trong danh sách giá trị cột và hàng
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
                        # df.at[tp_index, rpm_index] = x

                        # Lưu DataFrame cập nhật vào tệp CSV
                        df.to_csv(Map, header=None, index=None)
                        print(f"Giá trị tại TP (%) = {tps} và RPM = {rpm} đã được cập nhật thành: {x} với afr: {afr}")
    print(f"Tổng số giá trị đã thay đổi: {changed_values_count}")
# xulydatas(data="../Data_IN/so4.csv")
xulydatas(data="../Data_IN/testtt.csv")
working_tone(data1="out1.csv", afrs=12.5, Map="map1.csv")