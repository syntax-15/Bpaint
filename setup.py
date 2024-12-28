import tkinter as tk
from tkinter import messagebox

def save_preferences(language, theme):
    with open('usr/interface.txt', 'w') as file:
        file.write(f"{language}\n{theme}")

def on_submit():
    language = language_var.get()
    theme = theme_var.get()
    save_preferences(language, theme)
    messagebox.showinfo("Preferences Saved", f"Language: {language}\nTheme: {theme}")
    root.destroy()

# Vytvoření hlavního okna
root = tk.Tk()
root.title("B-paint Setup")

# ASCII art
ascii_art = """
                           ######+                                                      
                        #####  +++                                                      
                      *###     **                                                       
                   +*##      ***                                                        
                 ++##      ***                                                          
                +*++     ***                                                            
              +++**    ***                                                              
             +*+###  ***+***++**#                                                       
            #%  **  **++       ##                                                       
           %#  **             #*+                                    +**                
          ##  +*             +++                                     **+                
        ###  #**           ++++                                     ****                
       ###  ***          ++++                                      ****                 
       ##   **         ++++                                        **#                  
      #*   ##        +**#                       *+                 ###                  
     *+   ###      **##       +++                                 +++                   
    *+   ##       ###       ++++                                 ++++                   
   +++  #*+    ####      #*+++ ***    **+++    #**    ###       +++++                   
   +*  *++   ####     *#*++**+***#*  ++++***  ***#   ###***+   +++ +++          +++     
  ##  +++  %##    +**+*    ++**  **+++*#%#++***# **##*  **+#+++++  ****#    ++++++      
  ** +++*###      +        ***         %   **#     #        +++    *##***++++++         
  #*++++#                 **                                        #**++++             
                         ***                                                            
                        *+*                                                             
                        #*                                                              
                        **                                                              
                        %%                                                              
"""

# Vytvoření widgetů
label = tk.Label(root, text=ascii_art, font=("Courier", 10), justify="left")
label.pack()

language_var = tk.StringVar(value="en")
theme_var = tk.StringVar(value="light")

# Jazyk
language_label = tk.Label(root, text="Select Language:")
language_label.pack()

language_frame = tk.Frame(root)
language_frame.pack()

language_en = tk.Radiobutton(language_frame, text="English", variable=language_var, value="en")
language_en.pack(side=tk.LEFT)

language_cz = tk.Radiobutton(language_frame, text="Czech", variable=language_var, value="cz")
language_cz.pack(side=tk.LEFT)

# Téma
theme_label = tk.Label(root, text="Select Theme:")
theme_label.pack()

theme_frame = tk.Frame(root)
theme_frame.pack()

theme_light = tk.Radiobutton(theme_frame, text="Light", variable=theme_var, value="light")
theme_light.pack(side=tk.LEFT)

theme_dark = tk.Radiobutton(theme_frame, text="Dark", variable=theme_var, value="dark")
theme_dark.pack(side=tk.LEFT)

# Tlačítko pro odeslání
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Spuštění hlavní smyčky
root.mainloop()
