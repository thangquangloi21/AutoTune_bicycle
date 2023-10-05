import csv
import shutil
import pandas as pd

data_dyno = 'Data_IN/Data.csv'
ecu_data = 'Data_IN/ecu.tqECU'
data1 = 'Data_IN/Book1.csv'
map = 'DATA/map1.csv'

Datacantinhtoan = []
# xu ly file map
def xulydata(inp_data):
    # Mở file CSV để đọc với delimiter là ';'
    with open(inp_data, mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=';')
        data = list(csv_reader)
    # Xóa 7 hàng đầu tiên
    del data[:7]
    # Mở file CSV để ghi dữ liệu sau khi đã xóa
    with open('DATA/datas.csv', mode='w', newline='') as file:
        # Tạo đối tượng ghi CSV
        csv_writer = csv.writer(file)
        # Ghi dữ liệu vào file CSV
        csv_writer.writerows(data)
    data = pd.read_csv('DATA/datas.csv')
    selected_data = data[['TP (%)', 'RPM', 'Lambda (AFR)']]
    # Lưu DataFrame vào file CSV mới
    selected_data.to_csv('DATA/datas.csv', index=False)

# xu ly file ecu
def xulydata2(duong_dan_tep_tin_cu):
    # Đường dẫn mới với đuôi .txt
    duong_dan_tep_tin_moi = 'DATA/ecus.csv'
    # Sao chép nội dung của tệp tin gốc vào tệp tin mới
    shutil.copy(duong_dan_tep_tin_cu, duong_dan_tep_tin_moi)
    # Mở file CSV để đọc với delimiter là '&'
    with open('../APP/DATA/ecus.csv', mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='&')
        data = list(csv_reader)
    # Xóa
    dau = 13
    cuoi = 72
    du_lieu_can_lay = data[dau - 1:cuoi]
    # Luu vao
    with open('../APP/DATA/ecus.csv', mode='w', newline='') as file:
        # Tạo đối tượng ghi CSV
        csv_writer = csv.writer(file)
        # Ghi dữ liệu vào file CSV
        csv_writer.writerows(du_lieu_can_lay)
    with open('../APP/DATA/ecus.csv', mode='r', newline='') as file:
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
                      columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500', '6000', '6500',
                '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000', '11500', '12000', '12500',
                '13000', '13500', '14000', '14500', '15000'])
    df.index = ['90', '80', '70', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
    df.to_csv('DATA/map1.csv', index=True)
    # map 2
    dau = 17
    cuoi = 30
    map2 = data[dau - 1:cuoi]
    # Xóa cột đầu tiên trong map1
    for i in range(len(map2)):
        map2[i] = map2[i][1:]
    df = pd.DataFrame(map2,
                      columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500',
                               '6000', '6500',
                               '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000', '11500',
                               '12000', '12500',
                               '13000', '13500', '14000', '14500', '15000'])
    df.index = ['90', '80', '70', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
    df.to_csv('DATA/map2.csv', index=True)

    # map 3
    dau = 32
    cuoi = 45
    map3 = data[dau - 1:cuoi]
    # Xóa cột đầu tiên trong map1
    for i in range(len(map3)):
        map3[i] = map3[i][1:]
    df = pd.DataFrame(map3,
                      columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500',
                               '6000', '6500',
                               '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000', '11500',
                               '12000', '12500',
                               '13000', '13500', '14000', '14500', '15000'])
    df.index = ['90', '80', '70', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
    df.to_csv('DATA/map3.csv', index=True)

    # map 4
    dau = 47
    cuoi = 60
    map4 = data[dau - 1:cuoi]
    # Xóa cột đầu tiên trong map1
    for i in range(len(map4)):
        map4[i] = map4[i][1:]

    df = pd.DataFrame(map4,
                      columns=['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500',
                               '6000', '6500',
                               '7000', '7500', '8000', '8500', '90000', '9500', '10000', '10500', '11000', '11500',
                               '12000', '12500',
                               '13000', '13500', '14000', '14500', '15000'])
    df.index = ['90', '80', '70', '70', '60', '50', '40', '30', '20', '14', '8', '5', '2', '0']
    df.to_csv('DATA/map4.csv', index=True)

# gop data da xu ly
def gopdata(data1, map):
    # Lặp qua từng hàng trong bảng dữ liệu
    # bang = pd.read_excel(data1)
    bang = pd.read_csv(data1)
    df = pd.read_csv(map)
    for index, row in bang.iterrows():
        # Trích xuất các giá trị từ các cột cụ thể
        tp = row['TP (%)']
        rpm = row['RPM']
        lambda_afr = row['Lambda (AFR)']
        # lam tron
        rpm = int(round(rpm / 500) * 500)
        tp = int(tp)
        print(tp,rpm)
        try:
            # Kiểm tra xem TPS_ECU có tồn tại trong cột "Unnamed: 0" của df không
            if tp in df['Unnamed: 0'].values:
                thoigianphun = df[df['Unnamed: 0'] == tp][str(rpm)].values[0]
                print(f"Thời gian phun ở {tp}% TPS và  {rpm}RPM là: {thoigianphun} ms")
                Datacantinhtoan.append([tp, rpm, thoigianphun, lambda_afr])
            else:
                print(f"Không tìm thấy giá trị x ở hàng {tp}")
            pass
        except IndexError:
            print(f"Không tìm thấy giá trị x ở hàng {tp} và cột {rpm}")
        # In ra các giá trị đã trích xuất
    print(Datacantinhtoan)
    result_df = pd.DataFrame(Datacantinhtoan, columns=['TP (%)', 'RPM', 'INJ VE (ms)', 'AFR'])
    print(result_df)
    result_df.to_csv('DATA/ket_qua.csv', index=False)

# xulydata2(ecu_data)
xulydata(data_dyno)
gopdata(data1,map)


