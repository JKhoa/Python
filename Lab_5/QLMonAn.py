import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

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

# Lấy danh sách tất cả món ăn
def get_all_foods():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT MaMonAn, TenMonAn, DonViTinh, DonGia, TenNhom
                FROM MonAn
                JOIN NhomMonAn ON MonAn.Nhom = NhomMonAn.MaNhom
            ''')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Lỗi khi truy vấn món ăn: {e}')
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
def update_table(data):
    for row in tree.get_children():
        tree.delete(row)
    if data:
        for item in data:
            tree.insert('', 'end', values=item)

# Form thêm/sửa món ăn
def open_food_form(action, food=None):
    form = tk.Toplevel(root)
    form.title(f'{action} món ăn')
    form.geometry('300x200')

    tk.Label(form, text='Tên món ăn:').pack(pady=5)
    entry_name = tk.Entry(form)
    entry_name.pack(pady=5)

    tk.Label(form, text='Đơn vị tính:').pack(pady=5)
    entry_unit = tk.Entry(form)
    entry_unit.pack(pady=5)

    tk.Label(form, text='Đơn giá:').pack(pady=5)
    entry_price = tk.Entry(form)
    entry_price.pack(pady=5)

    if action == 'Sửa' and food:
        entry_name.insert(0, food[1])
        entry_unit.insert(0, food[2])
        entry_price.insert(0, food[3])

    def save_food():
        name = entry_name.get()
        unit = entry_unit.get()
        price = entry_price.get()
        if not name or not unit or not price:
            messagebox.showwarning('Cảnh báo', 'Vui lòng điền đầy đủ thông tin')
            return
        if action == 'Thêm':
            messagebox.showinfo('Thêm', f'Thêm món: {name}')
        elif action == 'Sửa':
            messagebox.showinfo('Sửa', f'Cập nhật món: {name}')
        form.destroy()
        update_table(get_all_foods())

    btn_save = tk.Button(form, text='Lưu', command=save_food)
    btn_save.pack(pady=10)

# Thêm món ăn
def add_food():
    open_food_form('Thêm')

# Sửa món ăn
def edit_food():
    selected_item = tree.selection()
    if selected_item:
        food = tree.item(selected_item)['values']
        open_food_form('Sửa', food)
    else:
        messagebox.showwarning('Cảnh báo', 'Vui lòng chọn một món ăn để sửa')

# Xóa món ăn
def delete_food():
    selected_item = tree.selection()
    if selected_item:
        food = tree.item(selected_item)['values']
        confirm = messagebox.askyesno('Xóa', f'Bạn có chắc chắn muốn xóa món: {food[1]}?')
        if confirm:
            messagebox.showinfo('Xóa', f'Đã xóa món: {food[1]}')
            update_table(get_all_foods())
    else:
        messagebox.showwarning('Cảnh báo', 'Vui lòng chọn một món ăn để xóa')

# Hiển thị tất cả món ăn
def show_all_foods():
    foods = get_all_foods()
    update_table(foods)

# Giao diện
root = tk.Tk()
root.title('Quản lý món ăn')
root.geometry('700x400')

# Frame chứa nút và combobox
top_frame = tk.Frame(root)
top_frame.pack(pady=5, fill='x')

# Nút hiển thị tất cả món ăn
btn_show_all = tk.Button(top_frame, text='Hiển thị danh sách món ăn', command=show_all_foods)
btn_show_all.pack(side='left', padx=5)

# Combobox nhóm món ăn
groups = get_food_groups()
group_names = [group[1] for group in groups]
cbo_group = ttk.Combobox(top_frame, values=group_names, state='readonly')
cbo_group.pack(side='left', padx=5)
cbo_group.bind('<<ComboboxSelected>>', lambda e: update_table(get_foods_by_group(cbo_group.get())))

# Table danh sách món ăn
columns = ('MaMonAn', 'TenMonAn', 'DonViTinh', 'DonGia', 'TenNhom')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(pady=10, expand=True, fill='both')

# Menu chuột phải
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label='Thêm', command=add_food)
context_menu.add_command(label='Sửa', command=edit_food)
context_menu.add_command(label='Xóa', command=delete_food)

# Hiện menu chuột phải
def show_context_menu(event):
    try:
        context_menu.post(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()

tree.bind('<Button-3>', show_context_menu)

root.mainloop()
