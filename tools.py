import tkinter as tk
from tkinter import filedialog, colorchooser, simpledialog, messagebox
from PIL import Image, ImageDraw, ImageTk
import random

class Paint:
    def __init__(self, root):
        self.root = root
        self.canvas = None
        self.color = "black"
        self.image = None
        self.draw = None
        self.last_x, self.last_y = None, None
        self.tool = "brush"  # Default tool
        self.brush_size = 2  # Default brush size
        self.start_x, self.start_y = None, None  # For rectangles and circles

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        # Initialize the image and drawing context
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

    def set_tool(self, tool):
        self.tool = tool

    def set_color(self, color):
        self.color = color

    def set_brush_size(self, size):
        self.brush_size = size

    def on_button_press(self, event):
        self.last_x, self.last_y = event.x, event.y
        if self.tool in ["rectangle", "circle"]:
            self.start_x, self.start_y = event.x, event.y
        elif self.tool == "text":
            self.add_text(event.x, event.y)

    def on_mouse_drag(self, event):
        if self.tool == "brush":
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=self.brush_size)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.color, width=self.brush_size)
            self.last_x, self.last_y = event.x, event.y
        elif self.tool == "pencil":
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=1)  # Pencil with width 1
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.color, width=1)
            self.last_x, self.last_y = event.x, event.y
        elif self.tool == "eraser":
            self.canvas.create_rectangle(event.x, event.y, event.x + self.brush_size, event.y + self.brush_size, fill="white", outline="white")
            self.draw.rectangle([event.x, event.y, event.x + self.brush_size, event.y + self.brush_size], fill="white", outline="white")
        elif self.tool == "spray":
            for _ in range(20):  # Number of spray dots
                sx = random.randint(event.x - 5, event.x + 5)
                sy = random.randint(event.y - 5, event.y + 5)
                self.canvas.create_oval(sx, sy, sx + 2, sy + 2, fill=self.color, outline=self.color)
                self.draw.ellipse([sx, sy, sx + 2, sy + 2], fill=self.color, outline=self.color)
        elif self.tool in ["rectangle", "circle"]:
            self.canvas.delete("temp")
            if self.tool == "rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color, tags="temp")
            elif self.tool == "circle":
                self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color, tags="temp")

    def on_button_release(self, event):
        if self.tool in ["rectangle", "circle"]:
            if self.tool == "rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color)
                self.draw.rectangle([self.start_x, self.start_y, event.x, event.y], outline=self.color)
            elif self.tool == "circle":
                self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color)
                self.draw.ellipse([self.start_x, self.start_y, event.x, event.y], outline=self.color)

    def add_text(self, x, y):
        text = simpledialog.askstring("Input", "Enter text:")
        if text:
            self.canvas.create_text(x, y, text=text, fill=self.color, font=("Arial", self.brush_size))
            self.draw.text((x, y), text, fill=self.color)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.draw = ImageDraw.Draw(self.image)
            self.update_canvas()

    def save_image(self):
        if not self.image:
            messagebox.showerror("Error", "No content to save!")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            try:
                self.image.save(file_path)
                messagebox.showinfo("Saved", f"Image saved successfully at {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {e}")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.set_color(color)

    def update_canvas(self):
        if self.image:
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = Paint(root)
    paint_app.create_canvas()
    root.mainloop()
