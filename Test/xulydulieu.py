import shutil
import csv
# Đường dẫn tới tệp tin cần đổi tên
duong_dan_tep_tin_cu = 'Data_IN/ecu.tqECU'
# Đường dẫn mới với đuôi .txt
duong_dan_tep_tin_moi = 'ecu.csv'
# Sao chép nội dung của tệp tin gốc vào tệp tin mới
shutil.copy(duong_dan_tep_tin_cu, duong_dan_tep_tin_moi)
# Mở file CSV để đọc với delimiter là '&'
with open('ecu.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file, delimiter='&')
    data = list(csv_reader)
# Xóa
dau = 13
cuoi = 72
du_lieu_can_lay = data[dau - 1:cuoi]
# del data[:12]
#Luu vao
with open('../APP/DATA/ecus.csv', mode='w', newline='') as file:
    # Tạo đối tượng ghi CSV
    csv_writer = csv.writer(file)
    # Ghi dữ liệu vào file CSV
    csv_writer.writerows(du_lieu_can_lay)
