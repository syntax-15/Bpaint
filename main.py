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
        self.create_menu()

        # Paleta barev
        self.create_color_palette()

        self.paint.create_canvas()
        self.apply_theme(self.theme)

    def load_preferences(self):
        default_language = "en"
        default_theme = "light"
        try:
            with open('usr/interface.txt', 'r') as file:
                lines = file.readlines()
                language = lines[0].strip() if len(lines) > 0 else default_language
                theme = lines[1].strip() if len(lines) > 1 else default_theme
                return language, theme
        except FileNotFoundError:
            return default_language, default_theme

    def load_language_file(self, lang):
        default_translations = {
            "Language": "Language",
            "Select Theme": "Select Theme",
            "Light": "Light",
            "Dark": "Dark",
            "File": "File",
            "Open": "Open",
            "Save": "Save",
            "Exit": "Exit",
            "Color": "Color",
            "Choose Color": "Choose Color",
            "Tools": "Tools",
            "Brush": "Brush",
            "Pencil": "Pencil",
            "Spray": "Spray",
            "Eraser": "Eraser",
            "Rectangle": "Rectangle",
            "Circle": "Circle",
            "Text": "Text",
            "Brush Size": "Brush Size",
        }
        try:
            with open(f'usr/language/{lang}.txt', 'r', encoding='utf-8') as file:
                translations = {}
                for line in file:
                    key, value = line.strip().split(': ', 1)
                    translations[key] = value
                return {**default_translations, **translations}  # Merge with defaults
        except FileNotFoundError:
            return default_translations

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
        self.create_menu()

    def create_menu(self):
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

        size_menu = tk.Menu(menu)
        menu.add_cascade(label=self.translations["Brush Size"], menu=size_menu)
        size_menu.add_command(label="Small", command=lambda: self.paint.set_brush_size(2))
        size_menu.add_command(label="Medium", command=lambda: self.paint.set_brush_size(5))
        size_menu.add_command(label="Large", command=lambda: self.paint.set_brush_size(10))

    def create_color_palette(self):
        color_palette = tk.Frame(self.root)
        color_palette.pack(side=tk.LEFT, fill=tk.Y)

        colors = ["black", "red", "green", "blue", "yellow", "cyan", "magenta", "gray", "white"]
        for color in colors:
            btn = tk.Button(color_palette, bg=color, command=lambda c=color: self.paint.set_color(c), width=4, height=2)
            btn.pack(pady=2)

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
