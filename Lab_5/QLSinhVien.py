import pyodbc

# Hàm kết nối đến SQL Server
def get_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=.;'
            'DATABASE=QLSinhVien;'
            'UID=sa;'
            'PWD=sa;'
            'Encrypt=no'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Lỗi kết nối CSDL: {e}")
        return None

# Hàm đóng kết nối CSDL
def close_connection(conn):
    if conn:
        conn.close()

# Hàm lấy danh sách sinh viên
def get_all_students():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            SELECT SinhVien.ID, SinhVien.HoTen, SinhVien.MaLop, Lop.TenLop
            FROM SinhVien
            JOIN Lop ON SinhVien.MaLop = Lop.ID
            """
            cursor.execute(query)
            students = cursor.fetchall()

            print(f"{'Mã số':<5}{'Họ tên':<25}{'Mã lớp':<10}{'Tên lớp':<10}")
            print("-" * 50)
            for sv in students:
                print(f"{sv.ID:<5}{sv.HoTen:<25}{sv.MaLop:<10}{sv.TenLop:<10}")
        except pyodbc.Error as e:
            print(f"Lỗi khi truy vấn CSDL: {e}")
        finally:
            close_connection(conn)

# Hàm thêm sinh viên
def insert_student(id, name, class_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO SinhVien (ID, HoTen, MaLop) VALUES (?, ?, ?)', (id, name, class_id))
            conn.commit()
            print('Thêm sinh viên thành công!')
        except pyodbc.Error as e:
            print(f'Lỗi khi thêm sinh viên: {e}')
        finally:
            close_connection(conn)

# Hàm cập nhật thông tin sinh viên
def update_student(id, name, class_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE SinhVien SET HoTen = ?, MaLop = ? WHERE ID = ?', (name, class_id, id))
            conn.commit()
            print('Cập nhật sinh viên thành công!')
        except pyodbc.Error as e:
            print(f'Lỗi khi cập nhật sinh viên: {e}')
        finally:
            close_connection(conn)

# Hàm xóa sinh viên
def delete_student(id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM SinhVien WHERE ID = ?', (id,))
            conn.commit()
            print('Xóa sinh viên thành công!')
        except pyodbc.Error as e:
            print(f'Lỗi khi xóa sinh viên: {e}')
        finally:
            close_connection(conn)

# Menu chức năng
def menu():
    while True:
        print("\n=== Quản lý sinh viên ===")
        print("1. Xem danh sách sinh viên")
        print("2. Thêm sinh viên")
        print("3. Sửa thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            get_all_students()
        elif choice == '2':
            try:
                id = int(input("Nhập ID sinh viên: "))
                name = input("Nhập họ tên sinh viên: ")
                class_id = int(input("Nhập mã lớp: "))
                insert_student(id, name, class_id)
            except ValueError:
                print("Dữ liệu nhập không hợp lệ!")
        elif choice == '3':
            try:
                id = int(input("Nhập ID sinh viên cần sửa: "))
                name = input("Nhập họ tên mới: ")
                class_id = int(input("Nhập mã lớp mới: "))
                update_student(id, name, class_id)
            except ValueError:
                print("Dữ liệu nhập không hợp lệ!")
        elif choice == '4':
            try:
                id = int(input("Nhập ID sinh viên cần xóa: "))
                delete_student(id)
            except ValueError:
                print("Dữ liệu nhập không hợp lệ!")
        elif choice == '5':
            print("Thoát chương trình!")
            break
        else:
            print("Chọn sai chức năng, vui lòng chọn lại!")

if __name__ == '__main__':
    menu()
