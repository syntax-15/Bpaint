import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from tools import Paint
import os

class BPaint:
    def __init__(self, root):
        self.root = root
        self.root.title("B-paint")
        
        self.paint = Paint(self.root)
        
        # Načtení jazyka a tématu
        self.language, self.theme = self.load_preferences()
        self.translations = self.load_language_file(self.language)
        
        # Menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        # Jazyk
        language_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Language"], menu=language_menu)
        language_menu.add_command(label="English", command=lambda: self.set_language("en"))
        language_menu.add_command(label="Czech", command=lambda: self.set_language("cz"))

        # Téma
        theme_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Select Theme"], menu=theme_menu)
        theme_menu.add_command(label=self.translations["Light"], command=self.set_light_theme)
        theme_menu.add_command(label=self.translations["Dark"], command=self.set_dark_theme)

        # Další menu
        file_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["File"], menu=file_menu)
        file_menu.add_command(label=self.translations["Open"], command=self.paint.open_image)
        file_menu.add_command(label=self.translations["Save"], command=self.paint.save_image)
        file_menu.add_separator()
        file_menu.add_command(label=self.translations["Exit"], command=self.root.quit)
        
        color_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Color"], menu=color_menu)
        color_menu.add_command(label=self.translations["Choose Color"], command=self.paint.choose_color)

        tool_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Tools"], menu=tool_menu)
        tool_menu.add_command(label=self.translations["Brush"], command=lambda: self.paint.set_tool("brush"))
        tool_menu.add_command(label=self.translations["Pencil"], command=lambda: self.paint.set_tool("pencil"))
        tool_menu.add_command(label=self.translations["Spray"], command=lambda: self.paint.set_tool("spray"))
        tool_menu.add_command(label=self.translations["Eraser"], command=lambda: self.paint.set_tool("eraser"))
        tool_menu.add_command(label=self.translations["Rectangle"], command=lambda: self.paint.set_tool("rectangle"))
        tool_menu.add_command(label=self.translations["Circle"], command=lambda: self.paint.set_tool("circle"))
        tool_menu.add_command(label=self.translations["Text"], command=lambda: self.paint.set_tool("text"))

        # Velikost štětce
        size_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Brush Size"], menu=size_menu)
        size_menu.add_command(label="Small", command=lambda: self.paint.set_brush_size(2))
        size_menu.add_command(label="Medium", command=lambda: self.paint.set_brush_size(5))
        size_menu.add_command(label="Large", command=lambda: self.paint.set_brush_size(10))

        # Paleta barev
        color_palette = tk.Frame(self.root)
        color_palette.pack(side=tk.LEFT, fill=tk.Y)

        colors = ["black", "red", "green", "blue", "yellow", "cyan", "magenta", "gray", "white"]
        for color in colors:
            btn = tk.Button(color_palette, bg=color, command=lambda c=color: self.paint.set_color(c), width=4, height=2)
            btn.pack(pady=2)

        self.paint.create_canvas()
        self.apply_theme(self.theme)

    def load_preferences(self):
        try:
            with open('usr/interface.txt', 'r') as file:
                language = file.readline().strip()
                theme = file.readline().strip()
                return language, theme
        except FileNotFoundError:
            return "en", "light"  # Default values

    def load_language_file(self, lang):
        try:
            with open(f'usr/language/{lang}.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                translations = {}
                for line in lines:
                    key, value = line.strip().split(': ')
                    translations[key] = value
                return translations
        except FileNotFoundError:
            return {}  # Return empty dictionary if file not found

    def apply_theme(self, theme):
        if theme == "dark":
            self.root.config(bg="black")
            self.paint.canvas.config(bg="gray")
        else:
            self.root.config(bg="white")
            self.paint.canvas.config(bg="lightgray")

    def set_language(self, lang):
        self.language = lang
        self.translations = self.load_language_file(self.language)
        self.update_menu_labels()

    def update_menu_labels(self):
        self.root.config(menu=None)  # Clear existing menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # Jazyk
        language_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Language"], menu=language_menu)
        language_menu.add_command(label="English", command=lambda: self.set_language("en"))
        language_menu.add_command(label="Czech", command=lambda: self.set_language("cz"))

        # Téma
        theme_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Select Theme"], menu=theme_menu)
        theme_menu.add_command(label=self.translations["Light"], command=self.set_light_theme)
        theme_menu.add_command(label=self.translations["Dark"], command=self.set_dark_theme)

        # Další menu
        file_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["File"], menu=file_menu)
        file_menu.add_command(label=self.translations["Open"], command=self.paint.open_image)
        file_menu.add_command(label=self.translations["Save"], command=self.paint.save_image)
        file_menu.add_separator()
        file_menu.add_command(label=self.translations["Exit"], command=self.root.quit)

        color_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Color"], menu=color_menu)
        color_menu.add_command(label=self.translations["Choose Color"], command=self.paint.choose_color)

        tool_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Tools"], menu=tool_menu)
        tool_menu.add_command(label=self.translations["Brush"], command=lambda: self.paint.set_tool("brush"))
        tool_menu.add_command(label=self.translations["Pencil"], command=lambda: self.paint.set_tool("pencil"))
        tool_menu.add_command(label=self.translations["Spray"], command=lambda: self.paint.set_tool("spray"))
        tool_menu.add_command(label=self.translations["Eraser"], command=lambda: self.paint.set_tool("eraser"))
        tool_menu.add_command(label=self.translations["Rectangle"], command=lambda: self.paint.set_tool("rectangle"))
        tool_menu.add_command(label=self.translations["Circle"], command=lambda: self.paint.set_tool("circle"))
        tool_menu.add_command(label=self.translations["Text"], command=lambda: self.paint.set_tool("text"))

        # Velikost štětce
        size_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Brush Size"], menu=size_menu)
        size_menu.add_command(label="Small", command=lambda: self.paint.set_brush_size(2))
        size_menu.add_command(label="Medium", command=lambda: self.paint.set_brush_size(5))
        size_menu.add_command(label="Large", command=lambda: self.paint.set_brush_size(10))

    def set_light_theme(self):
        self.theme = "light"
        self.apply_theme(self.theme)

    def set_dark_theme(self):
        self.theme = "dark"
        self.apply_theme(self.theme)

if __name__ == "__main__":
    root = tk.Tk()
    app = BPaint(root)
    root.mainloop()
