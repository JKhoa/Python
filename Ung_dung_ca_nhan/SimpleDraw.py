import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab

class SimplePaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Vẽ")

        # Canvas
        self.canvas = tk.Canvas(root, bg="white", width=800, height=500)
        self.canvas.pack(pady=5)

        # Thuộc tính vẽ
        self.color = "black"
        self.eraser_mode = False
        self.pen_size = 5
        self.history = []
        self.current_stroke = []
        self.tool = "pencil"  # Công cụ mặc định là bút chì

        # Thanh công cụ
        frame = tk.Frame(root)
        frame.pack(pady=5)

        # Công cụ vẽ
        tk.Button(frame, text="Bút chì", command=lambda: self.select_tool("pencil")).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Đường thẳng", command=lambda: self.select_tool("line")).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Hình chữ nhật", command=lambda: self.select_tool("rectangle")).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Oval", command=lambda: self.select_tool("oval")).pack(side=tk.LEFT, padx=2)


        # Nút chức năng
        tk.Button(frame, text="Chọn màu", command=self.choose_color).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Đổ màu nền", command=self.choose_bg_color).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Tẩy", command=self.toggle_eraser).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Xóa", command=self.clear_canvas).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Undo", command=self.undo).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Lưu", command=self.save_as_png).pack(side=tk.LEFT, padx=2)

        # Thanh kéo kích thước
        self.pen_size_slider = tk.Scale(root, from_=1, to=20, orient='horizontal', label='Cỡ Bút/Tẩy')
        self.pen_size_slider.set(self.pen_size)
        self.pen_size_slider.pack(pady=5)

        # Sự kiện vẽ
        self.start_x = None
        self.start_y = None
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def select_tool(self, tool):
        """Chọn công cụ vẽ"""
        self.tool = tool
        self.eraser_mode = False

    def start_draw(self, event):
        """Bắt đầu vẽ"""
        self.start_x, self.start_y = event.x, event.y
        self.current_stroke = []

    def paint(self, event):
        """Vẽ trên canvas khi giữ chuột"""
        pen_size = self.pen_size_slider.get()
        fill_color = "white" if self.eraser_mode else self.color

        if self.tool == "pencil":
            x1, y1 = event.x - pen_size, event.y - pen_size
            x2, y2 = event.x + pen_size, event.y + pen_size
            item = self.canvas.create_oval(x1, y1, x2, y2, fill=fill_color, outline=fill_color)
            self.current_stroke.append(item)

    def end_draw(self, event):
        """Kết thúc vẽ"""
        if self.tool == "line":
            item = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=self.pen_size_slider.get())
            self.current_stroke.append(item)
        elif self.tool == "rectangle":
            item = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color, width=self.pen_size_slider.get())
            self.current_stroke.append(item)
        elif self.tool == "oval":
            item = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color, width=self.pen_size_slider.get())
            self.current_stroke.append(item)

        if self.current_stroke:
            self.history.append(self.current_stroke)
            

    def choose_color(self):
        """Chọn màu vẽ"""
        self.color = colorchooser.askcolor()[1]
        self.eraser_mode = False

    def choose_bg_color(self):
        """Chọn màu nền"""
        bg_color = colorchooser.askcolor()[1]
        if bg_color:
            self.canvas.config(bg=bg_color)

    def fill_color(self):
        """Tô màu toàn bộ canvas"""
        self.canvas.config(bg=self.color)

    def toggle_eraser(self):
        """Bật/tắt chế độ tẩy"""
        self.eraser_mode = not self.eraser_mode

    def clear_canvas(self):
        """Xóa toàn bộ canvas"""
        self.canvas.delete("all")
        self.history.clear()

    def undo(self):
        """Hoàn tác (Undo) nét vẽ cuối cùng"""
        if self.history:
            last_stroke = self.history.pop()
            for item in last_stroke:
                self.canvas.delete(item)

    def save_as_png(self):
        """Lưu canvas thành file PNG"""
        try:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            img = ImageGrab.grab(bbox=(x, y, x1, y1))
            img.save("drawing.png")
            print("Lưu ảnh thành công: drawing.png")
        except Exception as e:
            print(f"Lỗi khi lưu ảnh: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePaint(root)
    root.mainloop()
