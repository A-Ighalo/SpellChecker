import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker
from tkinter import filedialog
import customtkinter
from customtkinter import CTkOptionMenu


class SpellCheckerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()  

        #change the theme of the app
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.title("Spell Checker")
        self.create_widgets()
        self.create_menu()
       
         
         
    def create_widgets(self):
        self.text_input = customtkinter.CTkTextbox(self, width= 900,height=600, wrap=tk.WORD)
        self.text_input.pack(pady=10, padx = 15)

        self.check_button = customtkinter.CTkButton(self, text="Check Spelling", command =self.check_spelling)
        self.check_button.pack(pady=10,padx= 15)
        
        self.clear = customtkinter.CTkButton(self, text="Clear", command = self.clear)
        self.clear.pack(pady= 10,padx= 15)
        
        self.result_label = customtkinter.CTkLabel(self, text="")
        self.result_label.pack()
        

        self.protocol("WM_DELETE_WINDOW", self.on_closing)



    def create_menu(self):
        # Create a menu bar
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        
        

        # Create a File menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="eng ca")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save",command = self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.on_closing)

        # Create an Edit menu
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Cut", command = self.cut_text)
        self.editmenu.add_command(label="Copy", command=self.copy_text)
        self.editmenu.add_command(label="Paste", command=self.paste_text)
        self.editmenu.add_command(label="zoom in", command=self.zoom_in)
        self.editmenu.add_command(label="zoom out", command=self.zoom_out)


    def check_spelling(self):
        # Get text from the entry widget
        text_to_check = self.text_input.get("1.0", tk.END)

        # Initialize SpellChecker
        spell = SpellChecker()

        # Get misspelled words
        misspelled = spell.unknown(text_to_check.split())
        
        # Display the result
        if misspelled:
            result_text = f"     \n Check spelling : {', '.join(misspelled)}"
            self.text_input.configure(text_color="red")
            self.result_label.configure(text=result_text,text_color="red")
        else:
            result_text = "      \nNo misspelled words found."
            # Insert the result_text with the "red" tag
            self.text_input.configure(text_color="#D3D3D3")
            self.result_label.configure(text=result_text,text_color="#D3D3D3")
            
         
        

        

    def zoom_in(self):
        
        self.text_input_font = self.text_input.cget("font")
        # Get the current font size
        current_size = self.text_input_font.actual()['size']
        new_size = current_size + 20  # Increase the font size by 2
        new_font = (self.text_input_font.actual()['family'], new_size)
        self.text_input.configure(font=new_font)
        # Store the new CTkFont object
        self.text_input_font = self.text_input.cget("font")

    def zoom_out(self):
        # Get the current font size
        current_size = self.text_input_font.actual()['size']
        new_size = max(1, current_size - 2)  # Decrease the font size by 2, but not less than 1
        new_font = (self.text_input_font.actual()['family'], new_size)
        self.text_input.configure(font=new_font)
        # Store the new CTkFont object
        self.text_input_font = self.text_input.cget("font")



       

     
    def copy_text(self):
        # Clear the clipboard
        self.clipboard_clear()
        
        text = self.text_input.get("1.0",tk.END)
        # Copy the selected text from the text_input widget to the clipboard
        self.clipboard_append(text)
    
    
    def cut_text(self):
        # Clear the clipboard
        self.clipboard_clear()
        text = self.text_input.get("1.0",tk.END)
        self.text_input.delete("1.0",tk.END)
        # Copy the selected text from the text_input widget to the clipboard
        self.clipboard_append(text)



        # Insert the text from the clipboard to the text_input widget at the cursor position
    def paste_text(self):
        try:
            self.text_input.insert(tk.INSERT, self.clipboard_get())
        except tk.TclError:
            pass



        # Open a save file dialog and get the selected file path
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])



    # removes text from CTKtestbox    
    def clear(self):
        self.text_input.delete('1.0', tk.END)
        self.text_input.configure(text_color="#D3D3D3")
        self.result_label.configure(text="Let's try again", text_color= "#D3D3D3")
     
     
     

    def on_closing(self):
        if messagebox.askyesno(title="Quit", message="Do you really want to quit?"):
            self.destroy()

SpellCheckerApp = SpellCheckerApp()
SpellCheckerApp.mainloop()
