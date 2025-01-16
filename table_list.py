import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('db.sqlite3')

# Tạo đối tượng cursor
cursor = conn.cursor()

# Truy vấn để lấy danh sách tên bảng
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Lấy tất cả tên bảng
tables = cursor.fetchall()

# Xuất danh sách tên bảng ra tệp txt
with open('tables_list.txt', 'w') as f:
    for table in tables:
        f.write(table[0] + '\n')

# Đóng kết nối
conn.close()

print("Danh sách tên bảng đã được xuất ra tệp 'tables_list.txt'.")
