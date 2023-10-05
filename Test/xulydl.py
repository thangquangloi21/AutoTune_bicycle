import pandas as pd


def xulydata(data1, afrs, file_path):
    # Lặp qua từng hàng trong bảng dữ liệu
    # bang = pd.read_excel(data1)
    bang = pd.read_csv(data1)
    # df = pd.read_csv(map)
    for index, row in bang.iterrows():
        # Trích xuất các giá trị từ các cột cụ thể
        tp = row['TP (%)']
        rpm = row['RPM']
        afr = row['Lambda (AFR)']
        print(f"tp = {tp}, rpm = {rpm}, afr = {afr}")
        rpm = int(round(rpm / 500) * 500)
        df = pd.read_csv(file_path, sep=',', header=None, skipinitialspace=True)

        # Lấy tất cả giá trị trong cột đầu tiên và hàng đầu tiên
        first_row = df.iloc[0, 1:].tolist()  # Lấy giá trị từ cột 2 trở đi (bỏ giá trị đầu tiên)
        first_column = df.iloc[1:, 0].tolist()  # Lấy giá trị từ hàng 2 trở đi (bỏ giá trị đầu tiên)
        for i in first_column:
            if tp == i:
                for j in first_row:
                    if j == rpm:
                        # Tìm vị trí của tp và rpm trong danh sách giá trị cột và hàng
                        try:
                            tp_index = first_column.index(tp) + 1
                        except Exception as error:

                            print(f"Không tìm thấy giá trị TP (%) = {tp} với lỗi :{error}")
                        try:
                            rpm_index = first_row.index(rpm) + 1
                        except Exception as error:
                            print(f"Không tìm thấy giá trị RPM = {rpm} với lỗi: {error}")
                        # Lấy giá trị tại vị trí đã tìm thấy
                        value = df.iloc[tp_index, rpm_index]
                        x = value * (afr / afrs)
                        x = round(x, 2)

                        # Thay thế giá trị tại vị trí đã tìm thấy bằng x
                        df.at[tp_index, rpm_index] = x

                        # Lưu DataFrame cập nhật vào tệp CSV
                        df.to_csv(file_path, header=None, index=None)
                        print(f"lúc đầu: {value}")
                        print(f"Giá trị tại TP (%) = {tp} và RPM = {rpm} đã được cập nhật thành: {x} với afr: {afr}")





data = "Data_IN/Book1.csv"
afrs = 12.5
file_map = "../APP/DATA/map1.csv"
xulydata(data, afrs, file_map)
# Đọc nội dung từ tệp văn bản thứ nhất
file1_path = '../APP/DATA/dau.txt'
with open(file1_path, 'r') as file1:
    content1 = file1.read()

# Đọc nội dung từ tệp văn bản thứ hai
file2_path = '../APP/DATA/output.txt'
with open(file2_path, 'r') as file2:
    content2 = file2.read()

# Ghép nội dung của các tệp vào nhau
merged_content = content1 + content2

# Ghi nội dung đã ghép vào tệp mới
merged_file_path = 'merged.tqECU'
with open(merged_file_path, 'w') as merged_file:
    merged_file.write(merged_content)
