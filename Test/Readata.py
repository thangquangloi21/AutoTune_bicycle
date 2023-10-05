import pandas as pd

def readdata(tp, rpm, afr, afrs, file_path):
    df = pd.read_csv(file_path, sep=',', header=None, skipinitialspace=True)

    # Lấy tất cả giá trị trong cột đầu tiên và hàng đầu tiên
    first_row = df.iloc[0, 1:].tolist()  # Lấy giá trị từ cột 2 trở đi (bỏ giá trị đầu tiên)
    first_column = df.iloc[1:, 0].tolist()  # Lấy giá trị từ hàng 2 trở đi (bỏ giá trị đầu tiên)

    # Tìm vị trí của tp và rpm trong danh sách giá trị cột và hàng
    try:
        tp_index = first_column.index(tp) + 1
    except ValueError:
        print(f"Không tìm thấy giá trị TP (%) = {tp}")
        return
    try:
        rpm_index = first_row.index(rpm) + 1
    except ValueError:
        print(f"Không tìm thấy giá trị RPM = {rpm}")
        return

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

# Gọi hàm để cập nhật giá trị x vào file CSV
readdata(100, 1500, 7.11, 12.5, '../APP/DATA/map1.csv')
