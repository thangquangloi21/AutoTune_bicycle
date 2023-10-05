import pandas as pd

# Đọc tệp CSV
csv_file_path = 'map1.csv'

def output(map_out):
    df = pd.read_csv(map_out, header=None)
    output_txt_file_path = '../APP/DATA/output.txt'
    # Xóa hàng đầu tiên và cột đầu tiên
    df = df.iloc[1:, 1:]
    # Lưu DataFrame vào tệp văn bản với delimiter mặc định (,) tạm thời
    txt_file_path = 'maps.csv'
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
        formatted_line = ' &'.join(formatted_parts) # Ghép các số lại thành một dòng
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


output(csv_file_path)