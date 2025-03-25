from graphviz import Digraph

# Tạo đối tượng đồ thị
dot = Digraph('UseCaseDiagram', format='png')

# Định dạng chung
dot.attr(size='10', rankdir='LR', splines='true')

# Thêm actor Khách hàng và Lễ tân
dot.node('KH', 'Khách hàng', shape='actor')
dot.node('LT', 'Lễ tân', shape='actor')

# Thêm các use case
dot.node('UC1', 'Đặt phòng online', shape='ellipse')
dot.node('UC2', 'Hủy phòng', shape='ellipse')
dot.node('UC3', 'Nhận phòng', shape='ellipse')
dot.node('UC4', 'Trả phòng', shape='ellipse')
dot.node('UC5', 'Góp ý', shape='ellipse')

# Liên kết actor với use case
dot.edge('KH', 'UC1')
dot.edge('KH', 'UC2')
dot.edge('KH', 'UC5')

dot.edge('LT', 'UC3')
dot.edge('LT', 'UC4')
dot.edge('LT', 'UC5')

# Lưu và hiển thị hình ảnh
dot.render('UseCaseDiagram', format='png', cleanup=True)
