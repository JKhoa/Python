import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Hàm kết nối đến CSDL
def get_connection():
    try:
        conn = sqlite3.connect('QLMonAn.db')
        return conn
    except sqlite3.Error as e:
        print(f'Lỗi khi kết nối CSDL: {e}')
        return None

# Hàm đóng kết nối CSDL
def close_connection(conn):
    if conn:
        conn.close()

# Hàm lấy danh sách món ăn theo nhóm
def get_foods_by_group(group_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom FROM MonAn WHERE Nhom = ?
            ''', (group_id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Lỗi khi truy vấn CSDL: {e}')
        finally:
            close_connection(conn)
    return []

# Hàm thêm món ăn
def insert_food(food_id, name, unit, price, group_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO MonAn(MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (?, ?, ?, ?, ?)', (food_id, name, unit, price, group_id))
            conn.commit()
            messagebox.showinfo('Thông báo', 'Thêm món ăn thành công!')
        except sqlite3.Error as e:
            messagebox.showerror('Lỗi', f'Lỗi khi thêm món ăn: {e}')
        finally:
            close_connection(conn)

# Hàm cập nhật món ăn
def update_food(food_id, name, unit, price, group_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE MonAn SET TenMonAn = ?, DonViTinh = ?, DonGia = ?, Nhom = ? WHERE MaMonAn = ?', (name, unit, price, group_id, food_id))
            conn.commit()
            messagebox.showinfo('Thông báo', 'Cập nhật món ăn thành công!')
        except sqlite3.Error as e:
            messagebox.showerror('Lỗi', f'Lỗi khi cập nhật món ăn: {e}')
        finally:
            close_connection(conn)

# Hàm xóa món ăn
def delete_food(food_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM MonAn WHERE MaMonAn = ?', (food_id,))
            conn.commit()
            messagebox.showinfo('Thông báo', 'Xóa món ăn thành công!')
        except sqlite3.Error as e:
            messagebox.showerror('Lỗi', f'Lỗi khi xóa món ăn: {e}')
        finally:
            close_connection(conn)

# Giao diện tkinter
root = tk.Tk()
root.title('Quản lý món ăn')
root.geometry('600x400')

# Combobox chọn nhóm món ăn
selected_group = tk.StringVar()
group_combobox = ttk.Combobox(root, textvariable=selected_group, values=['Khai vị', 'Hải sản', 'Bia - Nước ngọt', 'Lẩu'])
group_combobox.pack(pady=10)

# Bảng hiển thị danh sách món ăn
tree = ttk.Treeview(root, columns=('MaMonAn', 'TenMonAn', 'DonViTinh', 'DonGia', 'Nhom'), show='headings')
for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(pady=10)

# Menu chuột phải
menu = tk.Menu(root, tearoff=0)
menu.add_command(label='Thêm', command=lambda: insert_food(int(entries['Mã món ăn'].get()), entries['Tên món ăn'].get(), entries['Đơn vị tính'].get(), int(entries['Đơn giá'].get()), int(entries['Nhóm'].get())))
menu.add_command(label='Sửa', command=lambda: update_food(int(entries['Mã món ăn'].get()), entries['Tên món ăn'].get(), entries['Đơn vị tính'].get(), int(entries['Đơn giá'].get()), int(entries['Nhóm'].get())))
menu.add_command(label='Xóa', command=lambda: delete_food(int(entries['Mã món ăn'].get())))

# Hiển thị menu khi nhấn chuột phải

def show_context_menu(event):
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item, 'values')
        if item_values:
            entries['Mã món ăn'].delete(0, tk.END)
            entries['Mã món ăn'].insert(0, item_values[0])
            entries['Tên món ăn'].delete(0, tk.END)
            entries['Tên món ăn'].insert(0, item_values[1])
            entries['Đơn vị tính'].delete(0, tk.END)
            entries['Đơn vị tính'].insert(0, item_values[2])
            entries['Đơn giá'].delete(0, tk.END)
            entries['Đơn giá'].insert(0, item_values[3])
            entries['Nhóm'].delete(0, tk.END)
            entries['Nhóm'].insert(0, item_values[4])
    menu.post(event.x_root, event.y_root)

tree.bind('<Button-3>', show_context_menu)

# Hàm load dữ liệu theo nhóm
def load_data():
    group_map = {'Khai vị': 1, 'Hải sản': 2, 'Bia - Nước ngọt': 3, 'Lẩu': 4}
    group_id = group_map.get(selected_group.get())
    if group_id:
        foods = get_foods_by_group(group_id)
        tree.delete(*tree.get_children())
        for food in foods:
            tree.insert('', 'end', values=food)

group_combobox.bind('<<ComboboxSelected>>', lambda e: load_data())

# Form thêm/sửa món ăn
frame = tk.Frame(root)
frame.pack(pady=10)

labels = ['Mã món ăn', 'Tên món ăn', 'Đơn vị tính', 'Đơn giá', 'Nhóm']
entries = {}
for label in labels:
    row = tk.Frame(frame)
    row.pack(pady=2)
    tk.Label(row, text=label).pack(side='left')
    entry = tk.Entry(row)
    entry.pack(side='right')
    entries[label] = entry

root.mainloop()
