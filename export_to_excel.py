import sqlite3
import pandas as pd

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('db.sqlite3')

# Tạo đối tượng cursor
cursor = conn.cursor()

# Truy vấn để lấy danh sách tên bảng
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
#///////////Xuat tat ca cac bang
# Tạo một writer để ghi vào file Excel
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    for table in tables:
        table_name = table[0]
        # Đọc dữ liệu từ bảng
        df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
        # Xuất dữ liệu ra sheet với tên là tên bảng
        df.to_excel(writer, sheet_name=table_name, index=False)
#//////////////

#////////Xuat du lieu từng bảng///////

# Đọc dữ liệu từ bảng (thay 'your_table_name' bằng tên bảng của bạn)
# query = 'SELECT * FROM your_table_name'
# df = pd.read_sql_query(query, conn)

# # Xuất dữ liệu ra tệp Excel
# df.to_excel('output.xlsx', index=False)
#//////////

# Đóng kết nối
conn.close()

print("Dữ liệu đã được xuất ra tệp 'output.xlsx' với mỗi bảng là một sheet.")
