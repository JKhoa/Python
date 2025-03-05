import tkinter as tk
from tkinter import ttk
import sqlite3

# Kết nối CSDL
def get_connection():
    try:
        conn = sqlite3.connect('QLMonAn.db')
        return conn
    except sqlite3.Error as e:
        print(f'Lỗi khi kết nối CSDL: {e}')
        return None

# Lấy danh sách nhóm món ăn
def get_food_groups():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM NhomMonAn')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Lỗi khi truy vấn nhóm món ăn: {e}')
        finally:
            conn.close()

# Lấy danh sách món ăn theo nhóm
def get_foods_by_group(group_name):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT MaMonAn, TenMonAn, DonViTinh, DonGia, TenNhom
                FROM MonAn
                JOIN NhomMonAn ON MonAn.Nhom = NhomMonAn.MaNhom
                WHERE TenNhom = ?
            ''', (group_name,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Lỗi khi truy vấn món ăn: {e}')
        finally:
            conn.close()

# Cập nhật dữ liệu bảng
def update_table(group_name):
    for row in tree.get_children():
        tree.delete(row)
    foods = get_foods_by_group(group_name)
    if foods:
        for food in foods:
            tree.insert('', 'end', values=food)

# Giao diện
root = tk.Tk()
root.title('Quản lý món ăn')
root.geometry('600x400')

# Label nhóm món ăn
lbl_group = tk.Label(root, text='Nhóm món ăn:', font=('Arial', 12))
lbl_group.pack(pady=5)

# Combobox nhóm món ăn
groups = get_food_groups()
group_names = [group[1] for group in groups]
cbo_group = ttk.Combobox(root, values=group_names, state='readonly')
cbo_group.pack(pady=5)
cbo_group.bind('<<ComboboxSelected>>', lambda e: update_table(cbo_group.get()))

# Table danh sách món ăn
columns = ('MaMonAn', 'TenMonAn', 'DonViTinh', 'DonGia', 'TenNhom')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(pady=10, expand=True, fill='both')

root.mainloop()
