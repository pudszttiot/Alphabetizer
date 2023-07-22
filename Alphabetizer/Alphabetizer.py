import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Alphabetizer")

        self.label = tk.Label(master, text="Enter a list separated by line breaks:", font=('Courier New', 12, 'bold'), fg='black')
        self.label.pack()

        self.text_frame = tk.Frame(master)
        self.text_frame.pack()

        self.paste_button = tk.Button(self.text_frame, text="Paste", font=('Arial', 12, 'bold'), bg="#2BAE66", fg="#FCF6F5", command=self.paste_input, padx=5, pady=5)
        self.paste_button.pack(side=tk.TOP, pady=10, anchor='center')

        self.text_scrollbar = tk.Scrollbar(self.text_frame, orient=tk.HORIZONTAL)
        self.text_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.text = scrolledtext.ScrolledText(self.text_frame, height=10, wrap=tk.NONE, xscrollcommand=self.text_scrollbar.set, padx=5, pady=5)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_scrollbar.config(command=self.text.xview)

        self.button = tk.Button(master, text="ALPHABETIZE!", font=('Arial', 14, 'bold'), bg="#101820", fg="#1FFF0F", command=self.alphabetize, padx=5, pady=5)
        self.button.pack(side=tk.TOP, pady=10, anchor='center')

        self.output_frame = tk.Frame(master)
        self.output_frame.pack()

        self.output_scrollbar = tk.Scrollbar(self.output_frame, orient=tk.HORIZONTAL)
        self.output_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, height=10, wrap=tk.NONE, state='disabled', xscrollcommand=self.output_scrollbar.set, padx=5, pady=5)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.output_scrollbar.config(command=self.output_text.xview)

        self.copy_button = tk.Button(master, text="Copy", font=('Arial', 12, 'bold'), bg="#2BAE66", fg="#FCF6F5", command=self.copy_result, padx=5, pady=5)
        self.copy_button.pack(side=tk.TOP, pady=10, anchor='center')

        # Start the GUI window maximized
        master.state('zoomed')

    def paste_input(self):
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', self.master.clipboard_get())
        
    def alphabetize(self):
        input_list = self.text.get("1.0", "end").split('\n')
        if input_list := [x.strip() for x in input_list if x.strip()]:
            input_list.sort()
            output = "\n".join(input_list)
            self.output_text.configure(state='normal')
            self.output_text.delete('1.0', 'end')
            self.output_text.insert('1.0', output)
            self.output_text.configure(state='disabled')
        else:
            self.output_text.configure(state='normal')
            self.output_text.delete('1.0', 'end')
            self.output_text.configure(state='disabled')
            self.output_label.configure(text="Output: Please enter a list!")
        
    def copy_result(self):
        result = self.output_text.get("1.0", "end-1c")
        self.master.clipboard_clear()
        self.master.clipboard_append(result)
        messagebox.showinfo("TTIOT", "The alphabetized order has been copied to the clipboard.")

root = tk.Tk()
app = App(root)
root.mainloop()
