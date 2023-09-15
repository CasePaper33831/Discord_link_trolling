'''TODO:
none at the moment

finish:
-user input secret_url
-user input displayed url
-put in popup for easy copy/paste
-auto size popup for ease of copy/paste 
'''
import tkinter as tk

def display_popup():
    secret_url = secret_entry.get()
    displayed_url = display_entry.get()
    
    popup = tk.Toplevel(root)
    popup.title("Popup")
    
    text_widget = tk.Text(popup)
    text_widget.pack()
    
    formatted_text = ""
    for letter in displayed_url:
        formatted_text += f'[{letter}](<{secret_url}>)'
    
    text_widget.insert("1.0", formatted_text)

root = tk.Tk()
root.title("URL Input")
root.geometry("400x200")

display_label = tk.Label(root, text="Please input the fake link here:")
display_label.pack()

display_entry = tk.Entry(root)
display_entry.pack()

secret_label = tk.Label(root, text="Please input the actual link here:")
secret_label.pack()

secret_entry = tk.Entry(root)
secret_entry.pack()

submit_button = tk.Button(root, text="Generate Popup", command=display_popup)
submit_button.pack()

root.mainloop()
